import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json

class ProgressTracking:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Tracking pages")
        self.frame = tk.Frame(self.root, width=600, height=400, bg="#FFFFFF")
        self.header_frame = tk.Frame(self.frame, bg="#800080")
        self.nav_bar = tk.Frame(self.header_frame, bg="#800080")

        self.Program_name = tk.Label(self.nav_bar, text="WeekPlan", fg="white", bg="#800080", font=("Helvetica", 12, "bold"), cursor="hand2")
        self.Program_name.bind("<Button-1>", self.switch_to_MainPage)
        self.task_button = ttk.Button(self.nav_bar, text="Task", command=self.switch_to_TaskPage)
        self.ai_button = ttk.Button(self.nav_bar, text="AI", command=self.switch_to_AiPage)
        self.time_button = ttk.Button(self.nav_bar, text="Time", command=self.switch_to_ProgressTrackingPage)
        self.goals_button = ttk.Button(self.nav_bar, text="Goals", command=self.switch_to_GoalPage)

        self.stats_frame = tk.Frame(self.frame, width=400, height=100, bg="#83C0C1")
        self.time_spent_label = tk.Label(self.stats_frame, text="Total Time Spent:", fg="white", bg="#83C0C1", font=("Helvetica", 12, "bold"))
        self.time_spent_value = tk.Label(self.stats_frame, text="", fg="white", bg="#83C0C1", font=("Helvetica", 12, "bold"))

        self.list_frame = tk.Frame(self.frame, width=400, height=400, bg="#83C0C1")
        self.task_goal_list_label = tk.Label(self.list_frame, text="Completed Tasks and Goals:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))
        self.task_goal_list = tk.Text(self.list_frame, width=40, height=20, bg="#96E9C6", fg="black", font=("Helvetica", 10, "bold"))

        self.under_development = tk.Label(self.stats_frame, text="Under Development:", fg="white", bg="#83C0C1", font=("Helvetica", 10, "bold"))

        self.tasks_by_date = {}  
        self.load_tasks()
        self.goals_by_date = {}  
        self.load_goals()
        self.update_lists()

        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.header_frame.grid(row=0, column=0, sticky="ew")
        self.nav_bar.grid(row=0, column=0, sticky="ew")

        self.Program_name.grid(row=0, column=0, padx=5, pady=5)
        self.task_button.grid(row=0, column=1, padx=5, pady=5)
        self.ai_button.grid(row=0, column=2, padx=5, pady=5)
        self.time_button.grid(row=0, column=3, padx=5, pady=5)
        self.goals_button.grid(row=0, column=4, padx=5, pady=5)

        self.stats_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.time_spent_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.time_spent_value.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.list_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.task_goal_list_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.task_goal_list.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

        self.under_development.grid(row=1,column=0)

        self.createPieChart()
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


    def update_lists(self):
        total_time_spent = timedelta()
        total_time_spent_by_task = timedelta()
        total_time_spent_by_goals = timedelta()

        self.task_goal_list.delete("1.0", tk.END)

        def convert_duration_to_timedelta(duration_str):
        
            try:
                # Try to parse the duration as 'HH:MM:SS'
                return datetime.strptime(duration_str, "%H:%M:%S") - datetime(1900, 1, 1)
            except ValueError:
                # Handle the 'X day, HH:MM:SS' format
                days, time_str = 0, duration_str
                if 'day' in duration_str:
                    days, time_str = duration_str.split(', ')
                    days = int(days.split(' ')[0])
                hours, minutes, seconds = map(int, time_str.split(':'))
                return timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

        # Process completed tasks
        for date in self.tasks_by_date:
            for task_info in self.tasks_by_date[date]:
                if task_info.get("Completed"):
                    task = task_info.get("Task", "N/A")
                    priority = task_info.get("Priority", "N/A")
                    start_time = task_info.get("Start Time", "N/A")
                    end_time = task_info.get("End Time", "N/A")
                    duration = task_info.get("Duration", "00:00:00")
                    duration_td = convert_duration_to_timedelta(duration)
                    # Correct negative durations
                    if duration_td.days < 0:
                        duration_td = timedelta(days=0, seconds=duration_td.seconds, microseconds=duration_td.microseconds)
                    total_time_spent_by_task += duration_td
                    self.task_goal_list.insert(tk.END, f"Task: {task}, Priority: {priority}, Start Time: {start_time}, End Time: {end_time}, Duration: {duration_td}\n")

        # Process completed goals
        for date in self.goals_by_date:
            for goal_info in self.goals_by_date[date]:
                goal = goal_info.get("Goal", "N/A")
                priority = goal_info.get("Priority", "N/A")
                start_date = goal_info.get("Start Date", "N/A")
                end_date = goal_info.get("End Date", "N/A")
                duration = goal_info.get("Duration", "00:00:00")
                duration_td = convert_duration_to_timedelta(duration)
                # Correct negative durations
                if duration_td.days < 0:
                    duration_td = timedelta(days=0, seconds=duration_td.seconds, microseconds=duration_td.microseconds)
                total_time_spent_by_goals += duration_td
                self.task_goal_list.insert(tk.END, f"Goal: {goal}, Priority: {priority}, Start Date: {start_date}, End Date: {end_date}, Duration: {duration_td}\n")

        total_time_spent = total_time_spent_by_task + total_time_spent_by_goals

        # Display incomplete tasks
        self.task_goal_list.insert(tk.END, "\nIncomplete Tasks:\n", "incomplete")
        for date in self.tasks_by_date:
            for task_info in self.tasks_by_date[date]:
                if not task_info.get("Completed"):
                    task = task_info.get("Task", "N/A")
                    priority = task_info.get("Priority", "N/A")
                    start_time = task_info.get("Start Time", "N/A")
                    end_time = task_info.get("End Time", "N/A")
                    self.task_goal_list.insert(tk.END, f"Task: {task}, Priority: {priority}, Start Time: {start_time}, End Time: {end_time}\n", "incomplete")

        # Display incomplete goals
        self.task_goal_list.insert(tk.END, "\nIncomplete Goals:\n", "incomplete")
        for date in self.goals_by_date:
            for goal_info in self.goals_by_date[date]:
                if not goal_info.get("Completed"):
                    goal = goal_info.get("Goal", "N/A")
                    priority = goal_info.get("Priority", "N/A")
                    start_date = goal_info.get("Start Date", "N/A")
                    end_date = goal_info.get("End Date", "N/A")
                    self.task_goal_list.insert(tk.END, f"Goal: {goal}, Priority: {priority}, Start Date: {start_date}, End Date: {end_date}\n", "incomplete")

        self.task_goal_list.tag_config("incomplete", foreground="red")
        self.time_spent_value.config(text=str(total_time_spent))

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as task_file:
                self.tasks_by_date = json.load(task_file)
                for date in list(self.tasks_by_date):
                    if not self.tasks_by_date[date]:
                        del self.tasks_by_date[date]
        except FileNotFoundError:
            self.tasks_by_date = {}

    def load_goals(self):
        try:
            with open("goals.json", "r") as goal_file:
                self.goals_by_date = json.load(goal_file)
                for date in list(self.goals_by_date):
                    if not self.goals_by_date[date]:
                        del self.goals_by_date[date]
        except FileNotFoundError:
            self.goals_by_date = {}


    def createPieChart(self):
        # Load and parse tasks
        self.notice = tk.Label(self.stats_frame, text="UnderDevelopment: ")
        completed_tasks = sum(task.get("Completed", False) for tasks in self.tasks_by_date.values() for task in tasks)
        total_tasks = sum(len(tasks) for tasks in self.tasks_by_date.values())
        incomplete_tasks = total_tasks - completed_tasks

        # Load and parse goals
        completed_goals = sum(goal.get("Completed", False) for goals in self.goals_by_date.values() for goal in goals)
        total_goals = sum(len(goals) for goals in self.goals_by_date.values())
        incomplete_goals = total_goals - completed_goals

        # Combine counts
        total_completed = completed_tasks + completed_goals
        total_incomplete = incomplete_tasks + incomplete_goals

        PieV = [total_completed, total_incomplete]
        colV = ["#FFD700", "#FF4500"]
        labels = ['Completed', 'Incomplete']
        fig = Figure(figsize=(3, 1.5), dpi=100)
        ax = fig.add_subplot(111)
        ax.pie(PieV, colors=colV, labels=labels, autopct='%1.1f%%')

        self.pie_chart_canvas = FigureCanvasTkAgg(fig, master=self.frame)
        self.pie_chart_canvas.draw()
        self.pie_chart_canvas.get_tk_widget().grid(row=2, column=1, padx=10, pady=10, sticky="nsew")