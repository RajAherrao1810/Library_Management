// Add Book
document.getElementById('addBookForm')?.addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;

    fetch('/books', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, author })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        location.reload();
    });
});

// Load Books
document.addEventListener('DOMContentLoaded', () => {
    const bookList = document.getElementById('bookList');
    fetch('/books')
        .then(response => response.json())
        .then(data => {
            bookList.innerHTML = data.map(book => `
                <div data-id="${book.id}">
                    <h2>${book.title}</h2>
                    <p>${book.author}</p>
                    <button class="deleteBook">Delete</button>
                </div>
            `).join('');
        });
});

// Delete Book
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('deleteBook')) {
        const bookId = e.target.parentElement.getAttribute('data-id');
        fetch(`/books/${bookId}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                location.reload();
            });
    }
});
