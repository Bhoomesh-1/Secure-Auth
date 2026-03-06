from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, create_refresh_token
)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from email_validator import validate_email, EmailNotValidError
import bcrypt
import os
import time
from datetime import timedelta, datetime
from functools import wraps
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your-secret-key-change-in-production-please-use-env-var')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)
app.config['JWT_COOKIE_SECURE'] = os.environ.get('FLASK_ENV') != 'development'
app.config['JWT_COOKIE_HTTPONLY'] = True
app.config['JWT_COOKIE_SAMESITE'] = 'Lax'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_COOKIE_NAME'] = 'access_token'
app.config['JWT_REFRESH_COOKIE_NAME'] = 'refresh_token'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False  # Disable CSRF for API

# Initialize extensions
jwt = JWTManager(app)

# CORS configuration - allow credentials
CORS(app, 
     origins=["http://localhost:3000", "http://127.0.0.1:3000"],
     supports_credentials=True,
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

# Rate limiting with in-memory storage
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

# Database setup
DATABASE_URL = "sqlite:///app.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Example model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Track failed login attempts for rate limiting
failed_login_attempts = {}
# Track user sessions
user_sessions = {}

def get_current_time():
    """Get current timestamp"""
    return time.time()

def validate_password_strength(password):
    """Validate password meets security requirements"""
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"
    
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"
    
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one number"
    
    if not any(c in "!@#$%^&*(),.?\":{}|<>" for c in password):
        return False, "Password must contain at least one special character"
    
    return True, None

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    """Verify password against hash"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
    except Exception:
        return False

def set_token_cookies(response, access_token, refresh_token):
    """Set HTTP-only cookies for tokens"""
    max_age_access = int(timedelta(hours=1).total_seconds())
    max_age_refresh = int(timedelta(days=30).total_seconds())
    
    response.set_cookie(
        'access_token',
        access_token,
        max_age=max_age_access,
        httponly=True,
        secure=app.config['JWT_COOKIE_SECURE'],
        samesite=app.config['JWT_COOKIE_SAMESITE'],
        path='/'
    )
    response.set_cookie(
        'refresh_token',
        refresh_token,
        max_age=max_age_refresh,
        httponly=True,
        secure=app.config['JWT_COOKIE_SECURE'],
        samesite=app.config['JWT_COOKIE_SAMESITE'],
        path='/'
    )
    return response

def clear_token_cookies(response):
    """Clear token cookies"""
    response.set_cookie('access_token', '', expires=0, httponly=True, path='/', samesite='Lax')
    response.set_cookie('refresh_token', '', expires=0, httponly=True, path='/', samesite='Lax')
    return response

def admin_required(f):
    """Decorator to require admin role"""
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        try:
            email = get_jwt_identity()
            
            # Check if user exists in database
            db = SessionLocal()
            try:
                user = db.query(User).filter(User.email == email).first()
                
                if not user:
                    return jsonify({'message': 'User not found'}), 404
                
                # For now, only allow admin access if user is in a special admin list
                # In a real application, you'd add an 'is_admin' field to the User model
                admin_emails = ['admin@example.com']  # This should be configurable
                if email not in admin_emails:
                    return jsonify({'message': 'Admin access required'}), 403
                
                return f(*args, **kwargs)
                
            finally:
                db.close()
                
        except Exception as e:
            return jsonify({'message': f'Authorization failed: {str(e)}'}), 401
    return decorated_function

# JWT Error Handlers
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({'message': 'Token has expired'}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({'message': 'Invalid token'}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({'message': 'Authorization required'}), 401

@app.route('/api/auth/register', methods=['POST', 'OPTIONS'])
@limiter.limit("5 per minute")
def register():
    """User registration endpoint with rate limiting"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        data = request.get_json()

        if not data:
            return jsonify({'message': 'No data provided'}), 400

        # Validate required fields
        if not all(k in data for k in ['name', 'email', 'password']):
            return jsonify({'message': 'Missing required fields: name, email, password'}), 400

        name = data['name'].strip()
        email = data['email'].strip().lower()
        password = data['password']

        # Input validation
        if len(name) < 2 or len(name) > 100:
            return jsonify({'message': 'Name must be between 2 and 100 characters'}), 400

        # Validate email format
        try:
            # Use basic email validation instead of strict validation
            if '@' not in email or '.' not in email.split('@')[-1]:
                raise EmailNotValidError("Invalid email format")
        except EmailNotValidError:
            return jsonify({'message': 'Invalid email format'}), 400

        # Validate password strength
        is_valid, error_msg = validate_password_strength(password)
        if not is_valid:
            return jsonify({'message': error_msg}), 400

        db = SessionLocal()
        try:
            # Check if user already exists
            if db.query(User).filter(User.email == email).first():
                return jsonify({'message': 'User with this email already exists'}), 409

            # Hash password
            hashed_password = hash_password(password)

            # Create user
            new_user = User(username=name, email=email, password_hash=hashed_password)
            db.add(new_user)
            db.commit()

            # Generate tokens
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)

            # Create response with cookies
            response = make_response(jsonify({
                'message': 'User registered successfully',
                'user': {
                    'id': new_user.id,
                    'name': new_user.username,
                    'email': new_user.email
                }
            }), 201)

            # Set HTTP-only cookies
            response = set_token_cookies(response, access_token, refresh_token)
            return response
        finally:
            db.close()

    except Exception as e:
        app.logger.error(f'Registration error: {str(e)}')
        return jsonify({'message': f'Registration failed: {str(e)}'}), 500

