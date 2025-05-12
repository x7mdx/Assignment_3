from user import User

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    def view_sales(self, ticket_sales):
        for date, count in ticket_sales.items():
            print(f"{date}: {count} tickets sold")

    def modify_discount(self, discount, new_percentage):
        if discount.is_valid():
            discount.percentage = new_percentage
            print(f"Discount updated to {new_percentage}%")
        else:
            print("Discount is not valid anymore.")

