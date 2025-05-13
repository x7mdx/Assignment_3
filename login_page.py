import tkinter as tk
from tkinter import messagebox
import pickle
from customer_dashboard import CustomerDashboard
from customer import Customer
from admin import Admin

USER_DATA_FILE = "users.pkl"

ADMIN_CREDENTIALS = {
    "user_id": -1,
    "email": "admin@raceTicket.sys",
    "password": "UAE@123@",
    "role": "admin"
}

def load_users():
    try:
        with open(USER_DATA_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_DATA_FILE, "wb") as f:
        pickle.dump(users, f)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.users = load_users()
        self.configure(bg="#f5f5f5")

        login_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove")
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        login_frame.configure(padx=30, pady=30)

        tk.Label(login_frame, text="Login", font=("Arial", 18, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=20)
        tk.Label(login_frame, text="Email:", bg="#ffffff").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.email_entry = tk.Entry(login_frame, width=25)
        self.email_entry.grid(row=1, column=1, pady=10)

        tk.Label(login_frame, text="Password:", bg="#ffffff").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.password_entry = tk.Entry(login_frame, show="*", width=25)
        self.password_entry.grid(row=2, column=1, pady=10)

        tk.Button(login_frame, text="Login", command=self.login_user).grid(row=5, column=0, columnspan=2, pady=15)
        tk.Button(login_frame, text="Create Account", command=lambda: controller.show_frame("LoginPage", "RegisterPage")).grid(row=6, column=0, columnspan=2)

    def login_user(self):
        self.users = load_users()

        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if email == ADMIN_CREDENTIALS["email"] and password == ADMIN_CREDENTIALS["password"]:
            self.controller.current_user = Admin(-1, "Admin", email, password)
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            self.controller.show_frame("LoginPage", "AdminDashboard")
            return

       
        user = self.users.get(email)
        if user and user["password"] == password:
            self.controller.current_user = Customer(user["user_id"], user["name"], email, password)
            self.controller.frames["CustomerDashboard"] = CustomerDashboard(parent=self.controller, controller=self.controller)

            messagebox.showinfo("Login Successful", f"Welcome back, {email}!")
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.controller.show_frame("LoginPage", "CustomerDashboard")
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        reg_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove")
        reg_frame.place(relx=0.5, rely=0.5, anchor="center")
        reg_frame.configure(padx=30, pady=25)

        tk.Label(reg_frame, text="Create Account", font=("Arial", 16, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=20)

        tk.Label(reg_frame, text="Name:", bg="#ffffff").grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.name_entry = tk.Entry(reg_frame, width=25)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(reg_frame, text="Email:", bg="#ffffff").grid(row=2, column=0, sticky="e", padx=10, pady=5)
        self.email_entry = tk.Entry(reg_frame, width=25)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(reg_frame, text="Password:", bg="#ffffff").grid(row=3, column=0, sticky="e", padx=10, pady=5)
        self.password_entry = tk.Entry(reg_frame, show="*", width=25)
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(reg_frame, text="Register", command=self.register_user).grid(row=6, column=0, columnspan=2, pady=15)
        tk.Button(reg_frame, text="Back to Login", command=lambda: controller.show_frame("RegisterPage", "LoginPage")).grid(row=7, column=0, columnspan=2)

    def register_user(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not name or not email or not password:
            messagebox.showerror("Error", "All fields are required")
            return

        users = load_users()
        if email in users:
            messagebox.showerror("Error", "User already exists")
            return

        user_id = len(users) + 1
        users[email] = {"name": name, "password": password, "user_id": user_id}
        save_users(users)
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Account created successfully!")
        self.controller.show_frame("RegisterPage", "LoginPage")
