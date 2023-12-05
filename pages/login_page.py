import customtkinter as ctk
from database.commands import get_user,add_user
from tkinter.messagebox import showerror,showinfo
from .notes_page import NotePage

class LoginPage(ctk.CTkFrame):
    def __init__(self,container,user_id,**kwargs):
        super().__init__(container,**kwargs)
        self.container = container
        lbl1 = ctk.CTkLabel(self,text="Login: ")
        lbl1.pack()
        
        self.ent_log= ctk.CTkEntry(self)
        self.ent_log.pack()

        lbl2 = ctk.CTkLabel(self,text="Password: ")
        lbl2.pack()

        self.ent_pas= ctk.CTkEntry(self,show="*")
        self.ent_pas.pack()

        btn_ent = ctk.CTkButton(self,text= "Login",command = self.login)
        btn_ent.pack()

        lbl = ctk.CTkLabel(self,text= "Are you not registred?")
        lbl.pack()

        btn_r = ctk.CTkButton(self,text= "Sign up",command = self.new)
        btn_r.pack()
    
    def new(self):
         self.container.show_page(NewPage)

    def login(self):
        username = self.ent_log.get()
        password = self.ent_pas.get()

        if username == "" or  password =="":
            showerror("ERROR","Fields must not be empty")

        res = get_user(username,password)
        if not res:
                showerror("User Not Found","Inncorrect username or password")
                self.ent_log.delete(0,"end")
                self.ent_pas.delete(0,"end")
        else:
             self.container.show_page(NotePage,res.user_id)         


class NewPage(ctk.CTkFrame):
    def __init__(self,container,user_id,**kwargs):
        super().__init__(container,**kwargs)
        self.container = container

        lbl_new = ctk.CTkLabel(self,text="Entry your login: ")
        lbl_new.pack()

        self.ent_new_log= ctk.CTkEntry(self)
        self.ent_new_log.pack()

        lbl_pass = ctk.CTkLabel(self,text="Entry your password: ")
        lbl_pass.pack()

        self.ent_new_pas= ctk.CTkEntry(self,show="*")
        self.ent_new_pas.pack()

        self.ent_rep_pas = ctk.CTkEntry(self,show="*")
        self.ent_rep_pas.pack()

        btn_save = ctk.CTkButton(self,text= "Save",command = self.register_user)
        btn_save.pack()

    def register_user(self):
        username = self.ent_new_log.get()
        password = self.ent_new_pas.get()
        rep_password = self.ent_rep_pas.get()
        
        if username == "" or  password == "" or rep_password == "":
            showerror("ERROR","Fields must not be empty")
        
        elif password != rep_password:
            showerror("ERROR","passwords must be the same")    
        else:
            add_user(username,password)
            self.container.show_page(LoginPage)
            showinfo("Congratulations","Account registered successfully")