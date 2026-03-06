# Quick Start Guide

## Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Windows:
   venv\Scripts\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   python app.py
   ```
   
   Server will start on `http://localhost:5000`

## Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```
   
   Frontend will start on `http://localhost:3000`

## Testing the Application

1. **Open browser:** `http://localhost:3000`

2. **Register a new user:**
   - Click "Sign up here"
   - Fill in name, email, and password
   - Password must meet requirements (8+ chars, uppercase, lowercase, number, special char)

3. **Login:**
   - Use your registered credentials
   - You'll be redirected to dashboard

4. **Test API directly:**
   ```bash
   # Health check
   curl http://localhost:5000/api/health
   
   # Register
   curl -X POST http://localhost:5000/api/auth/register \
     -H "Content-Type: application/json" \
     -d '{"name":"Test User","email":"test@example.com","password":"Test123!@#"}'
   
   # Login (cookies will be set automatically)
   curl -X POST http://localhost:5000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email":"test@example.com","password":"Test123!@#"}' \
     -c cookies.txt
   
   # Verify (use cookies)
   curl http://localhost:5000/api/auth/verify -b cookies.txt
   ```

## Creating an Admin User

To create an admin user, manually add to `users_db` in `app.py`:

```python
# Add this after users_db initialization in app.py
users_db['admin@example.com'] = {
    'id': 1,
    'name': 'Admin User',
    'email': 'admin@example.com',
    'password': hash_password('AdminPass123!'),  # Use hash_password function
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

## Troubleshooting

### Backend Issues

1. **Port already in use:**
   - Change port in `app.py` or set `PORT` environment variable
   - Kill process using port 5000

2. **Module not found:**
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt` again

3. **CORS errors:**
   - Check that frontend URL matches CORS origins in `app.py`
   - Ensure `supports_credentials=True` is set

### Frontend Issues

1. **Cannot connect to backend:**
   - Verify backend is running on port 5000
   - Check `REACT_APP_API_URL` in `.env` file (if using custom URL)

2. **Cookies not working:**
   - Ensure `withCredentials: true` is set in axios
   - Check browser console for CORS errors
   - Verify cookies are being set in DevTools → Application → Cookies

3. **Authentication not persisting:**
   - Check browser console for errors
   - Verify `/api/auth/verify` endpoint is working
   - Check network tab to see if cookies are being sent

## Environment Variables

Create a `.env` file in the backend directory:

```env
FLASK_ENV=development
PORT=5000
JWT_SECRET_KEY=your-super-secret-key-here-change-this
```

Generate a secure JWT secret:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

## Security Notes

- ✅ HTTP-only cookies prevent XSS attacks
- ✅ Rate limiting prevents brute force
- ✅ Password hashing with bcrypt
- ✅ Input validation on all endpoints
- ⚠️ Change JWT_SECRET_KEY in production
- ⚠️ Use HTTPS in production
- ⚠️ Replace in-memory storage with database
