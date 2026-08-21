from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.expense import Expense
from app.models.user import User

from fastapi import HTTPException


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


def get_dashboard_summary(
    db: Session,
    current_user: str
):

    user_id = get_user_id(db, current_user)

    total_expenses = (
        db.query(func.count(Expense.id))
        .filter(Expense.user_id == user_id)
        .scalar()
    )

    total_amount = (
        db.query(func.sum(Expense.amount))
        .filter(Expense.user_id == user_id)
        .scalar()
        or 0
    )

    average_expense = (
        db.query(func.avg(Expense.amount))
        .filter(Expense.user_id == user_id)
        .scalar()
        or 0
    )

    highest_expense = (
        db.query(func.max(Expense.amount))
        .filter(Expense.user_id == user_id)
        .scalar()
        or 0
    )

    lowest_expense = (
        db.query(func.min(Expense.amount))
        .filter(Expense.user_id == user_id)
        .scalar()
        or 0
    )

    return {
        "total_expenses": total_expenses,
        "total_amount": total_amount,
        "average_expense": average_expense,
        "highest_expense": highest_expense,
        "lowest_expense": lowest_expense
    }


def get_category_summary(
    db: Session,
    current_user: str
):

    user_id = get_user_id(db, current_user)

    result = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total")
        )
        .filter(Expense.user_id == user_id)
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


def get_monthly_summary(
    db: Session,
    current_user: str
):

    user_id = get_user_id(db, current_user)

    result = (
        db.query(
            func.extract(
                "year",
                Expense.date
            ).label("year"),

            func.extract(
                "month",
                Expense.date
            ).label("month"),

            func.sum(
                Expense.amount
            ).label("total")
        )
        .filter(Expense.user_id == user_id)
        .group_by(
            func.extract("year", Expense.date),
            func.extract("month", Expense.date)
        )
        .order_by(
            func.extract("year", Expense.date),
            func.extract("month", Expense.date)
        )
        .all()
    )

    return [
        {
            "year": int(row.year),
            "month": int(row.month),
            "total": row.total
        }
        for row in result
    ]


def get_top_categories(
    db: Session,
    current_user: str
):

    user_id = get_user_id(db, current_user)

    result = (
        db.query(
            Expense.category,
            func.sum(
                Expense.amount
            ).label("total")
        )
        .filter(Expense.user_id == user_id)
        .group_by(Expense.category)
        .order_by(
            func.sum(
                Expense.amount
            ).desc()
        )
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
