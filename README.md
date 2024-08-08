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
https://github.com/vishalraj9102/Book-Recommendations-System.git

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

```bash

### 2. API Endpoints

BookViewSet Endpoints
List All Books

Endpoint: /api/books/
Method: GET
Description: Retrieves a list of all books.
Create a Book

Endpoint: /api/books/search/
Method: GET
Description: Searches for books using a query parameter q to fetch data from the Google Books API.
Featured Books

Endpoint: /api/recommendations/
Method: GET
Description: Retrieves a list of all recommendations.
Create a Recommendation


Endpoint: /api/recommendations/<int:pk>/like/
Method: POST
Description: Increments the number of likes for a specific recommendation.
CustomBookDataViewSet Endpoints
List All Custom Book Data

Endpoint: /api/custombookdata/
Method: GET
Description: Retrieves a list of all custom book data entries.
Create Custom Book Data



###3. Contributing
    If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. For detailed information on contributing, please refer to the CONTRIBUTING.md file.

License
    This project is licensed under the MIT License - see the LICENSE file for details.

Contact
    For any questions or feedback, please contact vishalrajmehra95@gmail.com


This `README.md` file now includes all the necessary details for setting up and running the project, as well as the available API endpoints and their usage examples. Adjust the email address and any other specific details as needed.



