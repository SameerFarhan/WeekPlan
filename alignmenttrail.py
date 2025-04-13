import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

class TaskPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter_Task")
        self.frame = tk.Frame(self.root, width=600, height=400, bg="#FFFFFF")

        # Frame for navigation bar
        self.header_frame = tk.Frame(self.frame, bg="#800080")
        self.nav_bar = tk.Frame(self.header_frame, bg="#800080")

        # Nav bar function
        self.Program_name = tk.Label(self.nav_bar, text="WeekPlan", fg="white", bg="#800080", font=("Helvetica", 12, "bold"), cursor="hand2")
        self.Program_name.bind("<Button-1>", self.Switch_to_MainPage)  # Bind click event to the label
        self.task_button = ttk.Button(self.nav_bar, text="Task", command=self.Switch_to_TaskPage)
        self.ai_button = ttk.Button(self.nav_bar, text="AI", command=self.Switch_to_AiPage)
        self.time_button = ttk.Button(self.nav_bar, text="Time", command=self.Switch_to_ProgressTrackingPage)
        self.goals_button = ttk.Button(self.nav_bar, text="Goals", command=self.Switch_to_GoalPage)

        # Second frame for task details
        self.second_frame = tk.Frame(self.frame, width=600, height=400, bg="#83C0C1")

        # Enter task section
        # Date
        self.date_label = tk.Label(self.second_frame, text="Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.date_entry = DateEntry(self.second_frame, width=20, state='readonly')

        # Task
        self.task_label = tk.Label(self.second_frame, text="Enter task:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.task_text = tk.Text(self.second_frame, width=20, height=3, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Priority
        self.priority_label = tk.Label(self.second_frame, text="Priority:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.priority_frame = tk.Frame(self.second_frame, bg="#83C0C1")
        self.high_var = tk.IntVar()
        self.medium_var = tk.IntVar()
        self.low_var = tk.IntVar()
        self.high_checkbox = tk.Checkbutton(self.priority_frame, text="High", variable=self.high_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")
        self.medium_checkbox = tk.Checkbutton(self.priority_frame, text="Medium", variable=self.medium_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")
        self.low_checkbox = tk.Checkbutton(self.priority_frame, text="Low", variable=self.low_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")

        # Time
        self.time_label = tk.Label(self.second_frame, text="Time:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.time_entry = ttk.Entry(self.second_frame, width=20)
        self.update_time()

        # Button
        self.button = ttk.Button(self.second_frame, text="Enter task", command=self.submit_task)

        # Third frame for task list
        self.third_frame = tk.Frame(self.frame, width=400, height=300, bg="#83C0C1")

        # Task list
        self.task_list_label = tk.Label(self.third_frame, text="Tasks Entered:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.task_list = tk.Text(self.third_frame, width=40, height=10, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Layout
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.nav_bar.grid(row=0, column=0, sticky="ew")
        self.Program_name.grid(row=0, column=0, padx=5, pady=5)
        self.task_button.grid(row=0, column=1, padx=5, pady=5)
        self.ai_button.grid(row=0, column=2, padx=5, pady=5)
        self.time_button.grid(row=0, column=3, padx=5, pady=5)
        self.goals_button.grid(row=0, column=4, padx=5, pady=5)

        self.second_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.third_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.task_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.task_text.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.priority_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.priority_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.high_checkbox.grid(row=0, column=0, padx=5, pady=5)
        self.medium_checkbox.grid(row=0, column=1, padx=5, pady=5)
        self.low_checkbox.grid(row=0, column=2, padx=5, pady=5)
        self.time_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.time_entry.grid(row=3, column=1, columnspan=3, padx=10, pady=5, sticky="ew")
        self.button.grid(row=4, column=0, columnspan=4, pady=10)

        self.task_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.task_list.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(1, weight=1)
        self.second_frame.columnconfigure(1, weight=1)
        self.third_frame.rowconfigure(1, weight=1)
        self.third_frame.columnconfigure(0, weight=1)

    def show(self):
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    def Switch_to_MainPage(self, event=None):
        from MainPage import MainPage
        self.frame.grid_forget()
        MainPage(self.root).show()

    def Switch_to_TaskPage(self, event=None):
        from TaskPage import TaskPage
        self.frame.grid_forget()
        TaskPage(self.root).show()

    def Switch_to_AiPage(self, event=None):
        from AiPage import AiPage
        self.frame.grid_forget()
        AiPage(self.root).show()

    def Switch_to_ProgressTrackingPage(self, event=None):
        from ProgressTracking import ProgressTracking
        self.frame.grid_forget()
        ProgressTracking(self.root).show()

    def Switch_to_GoalPage(self, event=None):
        from GoalPage import GoalPage
        self.frame.grid_forget()
        GoalPage(self.root).show()

    def show_calendar(self):
        selected_date = self.date_entry.get_date()
        print(f"Selected Date: {selected_date}")

    def submit_task(self):
        task = self.task_text.get("1.0", "end-1c")
        date = self.date_entry.get()
        priority = "High" if self.high_var.get() else "Medium" if self.medium_var.get() else "Low" if self.low_var.get() else "None"
        time = self.time_entry.get()
        self.task_list.insert("end", f"Task: {task}, Date: {date}, Priority: {priority}, Time: {time}\n")

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, current_time)
        self.time_entry.after(1000, self.update_time)