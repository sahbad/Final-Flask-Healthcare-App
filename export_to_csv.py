import csv
import os
from pymongo import MongoClient
from config import MONGO_URI
from models import User

client = MongoClient(MONGO_URI)
db = client["healthcare_survey"]
collection = db["responses"]

OUTPUT_DIR = "data"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "user_spending.csv")


def export_data_to_csv():
    docs = list(collection.find())

    fieldnames = [
        "age",
        "gender",
        "total_income",
        "utilities_amount",
        "entertainment_amount",
        "school_fees_amount",
        "shopping_amount",
        "healthcare_amount",
    ]

    with open(OUTPUT_FILE, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for doc in docs:
            user = User(
                age=doc.get("age"),
                gender=doc.get("gender"),
                total_income=doc.get("total_income"),
                utilities_amount=doc.get("utilities", {}).get("amount", 0),
                entertainment_amount=doc.get("entertainment", {}).get("amount", 0),
                school_fees_amount=doc.get("school_fees", {}).get("amount", 0),
                shopping_amount=doc.get("shopping", {}).get("amount", 0),
                healthcare_amount=doc.get("healthcare", {}).get("amount", 0),
            )
            writer.writerow(user.to_dict())

    print(f"Exported {len(docs)} records to {OUTPUT_FILE}")


if __name__ == "__main__":
    export_data_to_csv()