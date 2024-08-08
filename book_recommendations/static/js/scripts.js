document.addEventListener('DOMContentLoaded', function() {
    fetchFeaturedBooks();

    document.getElementById('search-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const query = document.getElementById('search-query').value.trim();
        if (query) {
            searchBooks(query);
        }
    });
});

function fetchFeaturedBooks() {
    fetch('/api/books/featured/')
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch featured books');
            return response.json();
        })
        .then(data => {
            const carouselDiv = document.getElementById('featured-books');
            carouselDiv.innerHTML = '';
            if (data.length === 0) {
                carouselDiv.innerHTML = '<p>No featured books available at the moment.</p>';
            } else {
                data.forEach(book => {
                    const bookCover = book.thumbnail || 'placeholder.jpg'; // Adjust according to your book model
                    carouselDiv.innerHTML += `
                        <img src="${bookCover}" alt="${book.title}" onclick="showBookDetail('${book.id}')">
                    `;
                });
            }
        })
        .catch(error => console.error('Error fetching featured books:', error));
}

function searchBooks(query) {
    const loadingIndicator = document.getElementById('loading');
    const resultsDiv = document.getElementById('book-results');

    loadingIndicator.classList.remove('hidden');
    resultsDiv.innerHTML = '';

    fetch(`/api/books/search/?q=${encodeURIComponent(query)}`)
        .then(response => {
            if (!response.ok) throw new Error('Failed to search books');
            return response.json();
        })
        .then(data => {
            if (data.items && data.items.length > 0) {
                data.items.forEach(item => {
                    const book = item.volumeInfo;
                    const bookCover = book.imageLinks ? book.imageLinks.thumbnail : 'placeholder.jpg';
                    resultsDiv.innerHTML += `
                        <div class="book-card" onclick="showBookDetail('${item.id}')">
                            <img src="${bookCover}" alt="${book.title}">
                            <h3>${book.title}</h3>
                            <p>${book.authors ? book.authors.join(', ') : 'Unknown Author'}</p>
                            <p>${book.description ? book.description.substring(0, 100) + '...' : 'No description available'}</p>
                        </div>
                    `;
                });
            } else {
                resultsDiv.innerHTML = '<p>No books found. Please try a different search.</p>';
            }
        })
        .catch(error => {
            console.error('Error searching books:', error);
            resultsDiv.innerHTML = '<p>There was an error fetching the search results. Please try again later.</p>';
        })
        .finally(() => {
            loadingIndicator.classList.add('hidden');
        });
}

function showBookDetail(bookId) {
    const bookDetailDiv = document.getElementById('book-detail');
    bookDetailDiv.classList.add('hidden');

    fetch(`/api/books/${bookId}/`)
        .then(response => {
            if (!response.ok) throw new Error('Failed to fetch book details');
            return response.json();
        })
        .then(data => {
            const book = data.volumeInfo || {}; // Adjust according to your API response
            const bookCover = book.imageLinks ? book.imageLinks.thumbnail : 'placeholder.jpg';
            bookDetailDiv.innerHTML = `
                <div>
                    <img src="${bookCover}" alt="${book.title}">
                    <div>
                        <h3>${book.title}</h3>
                        <p><strong>Authors:</strong> ${book.authors ? book.authors.join(', ') : 'Unknown Author'}</p>
                        <p><strong>Published Date:</strong> ${book.publishedDate || 'Unknown'}</p>
                        <p><strong>Description:</strong> ${book.description || 'No description available'}</p>
                    </div>
                </div>
            `;
            bookDetailDiv.classList.remove('hidden');
        })
        .catch(error => console.error('Error fetching book details:', error));
}
