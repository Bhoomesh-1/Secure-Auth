# Secure Web Authentication Protocol System

A capstone-level secure authentication system built with React (frontend) and Flask (backend), implementing industry-standard security practices.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup (5 minutes)

```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run server
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend Setup (3 minutes)

```bash
# 1. Navigate to frontend (in a new terminal)
cd frontend

# 2. Install dependencies
npm install

# 3. Start development server
npm start
```

Frontend will run on `http://localhost:3000` and open automatically in your browser.

## ✅ Features

### Security Features
- ✅ **HTTP-Only Cookies** - Tokens stored securely, not accessible via JavaScript
- ✅ **Bcrypt Password Hashing** - Industry-standard password encryption
- ✅ **JWT Authentication** - Access and refresh token system
- ✅ **Rate Limiting** - Prevents brute force attacks (5 attempts/minute)
- ✅ **Brute Force Protection** - Account lockout after 5 failed attempts
- ✅ **Role-Based Access Control** - User and Admin roles
- ✅ **Input Validation** - All inputs validated and sanitized
- ✅ **CORS Protection** - Secure cross-origin requests
- ✅ **Secure Cookie Configuration** - HttpOnly, Secure, SameSite flags

### User Features
- ✅ User Registration with password strength validation
- ✅ Secure Login
- ✅ Protected Dashboard
- ✅ Logout functionality
- ✅ Session persistence
- ✅ Admin panel (for admin users)

## 🛠️ New Features

### Backend Enhancements
- SQLite database integration with SQLAlchemy
- User registration and authentication API endpoints
- Admin role-based access control

### Frontend Enhancements
- Login integrated with backend API
- Improved Navbar with accessibility features

## 📁 Project Structure

```
capstone project/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── requirements.txt     # Python dependencies
│   ├── test_api.py         # API test script
│   └── README.md           # Backend documentation
├── frontend/
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── context/       # Auth context
│   │   └── App.js         # Main app
│   ├── package.json       # Node dependencies
│   └── README.md         # Frontend documentation
├── README.md              # This file
└── QUICK_START.md         # Quick start guide
```

## 🔧 Configuration

### Backend Environment Variables

Create a `.env` file in the `backend` directory:

```env
FLASK_ENV=development
PORT=5000
JWT_SECRET_KEY=your-super-secret-key-here
```

Generate a secure JWT secret:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Frontend Configuration

The frontend is configured to connect to `http://localhost:5000` by default. To change this, create a `.env` file in the `frontend` directory:

```env
REACT_APP_API_URL=http://localhost:5000
```

## 🧪 Testing

### Backend Tests
Run the following command to execute backend tests:

```bash
cd backend
python -m unittest discover
```

### Manual Testing

1. **Register a user:**
   - Open `http://localhost:3000`
   - Click "Sign up here"
   - Fill in the registration form
   - Password must: 8+ chars, uppercase, lowercase, number, special char

2. **Login:**
   - Use your registered credentials
   - You'll be redirected to dashboard

3. **Test Protected Route:**
   - Try accessing dashboard without login (should redirect to login)
   - Login and verify dashboard loads

4. **Test Logout:**
   - Click logout button
   - Should redirect to login page

## 📡 API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/` | API documentation | No |
| GET | `/api/health` | Health check | No |
| POST | `/api/auth/register` | Register new user | No |
| POST | `/api/auth/login` | User login | No |
| GET | `/api/auth/verify` | Verify token | Yes |
| POST | `/api/auth/refresh` | Refresh token | Yes (refresh) |
| POST | `/api/auth/logout` | Logout | No |
| GET | `/api/admin/users` | List all users | Yes (admin) |

## 🔐 Creating Admin User

To create an admin user, add this to `app.py` after `users_db = {}`:

```python
# Create admin user
users_db['admin@example.com'] = {
    'id': 1,
    'name': 'Admin User',
    'email': 'admin@example.com',
    'password': hash_password('AdminPass123!'),
    'role': 'admin'
}
```

Or use Python console:
```python
from app import hash_password, users_db
users_db['admin@example.com'] = {
    'id': 1,
    'name': 'Admin',
    'email': 'admin@example.com',
    'password': hash_password('AdminPass123!'),
    'role': 'admin'
}
```

## 🐛 Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Change port in app.py or set environment variable
set PORT=5001  # Windows
export PORT=5001  # macOS/Linux
```

**Module not found:**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

**CORS errors:**
- Check that frontend URL matches CORS origins in `app.py`
- Ensure `supports_credentials=True` is set

### Frontend Issues

**Cannot connect to backend:**
- Verify backend is running on port 5000
- Check browser console for errors
- Verify `REACT_APP_API_URL` in `.env` file

**Cookies not working:**
- Check browser DevTools → Application → Cookies
- Verify `withCredentials: true` in axios config
- Check for CORS errors in console

**Authentication not persisting:**
- Check browser console for errors
- Verify `/api/auth/verify` endpoint works
- Check network tab to see if cookies are sent

## 📝 Password Requirements

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character (!@#$%^&*(),.?":{}|<>)

## 🚨 Security Notes

### Production Checklist

- [ ] Change `JWT_SECRET_KEY` to a strong random value
- [ ] Enable HTTPS (cookies will automatically use Secure flag)
- [ ] Replace in-memory user storage with database
- [ ] Set `FLASK_ENV=production`
- [ ] Configure proper CORS origins
- [ ] Add logging and monitoring
- [ ] Implement password reset functionality
- [ ] Add email verification
- [ ] Set up rate limiting with Redis (for distributed systems)

## 📚 Documentation

- `QUICK_START.md` - Quick setup guide
- `backend/README.md` - Backend API documentation
- `frontend/README.md` - Frontend documentation
- `UPGRADE_SUMMARY.md` - Security upgrade details

## 🎯 Next Steps

1. **Database Integration** - Replace in-memory storage with PostgreSQL/MongoDB
2. **Email Verification** - Add email confirmation on registration
3. **Password Reset** - Implement forgot password functionality
4. **Two-Factor Authentication** - Add 2FA for enhanced security
5. **Session Management** - Track active sessions and devices
6. **Audit Logging** - Log all authentication events

## 📄 License

This project is for educational/capstone purposes.

## 👤 Support

For issues or questions:
1. Check the troubleshooting section
2. Review the documentation files
3. Check browser console and server logs for errors

---

**Status:** ✅ Production-Ready (with database migration)
**Security Level:** Capstone-Grade
**Last Updated:** 2024
