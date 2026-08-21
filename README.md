# 💰 Smart Expense Tracker API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.139-green?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/Auth-JWT-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A RESTful Expense Tracker API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. It provides secure user authentication using JWT and allows users to manage expenses efficiently with filtering capabilities.

---

## 🚀 Features

- 👤 User Registration
- 🔐 JWT Bearer Authentication
- 🔑 Secure User Login
- 👨‍💻 Get Current User Profile
- ➕ Create Expense
- 📋 View All Expenses
- 🔍 Get Expense by ID
- ✏️ Update Expense
- ❌ Delete Expense
- 🏷️ Filter Expenses by Category
- 📅 Filter Expenses by Date Range
- 💰 Filter Expenses by Amount Range
- 📊 Expense Analytics Dashboard
- 📈 Category-wise Expense Analysis
- 📅 Monthly Expense Analysis
- 🏆 Top 5 Spending Categories
- 🗄️ PostgreSQL Database
- ⚡ SQLAlchemy ORM
- 🐳 Docker & Docker Compose Support
- 🌐 CORS Support
- 📖 Interactive Swagger API Documentation
- 🛡️ Centralized HTTP Exception Handling

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

# 🏗️ Application Architecture

The project follows a layered architecture:

```text
Client
  │
  ▼
FastAPI Routes
  │
  ├── Authentication Routes
  ├── Expense Routes
  └── Analytics Routes
  │
  ▼
Service Layer
  │
  ├── Expense Services
  └── Analytics Services
  │
  ▼
SQLAlchemy ORM
  │
  ▼
PostgreSQL Database
```
---

# 📂 Project Structure

```text
Smart-Expense-Tracker/
│
├── app/
│   ├── database/
│   │   ├── database.py
│   │   └── init_db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── expense.py
│   │
│   ├── routes/
│   │   ├── auth.py
│   │   ├── expense.py
│   │   └── analytics.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── expense.py
│   │   └── analytics.py
│   │
│   ├── services/
│   │   ├── auth_services.py
│   │   ├── expense_service.py
│   │   └── analytics_services.py
│   │
│   ├── utils/
│   │   └── security.py
│   │
│   ├── exceptions.py
│   └── main.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root.

```env
DATABASE_URL=postgresql://postgres:postgres@db:5432/smart_expense_tracker
SECRET_KEY=YOUR_GENERATED_SECRET_KEY
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=smart_expense_tracker
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
| POST | `/register` | Register a new user |
| POST | `/login` | Authenticate user and generate JWT access token |
| GET | `/me` | Get the currently authenticated user's profile |

---

## Expenses

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/expenses/` | Create a new expense |
| GET | `/expenses/` | Get expenses with optional filters |
| GET | `/expenses/{expense_id}` | Get an expense by ID |
| PUT | `/expenses/{expense_id}` | Update an expense |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## 🔍 Expense Filters

The `GET /expenses/` endpoint supports multiple optional filters.

| Filter | Query Parameter | Example |
|--------|-----------------|---------|
| Category | `category` | `?category=Food` |
| Start Date | `start_date` | `?start_date=2026-01-01` |
| End Date | `end_date` | `?end_date=2026-01-31` |
| Minimum Amount | `min_amount` | `?min_amount=100` |
| Maximum Amount | `max_amount` | `?max_amount=1000` |

### Example

```text
GET /expenses/?category=Food&min_amount=100&max_amount=1000
```

### 📊 Analytics

The Smart Expense Tracker provides authenticated analytics endpoints that generate insights from the user's expenses.

All analytics endpoints require JWT authentication and return data only for the currently authenticated user.

### Dashboard Summary
GET /analytics/dashboard

Returns an overall summary of the user's expenses.

Response includes:

Total number of expenses
Total amount spent
Average expense amount
Highest expense
Lowest expense
Category-wise Summary
GET /analytics/category

Returns the total amount spent for each expense category.

Example response:

[
  {
    "category": "Food",
    "total": 2500
  },
  {
    "category": "Travel",
    "total": 1800
  }
]
### Monthly Summary
GET /analytics/monthly

Returns total spending grouped by year and month.

Example response:

[
  {
    "year": 2026,
    "month": 7,
    "total": 4500
  },
  {
    "year": 2026,
    "month": 8,
    "total": 3200
  }
]
### Top Spending Categories
GET /analytics/top-categories

Returns the top 5 categories based on total spending.

The categories are ordered from highest to lowest spending.

# 📈 Analytics Capabilities

The analytics module uses SQL aggregation functions through SQLAlchemy to calculate expense insights.

### Dashboard Metrics

The dashboard calculates:

- `COUNT` → Total number of expenses
- `SUM` → Total amount spent
- `AVG` → Average expense
- `MAX` → Highest expense
- `MIN` → Lowest expense

### Category Analysis

Expenses are grouped by category and their amounts are summed to identify spending distribution.

### Monthly Analysis

Expenses are grouped by year and month to provide monthly spending trends.

### Top Categories

The system calculates total spending per category and returns the top 5 categories based on spending amount.

All analytics queries are filtered using the authenticated user's ID.

---

# 🧪 Testing

All API endpoints can be tested using the interactive Swagger UI.

## Authentication Testing

- Register a new user
- Login with valid credentials
- Test invalid login credentials
- Get current user profile
- Verify JWT authentication

## Expense Testing

- Create expense
- Get all expenses
- Get expense by ID
- Update expense
- Delete expense
- Filter by category
- Filter by date range
- Filter by amount range
- Test invalid expense requests
- Test unauthorized requests

## Analytics Testing

- Test dashboard summary
- Test category-wise summary
- Test monthly summary
- Test top spending categories
- Verify analytics return data only for the authenticated user
- Test analytics endpoints without JWT authentication

Swagger UI:

```text
http://localhost:8000/docs
```


# 🚀 Future Improvements

- 📊 Interactive expense visualization dashboard
- 📥 Export expenses to Excel
- 📄 Export expense reports to PDF
- 📧 Email notifications and spending alerts
- 🧪 Automated unit and integration tests
- 🔄 Recurring expense support
- 🎯 Monthly or category-based spending budgets
- 📱 Frontend application for easier expense management

---

# 👩‍💻 Author

**Kalpana**

GitHub: https://github.com/kalpanajangra

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

