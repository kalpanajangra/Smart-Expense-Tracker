from fastapi import FastAPI

app = FastAPI(
    title="Smart Expense Tracker API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Expense Tracker API!"
    }