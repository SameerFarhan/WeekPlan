import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class AiPage:
    def __init__(self,root):
        self.root = root
        self.root.title("AI Task Generator")
        self.frame = tk.Frame(self.root, width=600, height=400, bg="#FFFFFF")

        # Frame for navigation bar
        self.header_frame = tk.Frame(self.frame, bg="#800080")
        self.nav_bar = tk.Frame(self.header_frame, bg="#800080")

        # Navigation bar components
        self.Program_name = tk.Label(self.nav_bar, text="WeekPlan", fg="white", bg="#800080", font=("Helvetica", 12, "bold"), cursor="hand2")
        self.Program_name.bind("<Button-1>", self.switch_to_MainPage)
        self.task_button = ttk.Button(self.nav_bar, text="Task", command=self.switch_to_TaskPage)
        self.ai_button = ttk.Button(self.nav_bar, text="AI", command=self.switch_to_AiPage)
        self.time_button = ttk.Button(self.nav_bar, text="Time", command=self.switch_to_ProgressTrackingPage)
        self.goals_button = ttk.Button(self.nav_bar, text="Goals", command=self.switch_to_GoalPage)

        # Layout for navigation bar
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.nav_bar.grid(row=0, column=0, sticky="ew")
        self.Program_name.grid(row=0, column=0, padx=5, pady=5)
        self.task_button.grid(row=0, column=1, padx=5, pady=5)
        self.ai_button.grid(row=0, column=2, padx=5, pady=5)
        self.time_button.grid(row=0, column=3, padx=5, pady=5)
        self.goals_button.grid(row=0, column=4, padx=5, pady=5)

        # Date and task input fields
        self.second_frame = tk.Frame(self.frame, width=600, height=400, bg="#83C0C1")

        # Date
        self.date_label = tk.Label(self.second_frame, text="Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.date_entry = DateEntry(self.second_frame, width=20, state='readonly', date_pattern="dd-mm-yyyy")

        # Task details
        self.details_label = tk.Label(self.second_frame, text="Enter any important task or details:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.details_entry = tk.Text(self.second_frame, height=4, width=50, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Button to generate schedule
        self.generate_button = ttk.Button(self.second_frame, text="Generate Schedule")

        # Display for AI-generated schedule
        self.schedule_label = tk.Label(self.second_frame, text="Generated schedule for:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.schedule_display = tk.Label(self.second_frame, bg="#E6FFF2", height=10, width=50, anchor="nw", justify="left", relief="solid")

        # Layout for input fields and schedule display
        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.details_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.details_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.generate_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")
        self.schedule_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.schedule_display.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.second_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Configure resizing behavior
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(1, weight=1)
        self.second_frame.columnconfigure(1, weight=1)
    def show(self):
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def switch_to_MainPage(self, event=None):
        from mainPage import MainPage
        self.frame.grid_forget()
        MainPage(self.root).show()

    # switch to the TaskPage (refresh current page)
    def switch_to_TaskPage(self, event=None):
        from taskPage import TaskPage
        self.frame.grid_forget()
        TaskPage(self.root).show()

    # switch to the AI page
    def switch_to_AiPage(self, event=None):
        from aiPage import AiPage
        self.frame.grid_forget()
        AiPage(self.root).show()

    # switch to the progress tracking page
    def switch_to_ProgressTrackingPage(self, event=None):
        from progressTracking import ProgressTracking
        self.frame.grid_forget()
        ProgressTracking(self.root).show()

    # switch to the goals page
    def switch_to_GoalPage(self, event=None):
        from goalPage import GoalPage
        self.frame.grid_forget()
        GoalPage(self.root).show()