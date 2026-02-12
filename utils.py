import json
import os

FILE = "data/expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense(data, title, amount, category):
    data.append({
        "title": title,
        "amount": amount,
        "category": category
    })
    save_data(data)

def show_expenses(data):
    if not data:
        print("\nXarajatlar yo‘q\n")
        return

    total = 0
    print("\nXarajatlar:\n")
    for i, e in enumerate(data, 1):
        print(f"{i}. {e['title']} - {e['amount']}$ ({e['category']})")
        total += e["amount"]

    print(f"\nJami: {total}$\n")

def by_category(data):
    cat = {}
    for e in data:
        cat[e["category"]] = cat.get(e["category"], 0) + e["amount"]

    print("\nKategoriya bo‘yicha:")
    for k, v in cat.items():
        print(f"{k}: {v}$")
    print()
