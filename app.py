from flask import Flask, render_template, request, jsonify, redirect
from database import init_db, db_session, Book, Member

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        published_year = request.form.get('published_year')
        
        if title and author and published_year:
            try:
                published_year = int(published_year)
                book = Book(title=title, author=author, published_year=published_year)
                db_session.add(book)
                db_session.commit()
                return redirect('/books')  # Redirect back to books page
            except ValueError:
                return jsonify({"message": "Invalid year"}), 400
        return jsonify({"message": "Invalid input"}), 400

    books = db_session.query(Book).all()
    return render_template('books.html', books=books)


@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book = db_session.query(Book).get(book_id)
    if book:
        db_session.delete(book)
        db_session.commit()
        return jsonify({"message": "Book deleted successfully"}), 200
    return jsonify({"message": "Book not found"}), 404


@app.route('/books/<int:book_id>', methods=['PUT', 'DELETE'])
def modify_books(book_id):
    book = db_session.query(Book).get(book_id)
    if not book:
        return jsonify({"message": "Book not found"}), 404

    if request.method == 'PUT':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        if title and author:
            book.title = title
            book.author = author
            db_session.commit()
            return jsonify({"message": "Book updated successfully"})
        return jsonify({"message": "Invalid input"}), 400

    if request.method == 'DELETE':
        db_session.delete(book)
        db_session.commit()
        return jsonify({"message": "Book deleted successfully"})

@app.route('/members', methods=['GET', 'POST'])
def manage_members():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        if name and email:
            member = Member(name=name, email=email)
            db_session.add(member)
            db_session.commit()
            return jsonify({"message": "Member added successfully"})
        return jsonify({"message": "Invalid input"}), 400

    members = db_session.query(Member).all()
    member_list = [{"id": member.id, "name": member.name, "email": member.email} for member in members]
    return jsonify(member_list)

@app.route('/members/<int:member_id>', methods=['PUT', 'DELETE'])
def modify_members(member_id):
    member = db_session.query(Member).get(member_id)
    if not member:
        return jsonify({"message": "Member not found"}), 404

    if request.method == 'PUT':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        if name and email:
            member.name = name
            member.email = email
            db_session.commit()
            return jsonify({"message": "Member updated successfully"})
        return jsonify({"message": "Invalid input"}), 400

    if request.method == 'DELETE':
        db_session.delete(member)
        db_session.commit()
        return jsonify({"message": "Member deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
