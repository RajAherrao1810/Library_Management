import unittest
from app import app
from database import execute_query

class TestBooks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a test database table
        execute_query("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, published_year INTEGER, genre TEXT)")
        execute_query("INSERT INTO books (title, author, published_year, genre) VALUES ('Test Book', 'Author Test', 2020, 'Fiction')")

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_books(self):
        response = self.app.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        data = {
            "title": "New Book",
            "author": "New Author",
            "published_year": 2021,
            "genre": "Non-Fiction"
        }
        response = self.app.post('/books/', json=data)
        self.assertEqual(response.status_code, 201)

    def test_get_book(self):
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": "Updated Author",
            "published_year": 2022,
            "genre": "Fantasy"
        }
        response = self.app.put('/books/1', json=data)
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
