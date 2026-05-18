import csv
import os
import random

random.seed(42)

def make_rows(target=350):
    rows = []

    templates = {
        "Groceries": [
            "Tesco shop", "Sainsbury's groceries", "Aldi weekly shop",
            "Lidl food run", "Waitrose produce", "Morrisons grocery trip",
            "Co-op essentials", "Asda delivery", "Marks Spencer food"
        ],
        "Entertainment": [
            "Netflix subscription", "Spotify premium", "Disney Plus",
            "YouTube Premium", "Steam game", "Cinema tickets",
            "Xbox Game Pass", "Audible subscription", "Apple Music"
        ],
        "Transport": [
            "Uber ride", "Bus pass", "Train ticket", "Taxi trip",
            "Petrol fill up", "Oyster top up", "Zipcar rental",
            "National Rail ticket", "Parking fee"
        ],
        "Utilities": [
            "Electric bill", "Gas bill", "Water bill",
            "Broadband internet", "Mobile phone bill",
            "Council tax", "EDF energy", "Virgin broadband"
        ],
        "Health": [
            "Gym membership", "Pharmacy purchase", "Dentist visit",
            "Optician eye test", "Yoga class", "GP appointment",
            "NHS prescription", "Vitamins purchase"
        ],
        "Shopping": [
            "Amazon order", "Zara clothing", "H&M clothes",
            "ASOS order", "Ikea furniture", "Boots toiletries",
            "John Lewis purchase", "Next clothing"
        ],
        "Dining": [
            "Restaurant meal", "McDonalds", "Pret lunch",
            "Starbucks coffee", "Nandos dinner", "Pizza Express",
            "Deliveroo order", "Greggs bakery", "Costa Coffee"
        ],
        "Housing": [
            "Rent payment", "Mortgage payment", "Home insurance",
            "Letting fee", "Boiler service", "Deposit payment",
            "Estate agent fee"
        ]
    }

    amounts = {
        "Groceries": (5, 120),
        "Entertainment": (5, 40),
        "Transport": (5, 80),
        "Utilities": (20, 200),
        "Health": (5, 120),
        "Shopping": (10, 200),
        "Dining": (3, 60),
        "Housing": (100, 1500),
    }

    categories = list(templates.keys())

    while len(rows) < target:
        cat = random.choice(categories)
        desc = random.choice(templates[cat])

        suffixes = ["", " - online", " - UK", " monthly", " charge", " payment"]
        desc = desc + random.choice(suffixes)

        amount = round(random.uniform(*amounts[cat]), 2)

        rows.append((desc, amount, cat))

    return rows


data = make_rows(350)

os.makedirs("ml", exist_ok=True)
with open("ml/training_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["description", "amount", "category"])
    writer.writerows(data)

print(f"Created training_data.csv with {len(data)} rows")