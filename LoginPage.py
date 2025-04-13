import tkinter as tk
from tkinter import messagebox
import bcrypt
from database import get_user

class LoginPage:
    def __init__(self, root):
        self.root = root

        #Name of the page 
        self.root.title("Login Page")

        #farme
        self.frame = tk.Frame(self.root, bg="#e2f2ff", width=600, height=400)

        #login form widget
        self.login_image = tk.PhotoImage(file="image.png")
        self.login_image_label = tk.Label(self.frame, image=self.login_image)

        self.username_label = tk.Label(self.frame, text="Username: ")
        self.username_entry= tk.Entry(self.frame, width=30)

        self.password_label = tk.Label(self.frame, text="Password: ")
        self.password_entry= tk.Entry(self.frame,show="*", width=30)

        self.login_button = tk.Button(self.frame, text="Login", bg="#0099ff", fg="white", command=self.handle_login)

        #link to switch to signup page
        self.signup_link = tk.Label(self.frame, text="Don't have an account? Sign Up", fg="blue", cursor="hand2")
        self.signup_link.bind("<Button-1>", self.switch_to_SignupPage)

        #Login from layout
        self.login_image_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10,sticky="nsew")
        
        self.username_label.grid(row=0, column=1, padx=10, pady=10,sticky="w")
        self.username_entry.grid(row=0, column=2, padx=10, pady=10,sticky="w")

        self.password_label.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.password_entry.grid(row=1, column=2, padx=10, pady=10,sticky="w")

        self.login_button.grid(row=2, column=2, padx=10, pady=10,sticky="e")
        
        self.signup_link.grid(row=3, column=2, padx=10, pady=10,sticky="w")

        #frame layout
        self.frame.grid(row=0,column=0, padx=10, pady=10)

    
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Validate empty fields
        if not username.strip() or not password.strip():
            self.show_message("Please enter both username and password.")
            return

        # Retrieve the user from the database
        user = get_user(username)

        if user is None:
            self.show_message("Invalid username!")
        else:
            # Verify the password
            if bcrypt.checkpw(password.encode('utf-8'), user[3].encode('utf-8')):
                self.switch_to_MainPage()
            else:
                self.show_message("Invalid password!")
    
    def show_message(self, message, success=False):
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)
        
    # switch to the sign-up page
    def switch_to_SignupPage(self, event = "None"):
        from signupPage import SignupPage
        self.frame.grid_forget()
        SignupPage(self.root).show()

    # switch to the main page
    def switch_to_MainPage(self):
        from mainPage import MainPage
        self.frame.grid_forget()
        MainPage(self.root).show()
    
    # Show the frame
    def show(self):
        self.frame.grid(row=0, column=0, padx=10, pady=10)

    