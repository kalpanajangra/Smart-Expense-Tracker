from pydantic import BaseModel, Field, field_validator
from datetime import date

ALLOWED_CATEGORIES = [
    "Food",
    "Travel",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Other"
]

class ExpenseCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=2,
        max_length=100
    )
    amount: float = Field(
        ...,
        gt=0
    )
    category: str
    date: date
    @field_validator("category")
    @classmethod
    def validate_category(cls, value):

        if value not in ALLOWED_CATEGORIES:
            raise ValueError(
                f"Category must be one of {ALLOWED_CATEGORIES}"
            )

        return value

    @field_validator("date")
    @classmethod
    def validate_date(cls, value):

        if value > date.today():
            raise ValueError(
                "Future dates are not allowed."
            )

        return value
class ExpenseResponse(BaseModel):

    id: int
    title: str
    amount: float
    category: str
    date: date

    class Config:
        from_attributes = True
from pydantic import BaseModel

class ExpenseAPIResponse(BaseModel):
    success: bool
    message: str
    data: ExpenseResponse

    class Config:
        from_attributes = True