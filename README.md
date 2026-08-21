# 💰 Smart Expense Tracker API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A RESTful Expense Tracker API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. It provides secure user authentication using JWT and allows users to manage expenses efficiently with filtering capabilities.

---

## 🚀 Features

- 👤 User Registration
- 🔐 JWT Authentication
- 🔑 User Login
- ➕ Create Expense
- 📋 View All Expenses
- 🔍 Get Expense by ID
- ✏️ Update Expense
- ❌ Delete Expense
- 🏷️ Filter by Category
- 📅 Filter by Date Range
- 💰 Filter by Amount Range
- 🗄️ PostgreSQL Database
- ⚡ SQLAlchemy ORM
- 📖 Interactive Swagger API Documentation

---

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Uvicorn

---

# 📂 Project Structure

```text
Smart-Expense-Tracker/
│
├── app/
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── expense.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   └── expense.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── expense.py
│   │
│   ├── services/
│   │   └── expense_service.py
│   │
│   ├── utils/
│   │   └── security.py
│   │
│   └── main.py
│
├── .env
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/kalpanajangra/Smart-Expense-Tracker.git
```

Go to project folder

```bash
cd Smart-Expense-Tracker
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
uvicorn app.main:app --reload
```

Server runs on

```
http://127.0.0.1:8000
```

---

## 🐳 Docker Setup

The Smart Expense Tracker is containerized using Docker Compose with separate containers for the FastAPI application and PostgreSQL database.

### Prerequisites

* Docker Desktop
* Docker Compose

### Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/smart_expense_tracker
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=smart_expense_tracker
```

The `.env` file is excluded from Git using `.gitignore`.

### Run the Project

Build the Docker image and start the application:

```bash
docker compose up -d --build
```

Check the running containers:

```bash
docker compose ps
```

The expected containers are:

```text
smart-expense-api
smart-expense-db
```

Open Swagger UI:

```text
http://localhost:8000/docs
```

### Verify PostgreSQL

Connect to the PostgreSQL container:

```bash
docker compose exec db psql -U postgres -d smart_expense_tracker
```

Check the database tables:

```sql
\dt
```

Exit PostgreSQL:

```sql
\q
```

### View Logs

Check FastAPI logs:

```bash
docker compose logs web
```

Check PostgreSQL logs:

```bash
docker compose logs db
```

### Stop and Restart

Stop the containers:

```bash
docker compose down
```

Restart the application:

```bash
docker compose up -d
```

If application code or dependencies change, rebuild:

```bash
docker compose up -d --build
```

### Production Docker Image

Build the production Docker image:

```bash
docker build -t smart-expense-tracker:latest .
```

Verify the image:

```bash
docker images
```

### Docker Architecture

```text
                    Smart Expense Tracker
                            │
                     Docker Compose
                            │
              ┌─────────────┴─────────────┐
              │                           │
       FastAPI Container           PostgreSQL Container
       smart-expense-api           smart-expense-db
              │                           │
          Port 8000                    Port 5432
              │                           │
       REST API / Swagger          Application Database
```

# 📖 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔗 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register User |
| POST | /login | Login User |

---

## Expenses

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /expenses | Create Expense |
| GET | /expenses | Get All Expenses |
| GET | /expenses/{id} | Get Expense by ID |
| PUT | /expenses/{id} | Update Expense |
| DELETE | /expenses/{id} | Delete Expense |

---

## Filters

| Method | Endpoint |
|---------|----------|
| GET | /expenses?category=Food |
| GET | /expenses?start_date=2026-01-01&end_date=2026-01-31 |
| GET | /expenses?min_amount=100&max_amount=1000 |

---

# 🧪 Testing

Test all endpoints using Swagger UI.

- Register
- Login
- Create Expense
- View Expenses
- Update Expense
- Delete Expense
- Category Filter
- Date Filter
- Amount Filter

---

# 🔒 Authentication

This project uses **JWT Bearer Authentication**.

After login:

- Copy the generated access token.
- Click **Authorize** in Swagger.
- Enter:

```
Bearer YOUR_ACCESS_TOKEN
```

---

# 📈 Future Improvements

- User-specific expenses
- Monthly expense reports
- Expense charts
- Export to Excel
- Export to PDF
- Email notifications
- Unit testing

---

# 👩‍💻 Author

**Kalpana**

GitHub: https://github.com/kalpanajangra

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

