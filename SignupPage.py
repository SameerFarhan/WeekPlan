import tkinter as tk
from tkinter import messagebox
from database  import create_account as db_create_account, get_user
import re

class SignupPage:
    def __init__(self, root):
        self.root = root

        #Name of the page 
        self.root.title("Signup Page")

        # Create the main frame
        self.frame = tk.Frame(self.root, bg="#e2f2ff" ,width=600, height=400)

        #Sign up form widget
        self.signup_image = tk.PhotoImage(file="image.png")
        self.signup_image_label = tk.Label(self.frame, image=self.signup_image)

        self.name_label = tk.Label(self.frame, text="Name: ")
        self.name_entry= tk.Entry(self.frame, width=30)

        self.username_label = tk.Label(self.frame, text="Username: ")
        self.username_entry= tk.Entry(self.frame, width=30)

        self.password_label = tk.Label(self.frame, text="Password: ")
        self.password_entry= tk.Entry(self.frame,show="*", width=30)

        self.signup_button = tk.Button(self.frame, text="Signup", bg="#0099ff", fg="white", command=self.create_account_action)

        # Link to switch to the login page
        self.login_link = tk.Label(self.frame, text=" Already have an account? Login in", fg="blue", cursor="hand2")
        self.login_link.bind("<Button-1>", self.switch_to_LoginPage)

        # Layout for the signup form
        self.name_label.grid(row=0, column=1, padx=10, pady=10,sticky="w")
        self.name_entry.grid(row=0, column=2, padx=10, pady=10,sticky="w")

        self.username_label.grid(row=1, column=1, padx=10, pady=10,sticky="w")
        self.username_entry.grid(row=1, column=2, padx=10, pady=10,sticky="w")

        self.password_label.grid(row=2, column=1, padx=10, pady=10,sticky="w")
        self.password_entry.grid(row=2, column=2, padx=10, pady=10,sticky="w")

        self.signup_button.grid(row=3, column=2, padx=10, pady=10, sticky="e")

        self.login_link.grid(row=4, column=2, padx=10, pady=10,sticky="w")
        # Layout for the frame
        self.frame.grid(row=0,column=0, padx=10, pady=10)
        
        self.signup_image_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky = "nsew")
      
    # switch to the sign-up  
    def switch_to_LoginPage(self, event):
     from loginPage import LoginPage
     self.frame.grid_forget()
     LoginPage(self.root).show()

    # Display the frame   
    def show(self):
        self.frame.grid(row=0, column=0, padx=10, pady=10)

    # creates the account
    def create_account_action(self):
    # Get input values
        name = self.name_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        # List of validation checks with corresponding error messages
        validations = [
            (not name.strip(), "Please fill in all fields."),
            (not username.strip(), "Please fill in all fields."),
            (not password.strip(), "Please fill in all fields."),
            (get_user(username), "Username already exists. Please choose a different username."),
            (not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,12}$", username), 
            "Username must be at least 8 characters long and less than 12 letters, must contain at least one capital letter and one number."),
            (not re.match(r"^(?=.*[A-Z])(?=.*\d).{8,12}$", password), 
            "Password must be at least 8 characters long and less than 12 letters, must contain at least one capital letter and one number.")
        ]

        # Iterate over validation checks and show the first error encountered
        for condition, error_message in validations:
            if condition:
                messagebox.showerror("Error", error_message)
                return

        # If all validations pass, proceed with account creation
        # Additional account creation logic here

        
        # Create the account
        db_create_account(name, username, password)
        messagebox.showinfo("Success", "Account created successfully!")
        from loginPage import LoginPage
        self.frame.grid_forget()
        LoginPage(self.root).show()

