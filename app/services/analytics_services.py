from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.expense import Expense

def get_dashboard_summary(db: Session):

    total_expenses = db.query(func.count(Expense.id)).scalar()

    total_amount = db.query(func.sum(Expense.amount)).scalar() or 0

    average_expense = db.query(func.avg(Expense.amount)).scalar() or 0

    highest_expense = db.query(func.max(Expense.amount)).scalar() or 0

    lowest_expense = db.query(func.min(Expense.amount)).scalar() or 0

    return {
        "total_expenses": total_expenses,
        "total_amount": total_amount,
        "average_expense": average_expense,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense
    }

def get_category_summary(db: Session):

    result = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total")
        )
        .group_by(Expense.category)
        .all()
    )

    return [
        {
            "category": row.category,
            "total": row.total
        }
        for row in result
    ]

def get_monthly_summary(db: Session):

    result = (
        db.query(
            func.extract("month", Expense.date).label("month"),
            func.sum(Expense.amount).label("total")
        )
        .group_by(func.extract("month", Expense.date))
        .all()
    )

    return [
        {
            "month": int(row.month),
            "total": row.total
        }
        for row in result
    ]

def get_top_categories(db: Session):

    result = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total")
        )
        .group_by(Expense.category)
        .order_by(func.sum(Expense.amount).desc())
        .limit(5)
        .all()
    )

    return [
        {
            "category": row.category,
            "total": row.total
        }
        for row in result
    ]

