from datetime import datetime

class Discount:
    """
    Represents a discount that can be applied to a price.
    """

    def __init__(self, discount_id, description, percentage, valid_until):
        """
        Create a new discount.

        Parameters:
        - discount_id: Unique ID for the discount.
        - description: A short description of the discount.
        - percentage: The discount percentage (e.g., 10 for 10% off).
        - valid_until: The date until the discount is valid (as a 'YYYY-MM-DD' string or a date object).
        """
        self.discount_id = discount_id
        self.description = description
        self.percentage = percentage 
        if isinstance(valid_until, str):
            self.valid_until = datetime.strptime(valid_until, "%Y-%m-%d").date()
        else:
            self.valid_until = valid_until

    def is_valid(self, current_date):
        """
        Check if the discount is still valid on the given date.

        Parameters:
        - current_date: The date to check (as a date object).

        Returns:
        - True if the discount is valid, False otherwise.
        """
        print(type(current_date), (self.valid_until))
        return current_date <= self.valid_until

    def apply_discount(self, price):
        """
        Apply the discount to the given price.

        Parameters:
        - price: The original price before discount.

        Returns:
        - The price after the discount is applied.
        """
        return price - (price * self.percentage / 100)
