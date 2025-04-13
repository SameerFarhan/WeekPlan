import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import json

class GoalPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Enter Goal")
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

        # Second frame for goal details
        self.second_frame = tk.Frame(self.frame, width=600, height=400, bg="#83C0C1")

        # Enter goal section widgets
        # Start Date
        self.start_date_label = tk.Label(self.second_frame, text="Start Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.start_date_entry = DateEntry(self.second_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")

        # End Date
        self.end_date_label = tk.Label(self.second_frame, text="End Date:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.end_date_entry = DateEntry(self.second_frame, width=20, state='readonly', date_pattern="DD-MM-YYYY")

        # Goal
        self.goal_label = tk.Label(self.second_frame, text="Enter goal:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.goal_text = tk.Text(self.second_frame, width=20, height=3, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Priority
        self.priority_label = tk.Label(self.second_frame, text="Priority:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.priority_frame = tk.Frame(self.second_frame, bg="#83C0C1")
        self.high_var = tk.IntVar()
        self.medium_var = tk.IntVar()
        self.low_var = tk.IntVar()
        self.high_checkbox = tk.Checkbutton(self.priority_frame, text="High", variable=self.high_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")
        self.medium_checkbox = tk.Checkbutton(self.priority_frame, text="Medium", variable=self.medium_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")
        self.low_checkbox = tk.Checkbutton(self.priority_frame, text="Low", variable=self.low_var, bg="#83C0C1", fg="white", font=("Helvetica", 10, "bold"), selectcolor="#83C0C1")

        # Button to enter goal
        self.button = ttk.Button(self.second_frame, text="Enter goal", command=self.submit_goal)

        # Third frame for goal list
        self.third_frame = tk.Frame(self.frame, width=400, height=300, bg="#83C0C1")

        # Goal list
        self.goal_list_label = tk.Label(self.third_frame, text="Goals Entered:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.goal_list = tk.Text(self.third_frame, width=40, height=10, bg="#96E9C6", fg="white", font=("Helvetica", 10, "bold"))

        # Dictionary to store goals by start date
        # Load goals from file
        self.goals_by_date = {}
        self.load_goals()  # Load goals from JSON file
        self.update_goal_list()

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



        # Layout for second frame
        self.start_date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.start_date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.end_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.end_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.goal_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.goal_text.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.priority_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.priority_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.high_checkbox.grid(row=0, column=0, padx=5, pady=5)
        self.medium_checkbox.grid(row=0, column=1, padx=5, pady=5)
        self.low_checkbox.grid(row=0, column=2, padx=5, pady=5)
        self.button.grid(row=4, column=0, columnspan=4, pady=10)

        # Layout for third frame
        self.goal_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.goal_list.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        self.start_date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.start_date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.end_date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.end_date_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.goal_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.goal_text.grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.priority_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.priority_frame.grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky="ew")
        self.high_checkbox.grid(row=0, column=0, padx=5, pady=5)
        self.medium_checkbox.grid(row=0, column=1, padx=5, pady=5)
        self.low_checkbox.grid(row=0, column=2, padx=5, pady=5)
        self.button.grid(row=4, column=0, columnspan=4, pady=10)
        self.goal_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.goal_list.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")

        # Configure resizing behavior
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.second_frame.rowconfigure(1, weight=1)
        self.second_frame.columnconfigure(1, weight=1)
        self.third_frame.rowconfigure(1, weight=1)
        self.third_frame.columnconfigure(0, weight=1)

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

    # Function to submit a goal
        # Function to submit a goal
    def submit_goal(self):
        goal = self.goal_text.get("1.0", "end-1c")
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        priority = "High" if self.high_var.get() else "Medium" if self.medium_var.get() else "Low" if self.low_var.get() else "None"
        self.goal_text.delete("1.0", tk.END)

        if start_date not in self.goals_by_date:
            self.goals_by_date[start_date] = []

        # Calculate duration
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")
        end_datetime = datetime.strptime(end_date, "%d-%m-%Y")
        duration = end_datetime - start_datetime

        # Record the start time when the goal is created
        start_time = datetime.now().strftime("%H:%M:%S")
        self.goals_by_date[start_date].append({
            "Goal": goal,
            "Start Date": start_date,
            "End Date": end_date,
            "Start Time": start_time,  # Record the start time
            "Priority": priority,
            "Completed": False
        })

        self.update_goal_list()  # Update the goal list after adding the new goal
        # Save goals to file after submitting
        self.save_goals()


    # Function to update goal list display
    def update_goal_list(self, event=None):
        # Clear the goal list
        self.goal_list.delete(1.0, tk.END)

        selected_date = self.start_date_entry.get()
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


    # Function to toggle goal completion
    def toggle_goal_completion(self, date, idx):
        if date in self.goals_by_date:
            if 0 <= idx < len(self.goals_by_date[date]):
                goal_info = self.goals_by_date[date][idx]
                goal_info["Completed"] = not goal_info.get("Completed", False)
                if goal_info["Completed"]:
                    # Record end time when goal is marked as completed
                    end_time = datetime.now().strftime("%H:%M:%S")
                    goal_info["End Time"] = end_time
                    # Calculate duration
                    start_time = datetime.strptime(goal_info["Start Time"], "%H:%M:%S")
                    end_time = datetime.strptime(end_time, "%H:%M:%S")
                    duration = end_time - start_time
                    goal_info["Duration"] = str(duration)
                else:
                    # If goal is unmarked, remove end time and duration
                    goal_info.pop("End Time", None)
                    goal_info.pop("Duration", None)
                self.save_goals()
                self.update_goal_list()


    # Function to load goals from file
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

    # Function to save goals to file
    def save_goals(self):
        # Save goals to file
        with open("goals.json", "w") as file:
            json.dump(self.goals_by_date, file)


            