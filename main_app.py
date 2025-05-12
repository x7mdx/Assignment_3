import tkinter as tk
from login_page import LoginPage, RegisterPage

class TicketApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Race Ticketing System")
        self.geometry("600x450")
        self.resizable(False, False)

        self.frames = {}
        self.current_user = None 

        login_page = LoginPage(parent=self, controller=self)
        self.frames["LoginPage"] = login_page

        register_page = RegisterPage(parent=self, controller=self)
        self.frames["RegisterPage"] = register_page

        login_page.pack(fill="both", expand=True)

    def show_frame(self, current_page, next_page_name):
        self.frames[current_page].pack_forget() 
        self.frames[next_page_name].pack(fill="both", expand=True)


if __name__ == "__main__":
    app = TicketApp()
    app.mainloop()
