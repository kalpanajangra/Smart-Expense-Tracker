# Smart Expense Tracker API

A RESTful Expense Tracker API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The application allows users to securely manage their expenses with JWT authentication and provides filtering options to analyze expenses efficiently.

## Features

* User Registration
* User Login using JWT Authentication
* Create, Read, Update, and Delete (CRUD) Expenses
* Filter Expenses by Category
* Filter Expenses by Date Range
* Filter Expenses by Amount Range
* PostgreSQL Database Integration
* SQLAlchemy ORM
* Interactive Swagger API Documentation

## Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* JWT Authentication
* Uvicorn

## API Documentation

After starting the server, you can access the interactive API documentation:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

## Project Structure

Smart-Expense-Tracker/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore


