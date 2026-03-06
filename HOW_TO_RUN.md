# How to Run the Application

## Step-by-Step Instructions

### Prerequisites Check
- ✅ Python 3.8 or higher installed
- ✅ Node.js 14 or higher installed
- ✅ npm (comes with Node.js)

---

## Part 1: Backend Setup (Terminal 1)

### Step 1: Open Terminal/Command Prompt
Open your terminal or command prompt.

### Step 2: Navigate to Backend Folder
```bash
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
```

### Step 3: Create Virtual Environment
```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

**For Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

**For Windows (Command Prompt):**
```bash
venv\Scripts\activate.bat
```

**For macOS/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your command prompt.

### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

Wait for all packages to install. This may take 1-2 minutes.

### Step 6: Run the Backend Server
```bash
python app.py
```

You should see:
```
Starting server on port 5000 (debug=True)
API available at: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

**✅ Backend is now running! Keep this terminal open.**

---

## Part 2: Frontend Setup (Terminal 2)

### Step 1: Open a NEW Terminal/Command Prompt
Open a **second** terminal window (keep the backend terminal running).

### Step 2: Navigate to Frontend Folder
```bash
cd "c:\Users\GOUDA BHOOMESH\capstone project\frontend"
```

### Step 3: Install Dependencies
```bash
npm install
```

Wait for all packages to install. This may take 2-3 minutes.

### Step 4: Start the Frontend Server
```bash
npm start
```

The browser should automatically open to `http://localhost:3000`

**✅ Frontend is now running!**

---

## Part 3: Using the Application

### 1. Register a New User
- Click **"Sign up here"** link
- Fill in:
  - **Name**: Your full name
  - **Email**: Your email address
  - **Password**: Must meet requirements:
    - At least 8 characters
    - One uppercase letter
    - One lowercase letter
    - One number
    - One special character (!@#$%^&*...)
- Click **"Sign Up"**

### 2. Login
- Enter your email and password
- Click **"Sign In"**
- You'll be redirected to the Dashboard

### 3. Logout
- Click the **"Logout"** button in the dashboard
- You'll be redirected to the login page

---

## Quick Commands Summary

### Backend (Terminal 1):
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
python app.py
```

### Frontend (Terminal 2):
```bash
cd frontend
npm install
npm start
```

---

## Troubleshooting

### Backend Issues

**Problem: "python is not recognized"**
- Solution: Use `py` instead of `python`:
  ```bash
  py -m venv venv
  py app.py
  ```

**Problem: "Port 5000 already in use"**
- Solution: Kill the process using port 5000 or change port:
  ```bash
  # Windows: Find and kill process
  netstat -ano | findstr :5000
  taskkill /PID <PID_NUMBER> /F
  
  # Or change port in app.py (line 456)
  port = int(os.environ.get('PORT', 5001))
  ```

**Problem: "Module not found"**
- Solution: Make sure virtual environment is activated and install again:
  ```bash
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

### Frontend Issues

**Problem: "npm is not recognized"**
- Solution: Install Node.js from https://nodejs.org/

**Problem: "Port 3000 already in use"**
- Solution: The terminal will ask if you want to use a different port. Type `Y` and press Enter.

**Problem: "Cannot connect to backend"**
- Solution: Make sure backend is running on port 5000
- Check browser console (F12) for errors
- Verify `http://localhost:5000/api/health` works in browser

**Problem: "Cookies not working"**
- Solution: 
  - Clear browser cache and cookies
  - Try a different browser
  - Check that both servers are running

---

## Testing the API

### Test Backend Directly

Open browser and visit:
- `http://localhost:5000` - API documentation
- `http://localhost:5000/api/health` - Health check

### Test with Python Script

```bash
cd backend
python test_api.py
```

---

## Stopping the Servers

### To Stop Backend:
- In Terminal 1, press `Ctrl + C`

### To Stop Frontend:
- In Terminal 2, press `Ctrl + C`

---

## Next Time You Run

### Backend:
```bash
cd backend
venv\Scripts\activate    # Activate virtual environment
python app.py           # Run server
```

### Frontend:
```bash
cd frontend
npm start               # Run server (dependencies already installed)
```

---

## Need Help?

1. **Check both terminals** - Make sure both servers are running
2. **Check browser console** - Press F12, look for errors
3. **Check server logs** - Look at terminal output for errors
4. **Verify ports** - Backend: 5000, Frontend: 3000

---

**✅ You're all set! The application should now be running smoothly.**
