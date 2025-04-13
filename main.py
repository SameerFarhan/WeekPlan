import tkinter as tk
from loginPage import LoginPage


if __name__ == "__main__":
    root = tk.Tk()
    # Main_Page = LoginPage(root)
    # Main_Page.show()
    login_Page = LoginPage(root)
    login_Page.show()
    root.mainloop()