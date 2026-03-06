"""
Simple test script to verify API endpoints are working
Run this after starting the server: python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("Testing /api/health...")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")

def test_register():
    """Test user registration"""
    print("Testing /api/auth/register...")
    data = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "Test123!@#"
    }
    response = requests.post(
        f"{BASE_URL}/api/auth/register",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print(f"Cookies set: {bool(response.cookies.get('access_token'))}\n")
    return response.cookies

def test_login():
    """Test user login"""
    print("Testing /api/auth/login...")
    data = {
        "email": "test@example.com",
        "password": "Test123!@#"
    }
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json=data,
        headers={"Content-Type": "application/json"}
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print(f"Cookies set: {bool(response.cookies.get('access_token'))}\n")
    return response.cookies

def test_verify(cookies):
    """Test token verification"""
    print("Testing /api/auth/verify...")
    response = requests.get(
        f"{BASE_URL}/api/auth/verify",
        cookies=cookies
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")

def test_logout(cookies):
    """Test logout"""
    print("Testing /api/auth/logout...")
    response = requests.post(
        f"{BASE_URL}/api/auth/logout",
        cookies=cookies
    )
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}\n")

if __name__ == "__main__":
    print("=" * 50)
    print("API Test Suite")
    print("=" * 50)
    print()
    
    try:
        # Test health
        test_health()
        
        # Test register
        cookies = test_register()
        
        # Test login
        cookies = test_login()
        
        # Test verify
        test_verify(cookies)
        
        # Test logout
        test_logout(cookies)
        
        print("=" * 50)
        print("All tests completed!")
        print("=" * 50)
        
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to server.")
        print("Make sure the server is running: python app.py")
    except Exception as e:
        print(f"ERROR: {str(e)}")
