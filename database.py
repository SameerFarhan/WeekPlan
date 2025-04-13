import sqlite3
import bcrypt 
from tkinter import messagebox
DB_FILE = "login_info.db"

# Function to create the users table in the database if it doesn't already exist
def create_table(show_message=True):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        # Create the users table with columns for id, name, username, and password_hash
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        conn.commit()
        if show_message:
            messagebox.showinfo("Success", "Table created successfully!")
    except sqlite3.Error as e:
        if show_message:
            messagebox.showerror("Database Error", f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

# Function to create a new user account
def create_account(name, username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Insert the new user's data into the users table
        cursor.execute('''
            INSERT INTO users (name, username, password_hash)
            VALUES (?, ?, ?)
        ''', (name, username, password_hash))
        conn.commit()
    finally:
        if conn:
            conn.close()
            
# Function to retrieve a user's information from the database by username
def get_user(username):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE username=?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user
