from user import User

class Customer(User):
    """
    Represents a customer who can buy tickets and manage their profile.
    Inherits from the User class.
    """
    def __init__(self, user_id, name, email, password):
        """
        Create a new customer.

        Parameters:
        - user_id: Unique ID of the user.
        - name: Name of the customer.
        - email: Email address of the customer.
        - password: Password for the customer account.
        """
        super().__init__(user_id, name, email, password)
        self.purchase_history = []  

    def add_order(self, order_id):
        """
        Add a new order ID to the purchase history.

        Parameters:
        - order_id: The ID of the order to add.
        """
        self.purchase_history.append(order_id)

    def view_orders(self):
        """
        Show all order IDs in the purchase history.

        Returns:
        - A list of order IDs.
        """
        return self.purchase_history

    def update_profile(self, new_name=None, new_password=None):
        """
        Update the customer's name and/or password.

        Parameters:
        - new_name: New name for the customer (optional).
        - new_password: New password for the account (optional).
        """
        if new_name:
            self.name = new_name
        if new_password:
            self.password = new_password
        print("Profile updated successfully.")
