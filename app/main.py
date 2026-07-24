from fastapi import FastAPI
from app.routes.auth import router
from app.database.database import Base, engine
from app.models.user import User
from app.routes.expense import router as expense_router
from fastapi import HTTPException
from app.exceptions import http_exception_handler

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)
app.include_router(router)
app.include_router(expense_router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API!"
    }

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)
