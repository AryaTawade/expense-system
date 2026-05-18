# Smart Expense Intelligence System

A finance platform that stores expenses, analyzes spending patterns, and predicts expense categories using Machine Learning.

## Live Demo

- UI → https://expense-system-4q3u.onrender.com/app
- API → https://expense-system-4q3u.onrender.com/docs

## Tech Stack

- **Backend** — Python, FastAPI
- **Database** — SQLite, SQLAlchemy
- **Machine Learning** — Scikit-learn (Random Forest)
- **Container** — Docker
- **Frontend** — HTML, JavaScript

## Features

- Add and store expenses with amount, date and description
- ML model automatically predicts expense category
- Analytics dashboard — spending by category and month
- REST API with 7 endpoints
- Web dashboard UI

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users` | Create a user |
| POST | `/expenses` | Add an expense |
| GET | `/expenses` | List expenses |
| GET | `/analytics` | Spending breakdown |
| POST | `/predict` | ML category prediction |

## ML Model

Predicts one of 8 categories — Groceries, Entertainment, Transport, Utilities, Health, Shopping, Dining, Housing — using a Random Forest classifier trained on 335 examples.

## Setup

```bash
git clone https://github.com/AryaTawade/expense-intelligence-system.git
cd expense-intelligence-system
pip install -r requirements.txt
python ml/training_data.py
python ml/predictor.py
uvicorn app.main:app --reload --port 8080
```

