
import unittest
from app import app

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_register_user(self):
        response = self.app.post('/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User registered successfully', response.get_data(as_text=True))

    def test_register_existing_user(self):
        self.app.post('/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        response = self.app.post('/register', json={
            'username': 'testuser',
            'email': 'testuser@example.com'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('User already exists', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()