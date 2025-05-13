import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import date

USER_DATA_FILE = "users.pkl"

def load_users():
    try:
        with open(USER_DATA_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return {}

def save_users(users):
    with open(USER_DATA_FILE, "wb") as f:
        pickle.dump(users, f)

ORDER_DATA_FILE = "orders.pkl"

def load_orders():
    try:
        with open(ORDER_DATA_FILE, "rb") as f:
            return pickle.load(f)
    except:
        return []

def save_orders(orders):
    with open(ORDER_DATA_FILE, "wb") as f:
        pickle.dump(orders, f)

def get_ticket_options():
    return {
        "Single Race Pass": {"price": 100, "validity": "1 Day", "features": "Access to 1 race"},
        "Weekend Package": {"price": 250, "validity": "2 Days", "features": "Access to all weekend races"},
        "Group Discount": {"price": 400, "validity": "1 Day", "features": "Entry for 5 people"}
    }

class CustomerDashboard(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

       
        user_email = controller.current_user.email
        welcome_message = f"Welcome, {user_email.split('@')[0]}!"

       
        dashboard_frame = tk.Frame(self, bg="#ffffff", bd=2, relief="groove")
        dashboard_frame.place(relx=0.5, rely=0.5, anchor="center")
        dashboard_frame.configure(padx=50, pady=50)

       
        tk.Label(dashboard_frame, text=welcome_message, font=("Arial", 18, "bold"), bg="#ffffff").grid(row=0, column=0, columnspan=2, pady=20)

       
        tk.Button(dashboard_frame, text="View/Edit Profile", command=self.view_profile).grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")
        tk.Button(dashboard_frame, text="Purchase Tickets", command=self.purchase_tickets).grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
        tk.Button(dashboard_frame, text="View Orders", command=self.view_orders).grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
        tk.Button(dashboard_frame, text="Logout", command=self.logout).grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

    def view_profile(self):
       
        user_email = self.controller.current_user.email
        users = load_users()
        profile_window = tk.Toplevel(self)
        profile_window.title("Profile")
        profile_window.geometry("400x300")

        tk.Label(profile_window, text="Edit Profile", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(profile_window, text="Name:").pack()
        name_entry = tk.Entry(profile_window, width=30)
        name_entry.insert(0,  self.controller.current_user.name)
        name_entry.pack(pady=5)

        tk.Label(profile_window, text="Email:").pack()
        email_entry = tk.Entry(profile_window, width=30)
        email_entry.insert(0, self.controller.current_user.email)
        email_entry.config(state="disabled")
        email_entry.pack(pady=5)

        tk.Label(profile_window, text="Password:").pack()
        password_entry = tk.Entry(profile_window, show="*", width=30)
        password_entry.insert(0, self.controller.current_user.password)
        password_entry.pack(pady=5)

        def save_profile():
            print(users[user_email])
            users[user_email] = {"name": name_entry.get(), "password": password_entry.get(), "user_id": users[user_email]["user_id"]}
            self.controller.current_user.update_profile(new_name=name_entry.get(), new_password=password_entry.get()) 
            save_users(users)
            messagebox.showinfo("Profile Updated", "Your profile has been updated successfully!")
            profile_window.destroy()

        tk.Button(profile_window, text="Save Changes", command=save_profile).pack(pady=10)
    def purchase_tickets(self):
        ticket_window = tk.Toplevel(self)
        ticket_window.title("Purchase Tickets")
        ticket_window.geometry("420x500")

        ticket_options = get_ticket_options()
        ticket_types = list(ticket_options.keys())

        tk.Label(ticket_window, text="Select Ticket Type:", font=("Arial", 12, "bold")).pack(pady=10)
        ticket_var = tk.StringVar(value=ticket_types[0])
        tk.OptionMenu(ticket_window, ticket_var, *ticket_types).pack(pady=5)

        ticket_details = tk.Label(ticket_window, text="", wraplength=380, justify="left")
        ticket_details.pack(pady=5)

        def update_ticket_details(*args):
            selected = ticket_var.get()
            details = ticket_options[selected]
            ticket_details.config(
                text=f"Price: AED {details['price']}\n"
                    f"Validity: {details['validity']}\n"
                    f"Features: {details['features']}"
            )

        ticket_var.trace("w", update_ticket_details)
        update_ticket_details()

        tk.Label(ticket_window, text="Enter number of tickets:").pack(pady=10)
        num_entry = tk.Entry(ticket_window)
        num_entry.pack()

        tk.Label(ticket_window, text="Payment Method (Credit/Debit):").pack(pady=10)
        payment_entry = tk.Entry(ticket_window)
        payment_entry.pack()

        tk.Label(ticket_window, text="Enter Discount Code (if any):").pack(pady=10)
        discount_entry = tk.Entry(ticket_window)
        discount_entry.pack()

        def load_discounts():
            try:
                with open("discounts.pkl", "rb") as f:
                    return pickle.load(f)
            except (FileNotFoundError, EOFError):
                return []

        def confirm_purchase():
            selected_type = ticket_var.get()
            ticket_count = num_entry.get()
            payment_method = payment_entry.get()
            discount_code = discount_entry.get().strip().upper()

            if not ticket_count.isdigit() or int(ticket_count) <= 0:
                messagebox.showerror("Error", "Enter a valid ticket quantity.")
                ticket_window.focus_force()
                return
            if not payment_method.strip():
                messagebox.showerror("Error", "Please enter a payment method.")
                ticket_window.focus_force()
                return

            ticket_info = ticket_options[selected_type]
            quantity = int(ticket_count)
            base_price = quantity * ticket_info["price"]
            applied_discount = None
            final_price = base_price

            if discount_code:
                today = date.today()
                for d in load_discounts():
                    if d.discount_id == discount_code and d.is_valid(today):
                        final_price = d.apply_discount(base_price)
                        applied_discount = {
                            "code": d.discount_id,
                            "description": d.description,
                            "percentage": d.percentage
                        }
                        break
                else:
                    messagebox.showwarning("Discount", "Invalid or expired discount code. No discount applied.")
                    return

            customer = self.controller.current_user

            order = {
                "user_id": customer.user_id,
                "user_email": customer.email,
                "ticket_type": selected_type,
                "quantity": quantity,
                "total_price": final_price,
                "payment_method": payment_method,
                "discount": applied_discount 
            }

            orders = load_orders()
            orders.append(order)
            save_orders(orders)

            customer.add_order(order)

            if applied_discount:
                discount_msg = f"Discount Applied: {applied_discount['description']} ({applied_discount['percentage']}%)"
            else:
                discount_msg = "No discount applied."

            messagebox.showinfo("Success",
                f"Purchased {quantity}x {selected_type} tickets!\n"
                f"Total: AED {final_price:.2f}\n{discount_msg}"
            )
            ticket_window.destroy()

        tk.Button(ticket_window, text="Confirm Purchase", command=confirm_purchase).pack(pady=20)

    def view_orders(self):
        orders_window = tk.Toplevel(self)
        orders_window.title("Your Orders")
        orders_window.geometry("450x400")

        customer = self.controller.current_user
        all_orders = load_orders()
        user_orders = [o for o in all_orders if o["user_email"] == customer.email]

        if not user_orders:
            tk.Label(orders_window, text="No orders found.", font=("Arial", 12)).pack(pady=20)
            return

        canvas = tk.Canvas(orders_window)
        scrollbar = tk.Scrollbar(orders_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        for idx, order in enumerate(user_orders):
            frame = tk.LabelFrame(scrollable_frame, text=f"Order {idx+1}", padx=10, pady=5)
            frame.pack(padx=10, pady=8, fill="x")

            tk.Label(frame, text=f"Ticket Type: {order['ticket_type']}").pack(anchor="w")
            tk.Label(frame, text=f"Quantity: {order['quantity']}").pack(anchor="w")
            tk.Label(frame, text=f"Total Price: AED {order['total_price']}").pack(anchor="w")
            tk.Label(frame, text=f"Payment Method: {order['payment_method']}").pack(anchor="w")

            def modify_order(index=idx):
                modify_win = tk.Toplevel(orders_window)
                modify_win.title("Modify Order")
                modify_win.geometry("300x200")

                tk.Label(modify_win, text="New Quantity:").pack(pady=10)
                qty_entry = tk.Entry(modify_win)
                qty_entry.insert(0, str(user_orders[index]["quantity"]))
                qty_entry.pack(pady=5)

                def save_modification():
                    new_qty = qty_entry.get()
                    if not new_qty.isdigit() or int(new_qty) <= 0:
                        messagebox.showerror("Error", "Enter a valid quantity.")
                        modify_win.focus_force()
                        return

                    new_qty = int(new_qty)
                    user_orders[index]["quantity"] = new_qty
                    user_orders[index]["total_price"] = new_qty * get_ticket_options()[user_orders[index]["ticket_type"]]["price"]

                   
                    for i, o in enumerate(all_orders):
                        if o == order:
                            all_orders[i] = user_orders[index]
                            break

                    save_orders(all_orders)
                    customer.purchase_history = [o for o in all_orders if o["user_email"] == customer.email]
                    messagebox.showinfo("Success", "Order updated successfully.")
                    modify_win.destroy()
                    orders_window.destroy()
                    self.view_orders() 

                tk.Button(modify_win, text="Save", command=save_modification).pack(pady=10)

            def delete_order(index=idx):
                result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this order?")
                if result:
                    target_order = user_orders[index]
                    all_orders.remove(target_order)
                    save_orders(all_orders)
                    customer.purchase_history = [o for o in all_orders if o["user_email"] == customer.email]
                    messagebox.showinfo("Deleted", "Order deleted successfully.")
                    orders_window.destroy()
                    self.view_orders() 

            btn_frame = tk.Frame(frame)
            btn_frame.pack(pady=5)

            tk.Button(btn_frame, text="Modify", command=modify_order).pack(side="left", padx=5)
            tk.Button(btn_frame, text="Delete", command=delete_order).pack(side="left", padx=5)


    def logout(self):
        self.controller.current_user = None 
        self.controller.show_frame("CustomerDashboard", "LoginPage") 
