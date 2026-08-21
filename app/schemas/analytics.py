from pydantic import BaseModel


class DashboardResponse(BaseModel):
    total_expenses: int
    total_amount: float
    average_expense: float
    highest_expense: float
    lowest_expense: float


class CategorySummary(BaseModel):
    category: str
    total: float


class MonthlySummary(BaseModel):
    year: int
    month: int
    total: float