@app.route('/api/auth/login', methods=['POST', 'OPTIONS'])
@limiter.limit("5 per minute")
def login():
    """User login endpoint with rate limiting"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'message': 'No data provided'}), 400
        
        # Validate required fields
        if not all(k in data for k in ['email', 'password']):
            return jsonify({'message': 'Email and password are required'}), 400
        
        email = data['email'].strip().lower()
        password = data['password']
        
        # Check rate limiting for this email
        if email in failed_login_attempts:
            attempts, last_attempt = failed_login_attempts[email]
            if attempts >= 5:
                time_since = get_current_time() - last_attempt
                if time_since < 300:  # 5 minutes lockout
                    # Track blocked attempt
                    if email in user_sessions:
                        user_sessions[email]['blocked_attempts'] += 1
                    return jsonify({
                        'message': 'Too many failed login attempts. Please try again in 5 minutes.'
                    }), 429
                else:
                    # Reset after lockout period
                    del failed_login_attempts[email]
        
        # Check if user exists in database
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.email == email).first()
            
            if not user:
                # Track failed attempt
                if email not in failed_login_attempts:
                    failed_login_attempts[email] = [0, 0]
                failed_login_attempts[email][0] += 1
                failed_login_attempts[email][1] = get_current_time()
                return jsonify({'message': 'Invalid email or password'}), 401
            
            # Verify password
            if not verify_password(password, user.password_hash):
                # Track failed attempt
                if email not in failed_login_attempts:
                    failed_login_attempts[email] = [0, 0]
                failed_login_attempts[email][0] += 1
                failed_login_attempts[email][1] = get_current_time()
                # Track blocked attempt
                if email in user_sessions:
                    user_sessions[email]['blocked_attempts'] += 1
                return jsonify({'message': 'Invalid email or password'}), 401
            
            # Successful login - clear failed attempts
            if email in failed_login_attempts:
                del failed_login_attempts[email]
            
            # Generate tokens
            access_token = create_access_token(identity=email)
            refresh_token = create_refresh_token(identity=email)
            
            # Update session tracking
            if email not in user_sessions:
                user_sessions[email] = {
                    'login_count': 0,
                    'last_login': None,
                    'blocked_attempts': 0
                }
            user_sessions[email]['login_count'] += 1
            user_sessions[email]['last_login'] = datetime.now().isoformat()
            
            # Create response with cookies
            response = make_response(jsonify({
                'message': 'Login successful',
                'user': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'role': 'user'  # Default role
                }
            }), 200)
            
            # Set HTTP-only cookies
            response = set_token_cookies(response, access_token, refresh_token)
            return response
            
        finally:
            db.close()
        
    except Exception as e:
        app.logger.error(f'Login error: {str(e)}')
        return jsonify({'message': f'Login failed: {str(e)}'}), 500

@app.route('/api/auth/verify', methods=['GET', 'OPTIONS'])
@jwt_required()
def verify_token():
    """Verify JWT token and return user info"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        email = get_jwt_identity()
        
        # Check if user exists in database
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.email == email).first()
            
            if not user:
                return jsonify({'message': 'User not found'}), 404
            
            return jsonify({
                'user': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'role': 'user'  # Default role
                }
            }), 200
            
        finally:
            db.close()
        
    except Exception as e:
        app.logger.error(f'Verify error: {str(e)}')
        return jsonify({'message': f'Token verification failed: {str(e)}'}), 401

