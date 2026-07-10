from app.database.database import Base, engine
from app.models.expense import Expense

Base.metadata.create_all(bind=engine)