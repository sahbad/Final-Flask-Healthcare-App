from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from config import MONGO_URI

app = Flask(__name__)

# MongoDB client setup
client = MongoClient(MONGO_URI)
db = client["healthcare_survey"]
collection = db["responses"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    # Basic demographic fields
    age = int(request.form.get("age"))
    gender = request.form.get("gender")
    total_income = float(request.form.get("total_income"))

    # Helper function to extract checkbox + amount
    def get_expense(field_checked, field_amount):
        checked = request.form.get(field_checked) == "yes"
        amount_str = request.form.get(field_amount)
        amount = float(amount_str) if amount_str else 0.0
        return checked, amount

    utilities_checked, utilities_amount = get_expense("utilities_checked", "utilities_amount")
    entertainment_checked, entertainment_amount = get_expense("entertainment_checked", "entertainment_amount")
    school_fees_checked, school_fees_amount = get_expense("school_fees_checked", "school_fees_amount")
    shopping_checked, shopping_amount = get_expense("shopping_checked", "shopping_amount")
    healthcare_checked, healthcare_amount = get_expense("healthcare_checked", "healthcare_amount")

    # Document structure saved to MongoDB
    doc = {
        "age": age,
        "gender": gender,
        "total_income": total_income,
        "utilities": {"selected": utilities_checked, "amount": utilities_amount},
        "entertainment": {"selected": entertainment_checked, "amount": entertainment_amount},
        "school_fees": {"selected": school_fees_checked, "amount": school_fees_amount},
        "shopping": {"selected": shopping_checked, "amount": shopping_amount},
        "healthcare": {"selected": healthcare_checked, "amount": healthcare_amount},
    }

    collection.insert_one(doc)

    return redirect(url_for("success"))


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)