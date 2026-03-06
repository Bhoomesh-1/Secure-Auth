# Secure Authentication Backend - Capstone Level

A production-ready secure authentication backend built with Flask and JWT, implementing industry-standard security practices.

## Features

- 🔐 User registration with email validation
- 🔑 Secure password hashing with bcrypt
- 🛡️ JWT token-based authentication with HTTP-only cookies
- 🔒 Password strength validation
- ✅ Token verification endpoint
- 🔄 Token refresh mechanism
- 🌐 CORS enabled for frontend integration
- 🚦 Rate limiting for login/register endpoints (5 per minute)
- 👑 Role-based access control (user/admin)
- 🔐 HTTP-only cookie storage (no localStorage)
- 🛡️ Brute force protection (5 failed attempts = 5 min lockout)
- 🔒 Secure cookie configuration (SameSite, HttpOnly, Secure in production)

## Installation

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Copy the example environment file:
```bash
copy .env.example .env  # Windows
cp .env.example .env    # macOS/Linux
```

2. Edit `.env` and set a strong `JWT_SECRET_KEY`:
```bash
# Generate a secure key:
python -c "import secrets; print(secrets.token_hex(32))"
```

## Running the Server

Start the Flask development server:
```bash
python app.py
```

The server will run on `http://localhost:5000`

## API Endpoints

### POST `/api/auth/register`
Register a new user.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "message": "User registered successfully",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }
}
```

**Note:** Tokens are automatically set as HTTP-only cookies. No tokens are returned in the response body for security.

### POST `/api/auth/login`
Login with email and password.

**Request Body:**
```json
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

**Response:**
```json
{
  "message": "Login successful",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }
}
```

**Note:** Tokens are automatically set as HTTP-only cookies. No tokens are returned in the response body for security.

**Rate Limiting:** Maximum 5 login attempts per minute per IP address.

### GET `/api/auth/verify`
Verify JWT token and get user info.

**Authentication:** HTTP-only cookies (automatic) or Authorization header

**Response:**
```json
{
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "role": "user"
  }
}
```

### POST `/api/auth/refresh`
Refresh access token using refresh token cookie.

**Authentication:** HTTP-only refresh_token cookie (automatic)

**Response:**
```json
{
  "message": "Token refreshed successfully"
}
```

**Note:** New access token is set as HTTP-only cookie automatically.

### POST `/api/auth/logout`
Logout and clear authentication cookies.

**Authentication:** HTTP-only access_token cookie (automatic)

**Response:**
```json
{
  "message": "Logged out successfully"
}
```

**Note:** Cookies are automatically cleared by the server.

### GET `/api/admin/users` (Admin Only)
Get all users. Requires admin role.

**Authentication:** HTTP-only access_token cookie with admin role

**Response:**
```json
{
  "users": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "role": "user"
    }
  ]
}
```

### GET `/api/health`
Health check endpoint.

## Security Features

- **HTTP-Only Cookies**: Tokens stored in HTTP-only cookies (not accessible via JavaScript)
- **Password Hashing**: Uses bcrypt with salt for secure password storage
- **JWT Tokens**: Secure token-based authentication with access and refresh tokens
- **Password Validation**: Enforces strong password requirements
- **Email Validation**: Validates email format using email-validator
- **CORS**: Configured for secure cross-origin requests with credentials
- **Rate Limiting**: Prevents brute force attacks (5 attempts per minute)
- **Brute Force Protection**: Account lockout after 5 failed login attempts (5 minutes)
- **Role-Based Access Control**: User and admin roles with protected endpoints
- **Secure Cookies**: SameSite, HttpOnly, and Secure (in production) flags
- **Input Validation**: All inputs are validated and sanitized

## Password Requirements

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&*(),.?":{}|<>)

## Creating Admin Users

To create an admin user, you can manually add one to the `users_db` in `app.py`:

```python
# Add this after users_db initialization
users_db['admin@example.com'] = {
    'id': 1,
    'name': 'Admin User',
    'email': 'admin@example.com',
    'password': hash_password('AdminPass123!'),  # Use hash_password function
    'role': 'admin'
}
```

Or use the helper script:
```bash
python create_admin.py
```

## Production Considerations

⚠️ **Important for Production:**

1. ✅ Replace in-memory user storage with a database (PostgreSQL, MongoDB, etc.)
2. ✅ Use environment variables for all secrets
3. ✅ Set a strong `JWT_SECRET_KEY` (generate with: `python -c "import secrets; print(secrets.token_hex(32))"`)
4. ✅ Enable HTTPS (cookies will automatically use Secure flag)
5. ✅ Rate limiting implemented
6. ⚠️ Implement proper logging (add logging middleware)
7. ✅ Input validation and sanitization implemented
8. ⚠️ Use a production WSGI server (gunicorn, uWSGI)
9. ⚠️ Add database connection pooling
10. ⚠️ Implement password reset functionality
11. ⚠️ Add email verification
12. ⚠️ Implement session management
13. ⚠️ Add security headers (Helmet.js equivalent for Flask)
14. ⚠️ Set up monitoring and alerting
