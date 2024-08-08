Here's the updated `README.md` file with the admin credentials included:

---

# 📚 BookHub

**BookHub** is a web application designed to help users discover and explore books. It features powerful search functionality and an intuitive interface to browse and view book details. The project leverages Django for the backend, ensuring a robust and scalable application, with a responsive and interactive frontend.

## ✨ Features

- **🔍 Book Search**: Users can search for books using keywords.
- **📑 Book Results**: Displays search results with detailed information.
- **📘 Book Details**: View comprehensive details about a selected book.
- **📱 Responsive Design**: Optimized for various devices and screen sizes.

## 🛠️ Technologies Used

- **🧰 Django**: Backend framework for building the web application.
- **🎨 HTML/CSS**: For structuring and styling the frontend.
- **⚙️ JavaScript**: Enables interactivity and dynamic content updates.
- **📚 Google Books API**: Integrated for fetching book data.

## 🚀 Installation and Setup

### 📝 Prerequisites

- 🐍 Python 3.12 or higher
- 📦 pip (Python package installer)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vishalraj9102/Book-Recommendations-System.git
cd Book-Recommendations-System
```

### 2️⃣ Apply Migrations

Apply the initial database migrations to set up the database schema.

```bash
python manage.py migrate
```

### 3️⃣ Create a Superuser (Optional)

Create a superuser to access the Django admin interface.

```bash
python manage.py createsuperuser
```

### 4️⃣ Run the Development Server

Start the Django development server to run the application locally.

```bash
python manage.py runserver
```

### 5️⃣ Access the Application

- 🌐 Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

- 🔑 For Admin access, go to `http://127.0.0.1:8000/admin/`.

  - **Admin Credentials**:
    - **Username**: `vishalraj`
    - **Password**: `vishal@8341`

## 🔗 API Endpoints

### **📚 BookViewSet Endpoints**

- **📝 List All Books**

  - **Endpoint**: `/api/books/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all books.

- **🔎 Search Books**

  - **Endpoint**: `/api/books/search/`
  - **Method**: `GET`
  - **Description**: Searches for books using a query parameter `q` to fetch data from the Google Books API.

- **⭐ Featured Books**

  - **Endpoint**: `/api/recommendations/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all featured book recommendations.

- **👍 Like a Recommendation**

  - **Endpoint**: `/api/recommendations/<int:pk>/like/`
  - **Method**: `POST`
  - **Description**: Increments the number of likes for a specific recommendation.

### **📚 CustomBookDataViewSet Endpoints**

- **📝 List All Custom Book Data**

  - **Endpoint**: `/api/custombookdata/`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all custom book data entries.

- **➕ Create Custom Book Data**

  - **Endpoint**: `/api/custombookdata/`
  - **Method**: `POST`
  - **Description**: Creates a new entry for custom book data.

## 🤝 Contributing

If you'd like to contribute to the project, please fork the repository and submit a pull request with your changes. For detailed information on contributing, please refer to the `CONTRIBUTING.md` file.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## 📧 Contact

For any questions or feedback, please contact [vishalrajmehra95@gmail.com](mailto:vishalrajmehra95@gmail.com).

![BookHub Screenshot](book_recommendations\assets\images\img1.png)





---

This version of the `README.md` file now includes the admin credentials, making it easier for others to access the admin interface during development or testing.
