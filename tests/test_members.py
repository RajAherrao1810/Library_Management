import unittest
from app import app
from database import execute_query

class TestMembers(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test database table
        execute_query("CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY, name TEXT, email TEXT, joined_date TEXT)")
        execute_query("INSERT INTO members (name, email, joined_date) VALUES ('Test Member', 'test@example.com', '2023-01-01')")

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_members(self):
        response = self.app.get('/members/')
        self.assertEqual(response.status_code, 200)

    def test_add_member(self):
        data = {
            "name": "New Member",
            "email": "newmember@example.com",
            "joined_date": "2023-05-01"
        }
        response = self.app.post('/members/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_member(self):
        response = self.app.get('/members/1')
        self.assertEqual(response.status_code, 200)

    def test_update_member(self):
        data = {
            "name": "Updated Member",
            "email": "updated@example.com",
            "joined_date": "2023-06-01"
        }
        response = self.app.put('/members/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_member(self):
        response = self.app.delete('/members/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
