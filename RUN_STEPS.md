# 📋 Step-by-Step: How to Run Backend and Frontend

## 🎯 Quick Steps

### **STEP 1: Open First Terminal (Backend)**

1. Open PowerShell or Command Prompt
2. Copy and paste these commands one by one:

```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
```

```powershell
venv\Scripts\activate
```

```powershell
python app.py
```

**✅ You should see:**
```
Starting server on port 5000 (debug=True)
API available at: http://localhost:5000
 * Running on http://0.0.0.0:5000
```

**⏸️ LEAVE THIS TERMINAL OPEN!** Don't close it.

---

### **STEP 2: Open Second Terminal (Frontend)**

1. Open a **NEW** PowerShell or Command Prompt window
2. Copy and paste these commands one by one:

```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\frontend"
```

```powershell
npm start
```

**✅ You should see:**
```
Compiled successfully!

You can now view secure-auth-frontend in the browser.

  Local:            http://localhost:3000
```

**🌐 Browser will open automatically!**

**⏸️ LEAVE THIS TERMINAL OPEN TOO!** Don't close it.

---

## ✅ That's It!

Now you have:
- ✅ Backend running on port 5000
- ✅ Frontend running on port 3000
- ✅ Browser showing the application

---

## 🎯 What Happens Next

1. Browser opens to `http://localhost:3000`
2. You see the **Home Page** with navigation
3. Click **"Get Started"** or **"Sign Up"**
4. Fill the registration form
5. After signup, you'll see the **Welcome Page**
6. Navigate through the app!

---

## ⚠️ Important Notes

- **Keep BOTH terminals open** while using the app
- If you close a terminal, that server stops
- Backend must run on port 5000
- Frontend must run on port 3000
- Browser should show `http://localhost:3000`

---

## 🐛 Troubleshooting

### If backend doesn't start:
```powershell
# Make sure you're in the backend folder
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"

# Activate virtual environment
venv\Scripts\activate

# Install dependencies if needed
pip install -r requirements.txt

# Then run
python app.py
```

### If frontend doesn't start:
```powershell
# Make sure you're in the frontend folder
cd "c:\Users\GOUDA BHOOMESH\capstone project\frontend"

# Install dependencies if needed
npm install

# Then run
npm start
```

### If browser doesn't open:
- Manually go to: `http://localhost:3000`

---

## 📝 Summary

**Terminal 1 (Backend):**
```
cd backend
venv\Scripts\activate
python app.py
```

**Terminal 2 (Frontend):**
```
cd frontend
npm start
```

**That's all you need! 🎉**
