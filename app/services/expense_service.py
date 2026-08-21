from datetime import date
from typing import Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.expense import Expense
from app.models.user import User
from app.schemas.expense import ExpenseCreate

def get_user_id(db: Session, current_user: str):

    user = (
        db.query(User)
        .filter(User.email == current_user)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user.id


# Create
def create_expense(db: Session, expense: ExpenseCreate,current_user: str):
    user_id = get_user_id(db, current_user)
    new_expense = Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
        user_id=user_id
    )
    try:
        db.add(new_expense)
        db.commit()
        db.refresh(new_expense)

        return {
            "success": True,
            "message": "Expense Created",
            "data": new_expense
        }
    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

# Get All + Filters
def get_expenses(
    db: Session,
    current_user: str,
    category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
):
    user_id = get_user_id(db, current_user)
    query = db.query(Expense).filter(
        Expense.user_id == user_id
    )

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
def get_expense_by_id(db: Session, expense_id: int,current_user: str):
    user_id = get_user_id(db, current_user)

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {
    
        "success": True,
    
        "message": "Expenses Retrieved",
    
        "data": expense
    
    }


# Update
def update_expense(db: Session, expense_id: int, expense_data: ExpenseCreate, current_user:str):
    user_id = get_user_id(db, current_user)

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    try:
        expense.title = expense_data.title
        expense.amount = expense_data.amount
        expense.category = expense_data.category
        expense.date = expense_data.date

        db.commit()
        db.refresh(expense)

        return {

            "success": True,

            "message": "Expense Updated",

            "data": expense

        }
    
    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database Error"
        )

# Delete
def delete_expense(db: Session, expense_id: int, current_user: str):
    user_id = get_user_id(db, current_user)

    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    try:
    
        db.delete(expense)
        db.commit()

        return {
                "success": True,
                "message": "Expense deleted successfully"
                }

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Database Error"
        )

    