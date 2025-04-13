import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import json

class TaskPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Task")
        self.frame = tk.Frame(self.root, width=600, height=400, bg="#FFFFFF")

        # Frame for navigation bar
        self.header_frame = tk.Frame(self.frame, bg="#800080")
        self.nav_bar = tk.Frame(self.header_frame, bg="#800080")

        # Navigation bar components
        self.Program_name = tk.Label(self.nav_bar, text="WeekPlan", fg="white", bg="#800080", font=("Helvetica", 12, "bold"), cursor="hand2")
        self.Program_name.bind("<Button-1>", self.switch_to_MainPage)  # Bind click event to the label
        self.task_button = ttk.Button(self.nav_bar, text="Task", command=self.switch_to_TaskPage)
        self.ai_button = ttk.Button(self.nav_bar, text="AI", command=self.switch_to_AiPage)
        self.time_button = ttk.Button(self.nav_bar, text="Time", command=self.switch_to_ProgressTrackingPage)
        self.goals_button = ttk.Button(self.nav_bar, text="Goals", command=self.switch_to_GoalPage)

        # Second frame for task details
        self.second_frame = tk.Frame(self.frame, width=600, height=400, bg="#83C0C1")

        # Enter task section widgets
        # Date
        self.date_label = tk.Label(self.second_frame, text="Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.date_entry = DateEntry(self.second_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")
        self.date_entry.bind("<<DateEntrySelected>>", self.update_task_list)  # Bind date change event

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
        self.update_time()  # Update time entry with current time

        # Button to enter task
        self.button = ttk.Button(self.second_frame, text="Enter task", command=self.submit_task)

        # Third frame for task list
        self.third_frame = tk.Frame(self.frame, width=400, height=300, bg="#83C0C1")

        # Task list
        self.task_list_label = tk.Label(self.third_frame, text="Tasks Entered:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.task_list = tk.Text(self.third_frame, width=40, height=10, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Dictionary to store tasks by date
        # Load tasks from file
        self.tasks_by_date = {}
        self.goals_by_date = {}
        # self.load_goals()  # Load goals from JSON file
        self.load_tasks()  # Load tasks from JSON file
        # self.update_goal_list()
        self.update_task_list()

        # Layout configuration
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

        # Configure resizing behavior
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(1, weight=1)
        self.second_frame.columnconfigure(1, weight=1)
        self.third_frame.rowconfigure(1, weight=1)
        self.third_frame.columnconfigure(0, weight=1)

    # Show the frame
    def show(self):
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # switch to the main page
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

    # Function to display calendar
    def show_calendar(self):
        selected_date = self.date_entry.get_date()

    # Function to submit a task
    def submit_task(self):
        task = self.task_text.get("1.0", "end-1c")
        date = self.date_entry.get()
        priority = "High" if self.high_var.get() else "Medium" if self.medium_var.get() else "Low" if self.low_var.get() else "None"
        start_time = self.time_entry.get()  # Record the start time when the task is added
        self.task_text.delete("1.0", tk.END)

        if date not in self.tasks_by_date:
            self.tasks_by_date[date] = []

        # Append task information to tasks_by_date dictionary
        self.tasks_by_date[date].append({"Task": task, "Priority": priority, "Time": start_time, "Start Time": start_time, "Completed": False}) 
        self.update_task_list()
        # Save tasks to file after submitting
        self.save_tasks()

    # Function to continuously update time entry widget
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, current_time)
        self.time_entry.after(1000, self.update_time)

   

    # Function to update task list display
    def update_task_list(self, event=None):
        # Clear the task list
        self.task_list.delete("1.0", tk.END)

        selected_date = self.date_entry.get()
        if selected_date in self.tasks_by_date:
            for idx, task_info in enumerate(self.tasks_by_date[selected_date]):
                task = task_info["Task"]
                priority = task_info["Priority"]
                time = task_info["Time"]
                completed = task_info.get("Completed", False)  # Get completion status

                # Create a checkbox for each task
                var = tk.IntVar(value=completed)  # Set IntVar value based on completion status
                checkbox = tk.Checkbutton(self.task_list, text=f"Task: {task}, Priority: {priority}, Time: {time}",
                                          variable=var, command=lambda idx=idx: self.toggle_task_completion(selected_date, idx))
                checkbox.var = var
                if completed:
                    checkbox.config(font="TkDefaultFont 9 overstrike")  # Apply strikethrough if completed
                self.task_list.window_create("end", window=checkbox)
                self.task_list.insert("end", "\n")

    # Function to toggle task completion
    def toggle_task_completion(self, date, idx):
        if date in self.tasks_by_date:
            if 0 <= idx < len(self.tasks_by_date[date]):
                task_info = self.tasks_by_date[date][idx]
                task_info["Completed"] = not task_info.get("Completed", False)
                if task_info["Completed"]:
                    # Record end time when task is marked as completed
                    end_time = datetime.now().strftime("%H:%M:%S")
                    task_info["End Time"] = end_time
                    # Calculate duration
                    start_time = datetime.strptime(task_info["Start Time"], "%H:%M:%S")
                    end_time = datetime.strptime(end_time, "%H:%M:%S")
                    duration = end_time - start_time
                    task_info["Duration"] = str(duration)
                else:
                    # If task is unmarked, remove end time and duration
                    task_info.pop("End Time", None)
                    task_info.pop("Duration", None)
                self.save_tasks()
                self.update_task_list()
    
    # Function to load tasks and goals from file
    def load_tasks(self):
        try:
            # Load tasks from "tasks.json" file
            with open("tasks.json", "r") as task_file:
                self.tasks_by_date = json.load(task_file)
                # Remove completed tasks
                for date in list(self.tasks_by_date.keys()):
                    self.tasks_by_date[date] = [task for task in self.tasks_by_date[date] if not task.get("Completed", False)]
                    if not self.tasks_by_date[date]:
                        del self.tasks_by_date[date]
        except FileNotFoundError:
            # If file does not exist, initialize tasks with empty dictionary
            self.tasks_by_date = {}


    # Function to save tasks to file
    def save_tasks(self):
        # Save tasks to file
        with open("tasks.json", "w") as file:
            json.dump(self.tasks_by_date, file)

    # Function to retrieve tasks based on specified criteria
    def retrieve_tasks(self, date=None, priority=None, time=None):
        filtered_tasks = []
        for task_date, tasks in self.tasks_by_date.items():
            for task_info in tasks:
                task = task_info["Task"]
                task_priority = task_info["Priority"]
                task_time = task_info["Time"]
                if (date is None or task_date == date) and \
                   (priority is None or task_priority == priority) and \
                   (time is None or task_time == time):
                    filtered_tasks.append({"Date": task_date, "Task": task, "Priority": task_priority, "Time": task_time})
        return filtered_tasks
    
    # def update_goal_list(self, event=None):
    #     start_date = self.start_date_entry.get()
    #     end_date = self.end_date_entry.get()      
    #     selected_date = self.start_date_entry.get()
    #     if selected_date in self.goals_by_date:
    #         for idx, goal_info in enumerate(self.goals_by_date[selected_date]):
    #             goal = goal_info.get("Goal", "")
    #             start_date = goal_info.get("Start Date", "")
    #             end_date = goal_info.get("End Date", "")
    #             duration = goal_info.get("Duration", "")
    #             priority = goal_info.get("Priority", "")
    #             completed = goal_info.get("Completed", False)  # Get completion status

    #             # Create a checkbox for each goal
    #             if goal and start_date:  # Check if 'Start Date' exists
    #                 var = tk.IntVar(value=completed)  # Set IntVar value based on completion status
    #                 checkbox = tk.Checkbutton(self.goal_list, text=f"Goal: {goal}, Start Date: {start_date} End Date: {end_date}, Priority: {priority}",
    #                                         variable=var, command=lambda idx=idx: self.toggle_goal_completion(selected_date, idx))
    #                 checkbox.var = var
    #                 if completed:
    #                     checkbox.config(font="TkDefaultFont 9 overstrike")  # Apply strikethrough if completed
    #                 self.task_list.window_create("end", window=checkbox)
    #                 self.goal_list.insert("end", "\n")


    # # Function to toggle goal completion
    # def toggle_goal_completion(self, date, idx):
    #     if date in self.goals_by_date:
    #         if 0 <= idx < len(self.goals_by_date[date]):
    #             goal_info = self.goals_by_date[date][idx]
    #             goal_info["Completed"] = not goal_info.get("Completed", False)
    #             self.update_goal_list()

    # # Function to load goals from file
    # def load_goals(self):
    #     try:
    #         # Load goals from file
    #         with open("goals.json", "r") as file:
    #             self.goals_by_date = json.load(file)
    #             # Remove completed goals
    #             for date in list(self.goals_by_date.keys()):
    #                 self.goals_by_date[date] = [goal for goal in self.goals_by_date[date] if not goal.get("Completed", False)]
    #                 if not self.goals_by_date[date]:
    #                     del self.goals_by_date[date]
    #     except FileNotFoundError:
    #         # If file does not exist, initialize with empty dictionary
    #         self.goals_by_date = {}