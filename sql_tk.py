import customtkinter as ctk
from database.commands import get_user
from tkinter.messagebox import showerror
from pages.login_page import LoginPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("450x500")
        self.title("LOGIN")

        self.current_page = None
        self.show_page(LoginPage)

        self.title_font = ctk.CTkFont(family="Arial", size=40, weight="bold")
        self.body_font = ctk.CTkFont(family="Helvetica", size=16)
        self.button_font = ctk.CTkFont(family="Helvetica", size=13)
    
    def show_page(self,page,id = None):
        if self.current_page:
            self.current_page.destroy()

        self.current_page = page(self,id)
        self.current_page.pack(fill="both",expand=True)

    def show_default_page(self):
        self.show_page(LoginPage)

app = App()
app.mainloop()