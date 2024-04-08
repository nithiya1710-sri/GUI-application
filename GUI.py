import tkinter as tk
from tkinter import messagebox
import sqlite3

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Application")

        # Connect to SQLite database
        self.conn = sqlite3.connect("database.db")
        self.cur = self.conn.cursor()

        # Create table if not exists
        self.create_table()

        # GUI Widgets
        self.create_widgets()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY,
                            name TEXT,
                            age INTEGER,
                            grade TEXT
                            )""")
        self.conn.commit()

    def create_widgets(self):
        # Labels and Entry Widgets
        self.label_name = tk.Label(self.root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entry_name = tk.Entry(self.root)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        self.label_age = tk.Label(self.root, text="Age:")
        self.label_age.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entry_age = tk.Entry(self.root)
        self.entry_age.grid(row=1, column=1, padx=5, pady=5)

        self.label_grade = tk.Label(self.root, text="Grade:")
        self.label_grade.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.entry_grade = tk.Entry(self.root)
        self.entry_grade.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.button_add = tk.Button(self.root, text="Add", command=self.add_student)
        self.button_add.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.button_show = tk.Button(self.root, text="Show All", command=self.show_students)
        self.button_show.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="we")

        self.button_custom_query = tk.Button(self.root, text="Custom Query", command=self.custom_query)
        self.button_custom_query.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="we")

    def add_student(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        grade = self.entry_grade.get()

        if name and age and grade:
            self.cur.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
            self.conn.commit()
            messagebox.showinfo("Success", "Student added successfully.")
        else:
            messagebox.showerror("Error", "Please fill all fields.")

    def show_students(self):
        self.cur.execute("SELECT * FROM students")
        students = self.cur.fetchall()

        if students:
            for student in students:
                print(student)  # Display in console for demonstration
        else:
            messagebox.showinfo("No Students", "No students found.")

    def custom_query(self):
        # Example: Custom query to get students with age greater than 20
        self.cur.execute("SELECT * FROM students WHERE age > ?", (20,))
        results = self.cur.fetchall()

        if results:
            for result in results:
                print(result)  # Display in console for demonstration
        else:
            messagebox.showinfo("No Results", "No results found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
