from pydantic import BaseModel
from typing import Optional
import datetime


class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        from_attributes = True


class ExpenseCreate(BaseModel):
    amount: float
    date: Optional[datetime.date] = None
    category: Optional[str] = None
    description: Optional[str] = None
    user_id: int

class ExpenseOut(BaseModel):
    id: int
    amount: float
    date: Optional[datetime.date]
    category: Optional[str]
    description: Optional[str]
    user_id: int
    class Config:
        from_attributes = True