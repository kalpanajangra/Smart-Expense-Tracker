from typing import List,Optional
from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate, ExpenseResponse,ExpenseAPIResponse

from app.utils.security import get_current_user

from app.services.expense_service import (
    create_expense as create_expense_service,
    get_expenses as get_expenses_service,
    get_expense_by_id,
    update_expense,
    delete_expense,
)

router = APIRouter(prefix="/expenses", tags=["Expenses"])

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST API
@router.post("/",status_code=201, response_model=ExpenseAPIResponse)
def create_expense(expense: ExpenseCreate,
            current_user=Depends(get_current_user), 
            db: Session = Depends(get_db)
            ):
        return create_expense_service(db, expense)


# GET API
@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(category: Optional[str] = None,
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    current_user=Depends(get_current_user),

    db: Session = Depends(get_db)
    ):

    return get_expenses_service(
        db=db,
        category=category,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
    )

#GET by id
@router.get("/{expense_id}", response_model=ExpenseAPIResponse)
def read_expense(
    expense_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_expense_by_id(db, expense_id)


#Update
@router.put("/{expense_id}", response_model=ExpenseAPIResponse)
def edit_expense(
    expense_id: int,
    expense: ExpenseCreate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return update_expense(db, expense_id, expense)

#Delete
@router.delete("/{expense_id}",status_code=200)
def remove_expense(
    expense_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return delete_expense(db, expense_id)