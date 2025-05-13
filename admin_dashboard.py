import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime
from discount import Discount



def load_orders():
    try:
        with open("orders.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return []

def save_discounts(discounts):
    with open("discounts.pkl", "wb") as f:
        pickle.dump(discounts, f)

def load_discounts():
    try:
        with open("discounts.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return []


class AdminDashboard(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f9f9f9")

        tk.Label(self, text="Admin Dashboard", font=("Arial", 18, "bold"), bg="#f9f9f9").pack(pady=20)

        tk.Button(self, text="View Ticket Sales", command=self.view_ticket_sales, width=30).pack(pady=10)
        tk.Button(self, text="Manage Discounts", command=self.manage_discounts, width=30).pack(pady=10)

    def view_ticket_sales(self):
        sales_window = tk.Toplevel(self)
        sales_window.title("Ticket Sales")
        sales_window.geometry("400x300")

        orders = load_orders()
        sales_per_day = {}

        for order in orders:
            date_str = order.get("date", datetime.now().strftime("%Y-%m-%d"))
            sales_per_day[date_str] = sales_per_day.get(date_str, 0) + order["quantity"]

        if not sales_per_day:
            tk.Label(sales_window, text="No ticket sales yet.").pack(pady=20)
        else:
            for date, total in sorted(sales_per_day.items()):
                tk.Label(sales_window, text=f"{date}: {total} tickets").pack(pady=5)

    def manage_discounts(self):
        discount_window = tk.Toplevel(self)
        discount_window.title("Manage Discounts")
        discount_window.geometry("500x400")

        discounts = load_discounts()
        listbox = tk.Listbox(discount_window, width=70, height=10)
        listbox.pack(pady=10)

        def refresh_list():
            listbox.delete(0, tk.END)
            for d in discounts:
                listbox.insert(tk.END, f"{d.discount_id}: {d.description} - {d.percentage}% until {d.valid_until}")

        def add_discount():
            def save_new():
                try:
                    new_id = id_entry.get().strip()
                    desc = desc_entry.get().strip()
                    perc = float(perc_entry.get().strip())
                    valid = valid_entry.get().strip()

                    if not new_id or not desc or perc <= 0:
                        raise ValueError("Invalid data.")

                    discounts.append(Discount(new_id, desc, perc, valid))
                    save_discounts(discounts)
                    refresh_list()
                    add_win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                    add_win.focus_force()

            add_win = tk.Toplevel(discount_window)
            add_win.title("Add Discount")

            tk.Label(add_win, text="ID").pack(); id_entry = tk.Entry(add_win); id_entry.pack()
            tk.Label(add_win, text="Description").pack(); desc_entry = tk.Entry(add_win); desc_entry.pack()
            tk.Label(add_win, text="Percentage").pack(); perc_entry = tk.Entry(add_win); perc_entry.pack()
            tk.Label(add_win, text="Valid Until (YYYY-MM-DD)").pack(); valid_entry = tk.Entry(add_win); valid_entry.pack()

            tk.Button(add_win, text="Add", command=save_new).pack(pady=10)

        def delete_discount():
            selection = listbox.curselection()
            if not selection:
                return
            index = selection[0]
            del discounts[index]
            save_discounts(discounts)
            refresh_list()

        def edit_discount():
            selection = listbox.curselection()
            if not selection:
                return
            index = selection[0]
            d = discounts[index]

            def save_edit():
                try:
                    d.description = desc_entry.get().strip()
                    d.percentage = float(perc_entry.get().strip())
                    d.valid_until = datetime.strptime(valid_entry.get().strip(), "%Y-%m-%d").date()
                    save_discounts(discounts)
                    refresh_list()
                    edit_win.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
                    edit_win.focus_force()

            edit_win = tk.Toplevel(discount_window)
            edit_win.title("Edit Discount")

            tk.Label(edit_win, text="Description").pack(); desc_entry = tk.Entry(edit_win); desc_entry.insert(0, d.description); desc_entry.pack()
            tk.Label(edit_win, text="Percentage").pack(); perc_entry = tk.Entry(edit_win); perc_entry.insert(0, str(d.percentage)); perc_entry.pack()
            tk.Label(edit_win, text="Valid Until").pack(); valid_entry = tk.Entry(edit_win); valid_entry.insert(0, d.valid_until); valid_entry.pack()

            tk.Button(edit_win, text="Save Changes", command=save_edit).pack(pady=10)

        tk.Button(discount_window, text="Add Discount", command=add_discount).pack(side="left", padx=10, pady=5)
        tk.Button(discount_window, text="Edit Selected", command=edit_discount).pack(side="left", padx=10, pady=5)
        tk.Button(discount_window, text="Delete Selected", command=delete_discount).pack(side="left", padx=10, pady=5)

        refresh_list()