@app.route('/api/auth/security-stats', methods=['GET', 'OPTIONS'])
@jwt_required()
def get_security_stats():
    """Get security statistics for the current user"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        email = get_jwt_identity()
        
        # Check if user exists in database
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.email == email).first()
            
            if not user:
                return jsonify({'message': 'User not found'}), 404
            
            session_data = user_sessions.get(email, {
                'login_count': 0,
                'last_login': None,
                'blocked_attempts': 0
            })
            
            # Calculate session duration (simplified)
            session_duration = 0
            if session_data['last_login']:
                try:
                    last_login = datetime.fromisoformat(session_data['last_login'])
                    session_duration = int((datetime.now() - last_login).total_seconds() / 60)
                except:
                    pass
            
            return jsonify({
                'login_attempts': session_data['login_count'],
                'blocked_attempts': session_data['blocked_attempts'],
                'session_duration': session_duration,
                'last_login': session_data['last_login'],
                'security_features': {
                    'http_only_cookies': True,
                    'bcrypt_encryption': True,
                    'rate_limiting': True,
                    'token_refresh': True
                }
            }), 200
            
        finally:
            db.close()
        
    except Exception as e:
        app.logger.error(f'Security stats error: {str(e)}')
        return jsonify({'message': f'Failed to get security stats: {str(e)}'}), 500

@app.route('/api/auth/refresh', methods=['POST', 'OPTIONS'])
@jwt_required(refresh=True)
def refresh():
    """Refresh access token"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        email = get_jwt_identity()
        new_token = create_access_token(identity=email)
        
        # Create response with new cookie
        response = make_response(jsonify({'message': 'Token refreshed successfully'}), 200)
        response.set_cookie(
            'access_token',
            new_token,
            max_age=int(timedelta(hours=1).total_seconds()),
            httponly=True,
            secure=app.config['JWT_COOKIE_SECURE'],
            samesite=app.config['JWT_COOKIE_SAMESITE'],
            path='/'
        )
        return response
        
    except Exception as e:
        app.logger.error(f'Refresh error: {str(e)}')
        return jsonify({'message': f'Token refresh failed: {str(e)}'}), 401

@app.route('/api/auth/logout', methods=['POST', 'OPTIONS'])
def logout():
    """Logout endpoint - clears cookies (works even without valid token)"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    # Clear cookies regardless of token validity
    response = make_response(jsonify({'message': 'Logged out successfully'}), 200)
    response = clear_token_cookies(response)
    return response

@app.route('/api/admin/users', methods=['GET', 'OPTIONS'])
@admin_required
def get_all_users():
    """Admin endpoint to get all users"""
    if request.method == 'OPTIONS':
        return make_response(), 200
        
    try:
        db = SessionLocal()
        try:
            users = db.query(User).all()
            
            users_list = []
            for user in users:
                users_list.append({
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'role': 'user',  # Default role
                    'created_at': None,  # Would need to add created_at field to model
                    'last_login': user_sessions.get(user.email, {}).get('last_login')
                })
            
            return jsonify({'users': users_list}), 200
            
        finally:
            db.close()
            
    except Exception as e:
        app.logger.error(f'Get users error: {str(e)}')
        return jsonify({'message': f'Failed to retrieve users: {str(e)}'}), 500

@app.route('/', methods=['GET'])
def root():
    """Root endpoint with API information"""
    return jsonify({
        'message': 'Secure Authentication API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'POST /api/auth/register': 'Register a new user',
            'POST /api/auth/login': 'Login with email and password',
            'GET /api/auth/verify': 'Verify JWT token and get user info',
            'GET /api/auth/security-stats': 'Get security statistics',
            'POST /api/auth/refresh': 'Refresh access token',
            'POST /api/auth/logout': 'Logout and clear cookies',
            'GET /api/admin/users': 'Get all users (admin only)',
            'GET /api/health': 'Health check endpoint'
        }
    }), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        db = SessionLocal()
        try:
            users_count = db.query(User).count()
            return jsonify({
                'status': 'healthy',
                'message': 'Server is running',
                'users_count': users_count
            }), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'message': f'Server error: {str(e)}',
            'users_count': 0
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Enhanced 404 error handler"""
    return jsonify({
        'message': 'Endpoint not found',
        'available_endpoints': [
            'GET /',
            'POST /api/auth/register',
            'POST /api/auth/login',
            'GET /api/auth/verify',
            'GET /api/auth/security-stats',
            'POST /api/auth/refresh',
            'POST /api/auth/logout',
            'GET /api/admin/users',
            'GET /api/health'
        ],
        'tip': 'Visit GET / for API documentation'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'message': 'Internal server error',
        'error': str(error) if app.debug else 'Contact administrator'
    }), 500

@app.errorhandler(429)
def ratelimit_handler(e):
    """Rate limit error handler"""
    return jsonify({
        'message': 'Rate limit exceeded',
        'error': 'Too many requests. Please try again later.'
    }), 429

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Enable debug mode for development (set FLASK_ENV=production to disable)
    debug = os.environ.get('FLASK_ENV', 'development') != 'production'
    print(f"Starting server on port {port} (debug={debug})")
    print(f"API available at: http://localhost:{port}")
    print(f"Environment: {os.environ.get('FLASK_ENV', 'development')}")
    app.run(host='0.0.0.0', port=port, debug=debug)
