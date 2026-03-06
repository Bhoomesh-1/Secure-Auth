# How to Activate Virtual Environment in PowerShell

## Problem
PowerShell might block the activation script due to execution policy.

## Solution 1: Use Full Path (Easiest)

```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
.\venv\Scripts\Activate.ps1
```

## Solution 2: Change Execution Policy (One Time)

Run this in PowerShell as Administrator:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then you can use:
```powershell
venv\Scripts\activate
```

## Solution 3: Use Command Prompt Instead

If PowerShell keeps giving issues, use Command Prompt (cmd):

```cmd
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
venv\Scripts\activate.bat
```

## Solution 4: Bypass Execution Policy (Temporary)

```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
powershell -ExecutionPolicy Bypass -File .\venv\Scripts\Activate.ps1
```

## Quick Fix - Try This First:

```powershell
cd "c:\Users\GOUDA BHOOMESH\capstone project\backend"
.\venv\Scripts\Activate.ps1
```

If that doesn't work, use Solution 3 (Command Prompt) - it's the most reliable!
