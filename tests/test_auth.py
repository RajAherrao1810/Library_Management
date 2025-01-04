import unittest
from app import app
from database import execute_query

class TestAuth(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create test database tables
        execute_query("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, name TEXT, email TEXT, joined_date TEXT)")
        execute_query("CREATE TABLE IF NOT EXISTS tokens (id INTEGER PRIMARY KEY, member_id INTEGER, token TEXT)")
        execute_query("INSERT INTO members (name, email, joined_date) VALUES ('Test Member', 'test@example.com', '2023-01-01')")

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_login(self):
        data = {"email": "test@example.com"}
        response = self.app.post('/auth/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.get_json())

    def test_validate_token(self):
        # Generate a valid token for testing
        execute_query("INSERT INTO tokens (member_id, token) VALUES (1, 'testtoken')")
        data = {"token": "testtoken"}
        response = self.app.post('/auth/validate', json=data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_token(self):
        data = {"token": "invalidtoken"}
        response = self.app.post('/auth/validate', json=data)
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
