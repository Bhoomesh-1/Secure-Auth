# Fix Frontend Dependency Issue

## Quick Fix (Run these commands)

### Step 1: Delete node_modules and package-lock.json
```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\frontend"
Remove-Item -Recurse -Force node_modules
Remove-Item -Force package-lock.json
```

### Step 2: Clear npm cache
```powershell
npm cache clean --force
```

### Step 3: Reinstall dependencies
```powershell
npm install
```

### Step 4: Start the app
```powershell
npm start
```

---

## Alternative: If above doesn't work

### Option 1: Use yarn instead of npm
```powershell
# Install yarn globally (if not installed)
npm install -g yarn

# Then use yarn
yarn install
yarn start
```

### Option 2: Update Node.js
- Make sure you have Node.js 16+ installed
- Download from: https://nodejs.org/

### Option 3: Manual fix
```powershell
npm install ajv@^8.12.0 --save
npm install
npm start
```
