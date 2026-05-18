import joblib, os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
import csv

MODEL_PATH = "ml/expense_model.pkl"
ENCODER_PATH = "ml/label_encoder.pkl"

def load_training_data():
    descriptions, amounts, categories = [], [], []
    with open("ml/training_data.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            descriptions.append(row["description"].lower())
            amounts.append(float(row["amount"]))
            categories.append(row["category"])
    return descriptions, amounts, categories

def train_model():
    print("Training model...")
    descriptions, amounts, categories = load_training_data()

   
    features = [f"{d} {a:.2f}" for d, a in zip(descriptions, amounts)]

    le = LabelEncoder()
    y = le.fit_transform(categories)

   
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2))),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    pipeline.fit(features, y)

    joblib.dump(pipeline, MODEL_PATH)
    joblib.dump(le, ENCODER_PATH)
    print(f"Model saved. Categories learned: {list(le.classes_)}")
    return pipeline, le

def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(ENCODER_PATH):
        return joblib.load(MODEL_PATH), joblib.load(ENCODER_PATH)
    return train_model()

def predict_category(description: str, amount: float):
    pipeline, le = load_model()
    feature = f"{description.lower()} {amount:.2f}"
    pred_index = pipeline.predict([feature])[0]
    probabilities = pipeline.predict_proba([feature])[0]
    confidence = round(float(max(probabilities)) * 100, 1)
    category = le.inverse_transform([pred_index])[0]
    return {"predicted_category": category, "confidence_percent": confidence}

if __name__ == "__main__":
    train_model()
    # Quick test
    tests = [
        ("Netflix monthly", 12.99),
        ("Tesco shopping", 65.00),
        ("Uber ride home", 14.50),
        ("Electric bill", 95.00),
    ]
    print("\nTest predictions:")
    for desc, amt in tests:
        result = predict_category(desc, amt)
        print(f"  '{desc}' £{amt} → {result['predicted_category']} ({result['confidence_percent']}% confident)")