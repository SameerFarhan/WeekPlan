import json
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime

class MainPage():
    def __init__(self,root):
        self.root = root
        self.root.title("Home Page")
        # Create the main frame to contain other widgets
        self.frame = tk.Frame(self.root, width=600, height=400, bg="#FFFFFF")
            
        # Create a frame for the task list on the left
        self.task_frame = tk.Frame(self.frame, width=400, height=400, bg="#83C0C1")
        # Create a frame for the goal list on the left
        self.goal_frame = tk.Frame(self.frame, width=400, height=400, bg="#83C0C1")
        # Create a frame for the navigation bar at the top
        self.header_frame = tk.Frame(self.frame, bg="#800080")
        self.nav_bar = tk.Frame(self.header_frame, bg="#800080")

        # Navigation bar components
        self.Program_name = tk.Label(self.nav_bar, text="WeekPlan", fg="white", bg="#800080", font=("Helvetica", 12, "bold"), cursor="hand2")
        self.Program_name.bind("<Button-1>", self.switch_to_MainPage)  # Bind click event to the label
        self.task_button = ttk.Button(self.nav_bar, text="Task", command=self.switch_to_TaskPage)
        self.ai_button = ttk.Button(self.nav_bar, text="AI", command=self.switch_to_AiPage)
        self.time_button = ttk.Button(self.nav_bar, text="Time", command=self.switch_to_ProgressTrackingPage)
        self.goals_button = ttk.Button(self.nav_bar, text="Goals", command=self.switch_to_GoalPage)
         
        # Create a frame for the calendar on the right
        self.calendar_frame = tk.Frame(self.frame, width=400, height=400, bg="#83C0C1")

        # Create a frame for the calendar on the right
        self.Goal_calendar_frame = tk.Frame(self.frame, width=400, height=400, bg="#83C0C1")

        # Calendar components
        self.calendar_label = tk.Label(self.calendar_frame, text="Select Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.calendar_entry = DateEntry(self.calendar_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")
        self.calendar_entry.bind("<<DateEntrySelected>>", self.update_task_list)  # Update task list when date is selected

         # Calendar components
        self.Goal_calendar_label = tk.Label(self.Goal_calendar_frame, text="Select Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.Goal_calendar_entry = DateEntry(self.Goal_calendar_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")
        self.Goal_calendar_entry.bind("<<DateEntrySelected>>", self.update_goal_list)

        # Task list components
        self.task_list_label = tk.Label(self.task_frame, text="Tasks Entered:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.task_list = tk.Text(self.task_frame, width=40, height=10, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Goal list components
        self.goal_list_label = tk.Label(self.goal_frame, text="Goals Entered:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.goal_list = tk.Text(self.goal_frame, width=40, height=10, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Date
        self.date_label = tk.Label(self.task_frame, text="Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.date_entry = DateEntry(self.task_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")
        self.date_entry.bind("<<DateEntrySelected>>", self.update_task_list)  # Bind date change event

        # Load tasks from JSON file
        self.tasks_by_date = {}  
        self.load_tasks()  # Load tasks from JSON file
        self.update_task_list()  # Update task list initially

        # Load goals from JSON file
        self.goals_by_date = {}  
        self.load_goals()  # Load goals from JSON file
        self.update_goal_list()  # Update goal list initially

        # Layout setup
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.nav_bar.grid(row=0, column=0, sticky="ew")

        # Arrange navigation bar components
        self.Program_name.grid(row=0, column=0, padx=5, pady=5)
        self.task_button.grid(row=0, column=1, padx=5, pady=5)
        self.ai_button.grid(row=0, column=2, padx=5, pady=5)
        self.time_button.grid(row=0, column=3, padx=5, pady=5)
        self.goals_button.grid(row=0, column=4, padx=5, pady=5)

            # Arrange task frame
        self.task_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Arrange calendar frame
        self.calendar_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.Goal_calendar_frame.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Arrange goal frame
        self.goal_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Arrange task list components
        self.task_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.task_list.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        # Arrange calendar components
        self.calendar_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.calendar_entry.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Arrange calendar components
        self.Goal_calendar_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.Goal_calendar_entry.grid(row=2, column=0, padx=10, pady=5, sticky="w")


        # Arrange goal list components
        self.goal_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.goal_list.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
     
        

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

    # Update the task list based on the selected date  
    def update_task_list(self, event=None):
        # Clear the task list
        self.task_list.delete("1.0", tk.END)

        selected_date = self.calendar_entry.get_date().strftime('%d-%m-%Y')  
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

    def update_goal_list(self, event=None):
        # Clear the goal list
        self.goal_list.delete(1.0, tk.END)

        selected_date = self.Goal_calendar_entry.get_date().strftime('%d-%m-%Y')  
        if selected_date in self.goals_by_date:
            for idx, goal_info in enumerate(self.goals_by_date[selected_date]):
                goal = goal_info.get("Goal", "")
                start_date = goal_info.get("Start Date", "")
                end_date = goal_info.get("End Date", "")
                duration = goal_info.get("Duration", "")
                priority = goal_info.get("Priority", "")
                completed = goal_info.get("Completed", False)  # Get completion status

                # Create a checkbox for each goal
                if goal and start_date:  # Check if 'Start Date' exists
                    var = tk.IntVar(value=completed)  # Set IntVar value based on completion status
                    checkbox = tk.Checkbutton(self.goal_list, text=f"Goal: {goal}, Start Date: {start_date} End Date: {end_date}, Priority: {priority}",
                                            variable=var, command=lambda idx=idx: self.toggle_goal_completion(selected_date, idx))
                    checkbox.var = var
                    if completed:
                        checkbox.config(font="TkDefaultFont 9 overstrike")  # Apply strikethrough if completed
                    self.goal_list.window_create("end", window=checkbox)
                    self.goal_list.insert("end", "\n")

    def toggle_goal_completion(self, date, idx):
        if date in self.goals_by_date:
            if 0 <= idx < len(self.goals_by_date[date]):
                goal_info = self.goals_by_date[date][idx]
                goal_info["Completed"] = not goal_info.get("Completed", False)
                self.save_goals()
                self.update_goal_list()

    def load_goals(self):
        try:
            # Load goals from file
            with open("goals.json", "r") as file:
                self.goals_by_date = json.load(file)
                # Remove completed goals
                for date in list(self.goals_by_date.keys()):
                    self.goals_by_date[date] = [goal for goal in self.goals_by_date[date] if not goal.get("Completed", False)]
                    if not self.goals_by_date[date]:
                        del self.goals_by_date[date]
        except FileNotFoundError:
            # If file does not exist, initialize with empty dictionary
            self.goals_by_date = {}

    def save_goals(self):
        # Save goals to file
        with open("goals.json", "w") as file:
            json.dump(self.goals_by_date, file)
