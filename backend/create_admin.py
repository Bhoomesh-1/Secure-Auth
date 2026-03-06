"""
Helper script to create an admin user.
Run this script to create an admin user in the system.

Usage:
    python create_admin.py
"""

import bcrypt
import sys

# Import the user database (in production, use a real database)
# For this script, we'll simulate the user creation
users_db = {}

def hash_password(password):
    """Hash password using bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def create_admin():
    """Create an admin user"""
    print("=" * 50)
    print("Admin User Creation")
    print("=" * 50)
    
    name = input("Enter admin name: ").strip()
    if not name:
        print("Error: Name cannot be empty")
        return
    
    email = input("Enter admin email: ").strip().lower()
    if not email or '@' not in email:
        print("Error: Invalid email format")
        return
    
    password = input("Enter admin password: ").strip()
    if len(password) < 8:
        print("Error: Password must be at least 8 characters")
        return
    
    confirm_password = input("Confirm admin password: ").strip()
    if password != confirm_password:
        print("Error: Passwords do not match")
        return
    
    # Hash password
    hashed_password = hash_password(password)
    
    # Create admin user
    admin_user = {
        'id': len(users_db) + 1,
        'name': name,
        'email': email,
        'password': hashed_password,
        'role': 'admin'
    }
    
    users_db[email] = admin_user
    
    print("\n" + "=" * 50)
    print("Admin user created successfully!")
    print("=" * 50)
    print(f"Name: {admin_user['name']}")
    print(f"Email: {admin_user['email']}")
    print(f"Role: {admin_user['role']}")
    print("\nNote: In production, this should be stored in a database.")
    print("For now, add this user to the users_db in app.py manually.")
    print("\nTo add to app.py, add this line after users_db initialization:")
    print(f"users_db['{email}'] = {admin_user}")

if __name__ == '__main__':
    try:
        create_admin()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
        sys.exit(0)
