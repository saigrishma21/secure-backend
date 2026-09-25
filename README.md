# 🔐 Secure Backend API

A secure and production-oriented backend API built using **Python, FastAPI, SQLAlchemy, SQLite, JWT Authentication, Role-Based Access Control (RBAC), Secure File Uploads, Pytest, and Docker**.

This project demonstrates how to build a backend application with authentication, authorization, database management, file validation, automated testing, environment-based configuration, containerization, and GitHub version control.

---

## 📌 Project Overview

The Secure Backend API provides a set of REST APIs for:

- User registration
- Secure password hashing
- User login
- JWT-based authentication
- Protected API endpoints
- Role-Based Access Control (RBAC)
- Admin-only operations
- Secure file uploads
- File type validation
- File size validation
- Application logging
- Automated API testing
- Environment variable management
- Docker containerization

The application is built using **FastAPI** and can be tested through the automatically generated **Swagger UI**.

---

## 🚀 Features

### 🔑 Authentication

- User registration
- User login
- bcrypt password hashing
- JWT access token generation
- JWT token validation
- Token expiration
- Bearer authentication

### 🛡️ Authorization

- Protected API endpoints
- Role-Based Access Control
- User role
- Admin role
- Admin-only endpoints
- HTTP 401 and 403 handling

### 📁 File Upload

- Authenticated file uploads
- Allowed file extensions
- Maximum file size of 5 MB
- UUID-based stored filenames
- Protection against directly trusting user-supplied filenames

### 🗄️ Database

- SQLite database
- SQLAlchemy ORM
- User model
- Unique username and email
- Database session management

### 🧪 Testing

- Pytest
- FastAPI TestClient
- Authentication testing
- Protected endpoint testing
- Registration testing
- Login testing

### 🐳 Docker

- Dockerfile
- Docker image creation
- Docker container execution
- Environment variable injection
- Docker ignore configuration

### 🔒 Security

- Passwords are never stored as plain text
- JWT authentication
- Role-based authorization
- File validation
- File size restrictions
- Environment-based secret key
- `.env` excluded from Git
- Database and uploaded files excluded from Git

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Uvicorn | ASGI server |
| SQLAlchemy | ORM and database interaction |
| SQLite | Relational database |
| Passlib | Password hashing |
| bcrypt | Secure password hashing algorithm |
| python-jose | JWT creation and verification |
| Pydantic | Request validation |
| python-multipart | File upload handling |
| python-dotenv | Environment variable management |
| Pytest | Automated testing |
| Docker | Containerization |
| Git | Version control |
| GitHub | Source code hosting |

---

## 📂 Project Structure

```text
secure-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   │
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── files.py
│
├── tests/
│   ├── __init__.py
│   └── test_auth.py
│
├── uploads/
│
├── .env
├── .gitignore
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── app.db
