from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.analytics_services import (
    get_dashboard_summary,
    get_category_summary,
    get_monthly_summary,
    get_top_categories
)

from app.schemas.analytics import (
    DashboardResponse,
    CategorySummary,
    MonthlySummary
)

from typing import List

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get(
    "/dashboard",
    response_model=DashboardResponse
)
def dashboard(db: Session = Depends(get_db)):
    return get_dashboard_summary(db)

@router.get(
    "/category",
    response_model=List[CategorySummary]
)
def category_summary(db: Session = Depends(get_db)):
    return get_category_summary(db)

@router.get(
    "/monthly",
    response_model=List[MonthlySummary]
)
def monthly_summary(db: Session = Depends(get_db)):
    return get_monthly_summary(db)

@router.get("/top-categories")
def top_categories(db: Session = Depends(get_db)):
    return get_top_categories(db)