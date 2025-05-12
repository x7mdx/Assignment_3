class Discount:
    def __init__(self, discount_id, description, percentage, valid_until):
        self.discount_id = discount_id
        self.description = description
        self.percentage = percentage 
        self.valid_until = valid_until 

    def is_valid(self, current_date):
        return current_date <= self.valid_until

    def apply_discount(self, price):
        return price - (price * self.percentage / 100)
