# Setup Instructions

## Environment Variables

Create a `.env` file in the backend directory with the following:

```
FLASK_ENV=development
PORT=5000
JWT_SECRET_KEY=your-super-secret-key-change-this-in-production
```

To generate a secure JWT secret key, run:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
