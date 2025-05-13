class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password

    def login(self, input_email, input_password):
        return self.email == input_email and self.password == input_password

    def logout(self):
        print(f"{self.name} has logged out.")
