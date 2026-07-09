from fastapi import FastAPI
from app.routes.auth import router
from app.database.database import Base, engine
from app.models.user import User

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)
app.include_router(router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API!"
    }