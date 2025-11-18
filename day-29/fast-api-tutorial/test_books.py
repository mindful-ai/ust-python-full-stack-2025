import unittest
import requests
import time
from threading import Thread
from books import app
from fastapi.testclient import TestClient

# Base URL for the API
BASE_URL = "http://localhost:8000"

class TestBooksAPI(unittest.TestCase):
    """Test suite for Books API endpoints"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test client"""
        cls.client = TestClient(app)
    
    def setUp(self):
        """Clear books before each test"""
        # Access the app's books dictionary and clear it
        from books import books
        books.clear()
    
    def tearDown(self):
        """Clean up after each test"""
        from books import books
        books.clear()
    
    # ==================== GET ALL BOOKS ====================
    def test_get_all_books_empty(self):
        """Test getting all books when list is empty"""
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})
    
    def test_get_all_books_with_data(self):
        """Test getting all books with data"""
        # Create a book first
        book_data = {"title": "1984", "author": "George Orwell"}
        self.client.post("/books/1", json=book_data)
        
        # Get all books
        response = self.client.get("/books")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("1", data)
        self.assertEqual(data["1"]["title"], "1984")
        self.assertEqual(data["1"]["author"], "George Orwell")
    
    # ==================== CREATE BOOK ====================
    def test_create_book_success(self):
        """Test creating a book successfully"""
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        response = self.client.post("/books/1", json=book_data)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Book created")
        self.assertEqual(data["book"]["title"], "The Great Gatsby")
        self.assertEqual(data["book"]["author"], "F. Scott Fitzgerald")
    
    def test_create_multiple_books(self):
        """Test creating multiple books"""
        books_to_create = [
            {"title": "1984", "author": "George Orwell"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
            {"title": "Pride and Prejudice", "author": "Jane Austen"}
        ]
        
        for idx, book_data in enumerate(books_to_create, 1):
            response = self.client.post(f"/books/{idx}", json=book_data)
            self.assertEqual(response.status_code, 200)
        
        # Verify all were created
        response = self.client.get("/books")
        self.assertEqual(len(response.json()), 3)
    
    def test_create_book_duplicate_id(self):
        """Test creating a book with an ID that already exists"""
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        
        # Create first book
        response1 = self.client.post("/books/1", json=book_data)
        self.assertEqual(response1.status_code, 200)
        
        # Try to create another with same ID
        response2 = self.client.post("/books/1", json={"title": "1984", "author": "George Orwell"})
        self.assertEqual(response2.status_code, 400)
        self.assertIn("already exists", response2.json()["detail"])
    
    def test_create_book_missing_fields(self):
        """Test creating a book with missing required fields"""
        # Missing author field
        response = self.client.post("/books/1", json={"title": "The Great Gatsby"})
        self.assertEqual(response.status_code, 422)  # Validation error
    
    def test_create_book_invalid_json(self):
        """Test creating a book with invalid JSON"""
        response = self.client.post(
            "/books/1", 
            data="invalid json",
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 422)
    
    # ==================== GET SPECIFIC BOOK ====================
    def test_get_book_success(self):
        """Test retrieving a specific book"""
        # Create a book
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        self.client.post("/books/1", json=book_data)
        
        # Get the book
        response = self.client.get("/books/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["title"], "The Great Gatsby")
        self.assertEqual(data["author"], "F. Scott Fitzgerald")
    
    def test_get_book_not_found(self):
        """Test retrieving a non-existent book"""
        response = self.client.get("/books/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.json()["detail"])
    
    def test_get_book_with_different_ids(self):
        """Test retrieving books with different IDs"""
        books_data = [
            {"title": "1984", "author": "George Orwell"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
        ]
        
        for idx, book in enumerate(books_data, 1):
            self.client.post(f"/books/{idx}", json=book)
        
        # Get first book
        response1 = self.client.get("/books/1")
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response1.json()["title"], "1984")
        
        # Get second book
        response2 = self.client.get("/books/2")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response2.json()["title"], "To Kill a Mockingbird")
    
    # ==================== UPDATE BOOK ====================
    def test_update_book_success(self):
        """Test updating a book successfully"""
        # Create a book
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        self.client.post("/books/1", json=book_data)
        
        # Update the book
        updated_data = {"title": "The Great Gatsby - Revised Edition", "author": "F. Scott Fitzgerald"}
        response = self.client.put("/books/1", json=updated_data)
        
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["message"], "Book updated")
        self.assertEqual(data["book"]["title"], "The Great Gatsby - Revised Edition")
    
    def test_update_book_not_found(self):
        """Test updating a non-existent book"""
        updated_data = {"title": "Updated Title", "author": "Updated Author"}
        response = self.client.put("/books/999", json=updated_data)
        
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.json()["detail"])
    
    def test_update_book_partial_change(self):
        """Test updating only certain fields"""
        # Create a book
        book_data = {"title": "1984", "author": "George Orwell"}
        self.client.post("/books/1", json=book_data)
        
        # Update only title
        updated_data = {"title": "Nineteen Eighty-Four", "author": "George Orwell"}
        response = self.client.put("/books/1", json=updated_data)
        
        self.assertEqual(response.status_code, 200)
        retrieved = self.client.get("/books/1").json()
        self.assertEqual(retrieved["title"], "Nineteen Eighty-Four")
        self.assertEqual(retrieved["author"], "George Orwell")
    
    def test_update_book_missing_fields(self):
        """Test updating a book with missing required fields"""
        # Create a book
        book_data = {"title": "1984", "author": "George Orwell"}
        self.client.post("/books/1", json=book_data)
        
        # Try to update with missing field
        response = self.client.put("/books/1", json={"title": "Updated Title"})
        self.assertEqual(response.status_code, 422)  # Validation error
    
    # ==================== DELETE BOOK ====================
    def test_delete_book_success(self):
        """Test deleting a book successfully"""
        # Create a book
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        self.client.post("/books/1", json=book_data)
        
        # Delete the book
        response = self.client.delete("/books/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Book deleted")
        
        # Verify it's deleted
        response = self.client.get("/books/1")
        self.assertEqual(response.status_code, 404)
    
    def test_delete_book_not_found(self):
        """Test deleting a non-existent book"""
        response = self.client.delete("/books/999")
        self.assertEqual(response.status_code, 404)
        self.assertIn("not found", response.json()["detail"])
    
    def test_delete_book_twice(self):
        """Test deleting the same book twice"""
        # Create a book
        book_data = {"title": "1984", "author": "George Orwell"}
        self.client.post("/books/1", json=book_data)
        
        # Delete once
        response1 = self.client.delete("/books/1")
        self.assertEqual(response1.status_code, 200)
        
        # Try to delete again
        response2 = self.client.delete("/books/1")
        self.assertEqual(response2.status_code, 404)
    
    # ==================== WORKFLOW TESTS ====================
    def test_full_crud_workflow(self):
        """Test complete CRUD workflow"""
        # Create
        book_data = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
        create_response = self.client.post("/books/1", json=book_data)
        self.assertEqual(create_response.status_code, 200)
        
        # Read
        read_response = self.client.get("/books/1")
        self.assertEqual(read_response.status_code, 200)
        self.assertEqual(read_response.json()["title"], "The Great Gatsby")
        
        # Update
        updated_data = {"title": "The Great Gatsby - Classics Edition", "author": "F. Scott Fitzgerald"}
        update_response = self.client.put("/books/1", json=updated_data)
        self.assertEqual(update_response.status_code, 200)
        
        # Verify update
        verify_response = self.client.get("/books/1")
        self.assertEqual(verify_response.json()["title"], "The Great Gatsby - Classics Edition")
        
        # Delete
        delete_response = self.client.delete("/books/1")
        self.assertEqual(delete_response.status_code, 200)
        
        # Verify deletion
        final_response = self.client.get("/books/1")
        self.assertEqual(final_response.status_code, 404)
    
    def test_multiple_books_operations(self):
        """Test operations on multiple books"""
        # Create 3 books
        books_data = [
            {"title": "1984", "author": "George Orwell"},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
            {"title": "Pride and Prejudice", "author": "Jane Austen"}
        ]
        
        for idx, book in enumerate(books_data, 1):
            response = self.client.post(f"/books/{idx}", json=book)
            self.assertEqual(response.status_code, 200)
        
        # Get all
        response = self.client.get("/books")
        self.assertEqual(len(response.json()), 3)
        
        # Update one
        updated = {"title": "Nineteen Eighty-Four", "author": "George Orwell"}
        response = self.client.put("/books/1", json=updated)
        self.assertEqual(response.status_code, 200)
        
        # Delete one
        response = self.client.delete("/books/2")
        self.assertEqual(response.status_code, 200)
        
        # Verify final state
        response = self.client.get("/books")
        books_list = response.json()
        self.assertEqual(len(books_list), 2)
        self.assertIn("1", books_list)
        self.assertNotIn("2", books_list)
        self.assertIn("3", books_list)


class TestBooksAPIWithLiveServer(unittest.TestCase):
    """Test suite using live server (optional - requires server running)"""
    
    def setUp(self):
        """Set up for live server tests"""
        self.base_url = BASE_URL
        # Check if server is running
        try:
            requests.get(f"{self.base_url}/docs", timeout=2)
            self.server_available = True
        except requests.exceptions.ConnectionError:
            self.server_available = False
    
    def test_live_server_connection(self):
        """Test if the live server is reachable"""
        if not self.server_available:
            self.skipTest("Live server not available on localhost:8000")
        
        response = requests.get(f"{self.base_url}/books")
        self.assertEqual(response.status_code, 200)
    
    def test_live_server_create_book(self):
        """Test creating a book on live server"""
        if not self.server_available:
            self.skipTest("Live server not available on localhost:8000")
        
        book_data = {"title": "Test Book", "author": "Test Author"}
        response = requests.post(f"{self.base_url}/books/100", json=book_data)
        
        # May be 200 or 400 depending on server state
        self.assertIn(response.status_code, [200, 400])


if __name__ == "__main__":
    # Run tests with verbose output
    unittest.main(verbosity=2)
