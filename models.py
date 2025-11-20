class User:
    """Represents a single survey respondent."""

    def __init__(
        self,
        age,
        gender,
        total_income,
        utilities_amount,
        entertainment_amount,
        school_fees_amount,
        shopping_amount,
        healthcare_amount,
    ):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.utilities_amount = utilities_amount
        self.entertainment_amount = entertainment_amount
        self.school_fees_amount = school_fees_amount
        self.shopping_amount = shopping_amount
        self.healthcare_amount = healthcare_amount

    def to_dict(self):
        """Return a dictionary suitable for writing to CSV or Pandas."""
        return {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
            "utilities_amount": self.utilities_amount,
            "entertainment_amount": self.entertainment_amount,
            "school_fees_amount": self.school_fees_amount,
            "shopping_amount": self.shopping_amount,
            "healthcare_amount": self.healthcare_amount,
        }