# BookHub

BookHub is a web application designed to help users discover and explore books. It features search functionality to find books and view their details. This project uses Django for the backend and offers a responsive and interactive user interface.

## Features
- **Book Search**: Users can search for books using keywords.
- **Book Results**: Displays search results with book details.
- **Book Details**: Shows detailed information about a selected book.
- **Responsive Design**: Optimized for various devices and screen sizes.

## Technologies Used
- **Django**: Framework for building the web application.
- **HTML/CSS**: For structuring and styling the frontend.
- **JavaScript**: For interactivity and dynamic content updates.
- **Google Books API**: Integrated for fetching book data.

## Installation and Setup

### Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bookhub.git
cd bookhub

### 1. Apply Migrations
Apply the initial database migrations to set up the database schema.
- python manage.py migrate

### 2.Create a Superuser
(Optional) Create a superuser to access the Django admin interface.
- python manage.py createsuperuser

### 3.Run the Development Server
Start the Django development server to run the application locally.
- python manage.py runserver

### 3.Run the Development Server
Access the Application
- Open your browser and navigate to http://127.0.0.1:8000/ to view the application.

For Admin
- Open your browser and navigate to http://127.0.0.1:8000/admin/ to view the application.
