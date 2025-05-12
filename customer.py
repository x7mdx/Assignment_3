from user import User
class Customer(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.purchase_history = []  

    def add_order(self, order_id):
        self.purchase_history.append(order_id)

    def view_orders(self):
        return self.purchase_history

    def update_profile(self, new_name=None, new_email=None):
        if new_name:
            self.name = new_name
        if new_email:
            self.email = new_email
        print("Profile updated successfully.")
