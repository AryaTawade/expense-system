from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class User(Base):
    __tablename__ = "users"          

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)
    email    = Column(String, unique=True, nullable=False)

   
    expenses = relationship("Expense", back_populates="owner")


class Expense(Base):
    __tablename__ = "expenses"       

    id          = Column(Integer, primary_key=True, index=True)
    amount      = Column(Float, nullable=False)           
    date        = Column(Date, default=datetime.date.today)
    category    = Column(String, nullable=True)           
    description = Column(String, nullable=True)           
    user_id     = Column(Integer, ForeignKey("users.id")) 

   
    owner = relationship("User", back_populates="expenses")