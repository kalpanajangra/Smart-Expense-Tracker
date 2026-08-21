from fastapi import FastAPI
from app.routes.auth import router
from app.database.database import Base, engine
from app.models.user import User
from app.routes.expense import router as expense_router
from fastapi import HTTPException
from app.exceptions import http_exception_handler
from app.routes import analytics
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)
app.include_router(expense_router)
app.include_router(analytics.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API!"
    }

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

