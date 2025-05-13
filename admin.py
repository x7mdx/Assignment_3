from user import User

class Admin(User):
    """
    Represents an admin user who can view ticket sales and modify discounts.
    Inherits from the User class.
    """
    def __init__(self, user_id, name, email, password):
        """
        Create a new admin user.

        Parameters:
        - user_id: Unique ID of the user.
        - name: Name of the admin.
        - email: Email address of the admin.
        - password: Password for the admin account.
        """
        super().__init__(user_id, name, email, password)

    def view_sales(self, ticket_sales):
        """
        Display the number of tickets sold on each date.

        Parameters:
        - ticket_sales: A dictionary with dates as keys and number of tickets sold as values.
        """
        for date, count in ticket_sales.items():
            print(f"{date}: {count} tickets sold")

    def modify_discount(self, discount, new_percentage):
        """
        Update the percentage of a discount if it's still valid.

        Parameters:
        - discount: The discount object to be updated.
        - new_percentage: The new discount percentage to set.
        """
        if discount.is_valid():
            discount.percentage = new_percentage
            print(f"Discount updated to {new_percentage}%")
        else:
            print("Discount is not valid anymore.")
