# Secure Authentication Frontend

A modern, secure authentication frontend built with React.

## Features

- 🔐 Secure login and registration
- 🛡️ Protected routes with authentication
- 🔑 JWT token-based authentication
- 📱 Responsive design
- ✨ Modern UI with smooth animations
- 🔒 Password strength validation
- 👁️ Password visibility toggle

## Installation

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

## Running the Application

Start the development server:
```bash
npm start
```

The app will open at `http://localhost:3000`

## Environment Variables

Create a `.env` file in the frontend directory:

```
REACT_APP_API_URL=http://localhost:5000
```

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── Login.js
│   │   ├── Register.js
│   │   ├── Dashboard.js
│   │   ├── ProtectedRoute.js
│   │   ├── Auth.css
│   │   └── Dashboard.css
│   ├── context/
│   │   └── AuthContext.js
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## Security Features

- Password strength requirements (8+ chars, uppercase, lowercase, number, special char)
- JWT token storage in localStorage
- Automatic token verification
- Protected routes
- Secure API communication with axios
