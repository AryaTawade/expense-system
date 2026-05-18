from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import engine, get_db
from models import expense as expense_models
from app import schemas, crud
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

expense_models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Expense Intelligence System")

# This allows the HTML file to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Expense Intelligence API is running!"}


@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post("/expenses", response_model=schemas.ExpenseOut)
def add_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@app.get("/expenses", response_model=list[schemas.ExpenseOut])
def list_expenses(user_id: int, db: Session = Depends(get_db)):
    return crud.get_expenses(db, user_id)


@app.get("/analytics")
def analytics(user_id: int, db: Session = Depends(get_db)):
    return crud.get_analytics(db, user_id)


from ml.predictor import predict_category

@app.post("/predict")
def predict(description: str, amount: float):
    return predict_category(description, amount)

@app.get("/app")
def serve_ui():
    return FileResponse("index.html")