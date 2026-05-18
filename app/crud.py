from sqlalchemy.orm import Session
from sqlalchemy import func
from models.expense import User, Expense
from app.schemas import UserCreate, ExpenseCreate
import datetime


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()


def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(
        amount=expense.amount,
        date=expense.date or datetime.date.today(),
        category=expense.category,
        description=expense.description,
        user_id=expense.user_id
    )
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, user_id: int):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

def get_all_expenses(db: Session):
    return db.query(Expense).all()


def get_analytics(db: Session, user_id: int):
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()

    if not expenses:
        return {"message": "No expenses found for this user"}

    total_spent = sum(e.amount for e in expenses)
    avg_per_expense = total_spent / len(expenses)

   
    by_category = {}
    for e in expenses:
        cat = e.category or "Uncategorised"
        by_category[cat] = by_category.get(cat, 0) + e.amount


    by_month = {}
    for e in expenses:
        month = e.date.strftime("%Y-%m") if e.date else "unknown"
        by_month[month] = by_month.get(month, 0) + e.amount

    return {
        "total_spent": round(total_spent, 2),
        "total_transactions": len(expenses),
        "average_per_expense": round(avg_per_expense, 2),
        "spending_by_category": by_category,
        "spending_by_month": by_month,
        "top_category": max(by_category, key=by_category.get)
    }