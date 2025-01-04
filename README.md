# Library Management System

## Description
This project implements a **Library Management System** using Flask, SQLAlchemy, and a simple HTML frontend. The system allows for basic CRUD (Create, Read, Update, Delete) operations for managing books and members in the library. It also includes an option to view books and add/delete them from the system, with a home page for navigation.


## 1. How to Run the Project

### Step 1: Clone the repository


### Step 1: Clone the repository
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system

### Step 2: Install Dependencies
pip install -r requirements.txt

### Step 3: Run the Flask application
python app.py
By default, Flask will run on http://127.0.0.1:5000/.

###Step 4: Open the browser and go to http://127.0.0.1:5000/.


## 2. Design Choices

### 1] Flask as the Web Framework:
    Flask is chosen for its simplicity and minimalism. It allows us to quickly set up routes and implement CRUD functionality with minimal boilerplate code.

### 2]SQLAlchemy for Database Management:
    SQLAlchemy is used as the ORM for interacting with the SQLite database. This provides an easy way to manage the database schema, perform queries, and handle relationships between entities.
    The database schema includes two models: Book (for storing information about books) and Member (for storing library member details).

### 3]Templates and Static Files:
    The HTML templates are rendered using Jinja2 templating engine, which is built into Flask. It allows us to dynamically display books and handle user input.
    Static assets like CSS files are stored in the /static directory to style the frontend pages.

### 4] CRUD Operations:
    Create: Books can be added through a form in the frontend (add a book).
    Read: The list of books can be viewed on the home page.
    Update: Books can be edited in the database (though this feature is not implemented yet).
    Delete: Books can be removed from the system with a delete button next to each book.


## 3. Assumptions or Limitations

### 1] Assumptions:

    The system is assumed to work only for books and members, without any advanced features like late fees or book reservations.
    The app uses an SQLite database for simplicity, making it suitable for small-scale projects and testing. It may not scale well for large production environments.
    The Book model includes attributes like title, author, and published_year, but does not currently include more advanced fields such as isbn.
    Only basic input validation is applied (checking for missing data), and more advanced validation or error handling may be needed in a real-world application.

### 2]Limitations:
    The Update feature is not yet implemented. Books can only be added and deleted.
    The system does not provide pagination for the book listing page, so if the number of books grows large, the page may become slow or cumbersome.