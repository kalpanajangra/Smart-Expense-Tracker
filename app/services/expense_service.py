from datetime import date
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate


# Create
def create_expense(db: Session, expense: ExpenseCreate):
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


# Get All + Filters
def get_expenses(
    db: Session,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
):
    query = db.query(Expense)

    if category:
        query = query.filter(Expense.category == category)

    if start_date:
        query = query.filter(Expense.date >= start_date)

    if end_date:
        query = query.filter(Expense.date <= end_date)

    if min_amount:
        query = query.filter(Expense.amount >= min_amount)

    if max_amount:
        query = query.filter(Expense.amount <= max_amount)

    return query.all()


# Get By ID
def get_expense_by_id(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return expense


# Update
def update_expense(db: Session, expense_id: int, expense_data: ExpenseCreate):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    expense.title = expense_data.title
    expense.amount = expense_data.amount
    expense.category = expense_data.category

    db.commit()
    db.refresh(expense)

    return expense


# Delete
def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id).first()

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}