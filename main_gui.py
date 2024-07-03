import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class TaxiServiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Call Service Center")
        self.root.configure(bg="#F0F0F0")

        # Connect to SQLite database
        self.conn = sqlite3.connect('taxi.db')
        self.cursor = self.conn.cursor()

        # Page 1: Select Table
        self.page1 = tk.Frame(root, bg="#F0F0F0")
        self.page1.grid(row=0, column=0, padx=10, pady=10)
        self.create_table_buttons()

        # Page 2: Display Details
        self.page2 = tk.Frame(root, bg="#F0F0F0")
        self.table_label = tk.Label(self.page2, text="Selected Table: ", bg="#F0F0F0", font=("Arial", 12, "bold"))
        self.table_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.tree = ttk.Treeview(self.page2)
        self.tree.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
        self.scrollbar = ttk.Scrollbar(self.page2, orient="vertical", command=self.tree.yview)
        self.scrollbar.grid(row=1, column=2, sticky='ns')
        self.tree.configure(yscrollcommand=self.scrollbar.set)
        self.create_text_box()
        self.back_button = tk.Button(self.page2, text="Back", command=self.show_page1, bg="#FF5733", fg="white", font=("Arial", 10, "bold"), padx=10)
        self.back_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Current page
        self.current_page = None

    def create_text_box(self):
        self.result_text = tk.Text(self.page2, height=4, width=30, bg="#FFFFFF", font=("Arial", 10))
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

    def create_table_buttons(self):
        # Get table names from the database
        tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        for i, table in enumerate(tables):
            btn = tk.Button(self.page1, text=table[0], command=lambda table=table[0]: self.show_page2(table), bg="#2E86C1", fg="white", font=("Arial", 10, "bold"), padx=10)
            btn.grid(row=i, column=0, padx=5, pady=5, sticky="ew")

    def show_page1(self):
        self.page2.grid_forget()
        self.page1.grid(row=0, column=0)

    def show_page2(self, table):
        self.current_table = table
        self.table_label.config(text=f"Selected Table: {table}")
        self.page1.grid_forget()
        self.page2.grid(row=0, column=0)
        self.display_table_data(table)
        self.create_attribute_buttons()

    def display_table_data(self, table_name):
        try:
            # Clear existing data
            self.tree.delete(*self.tree.get_children())

            # Get column names from the database
            columns = self.get_columns(table_name)
            self.tree["columns"] = columns
            for col in columns:
                self.tree.heading(col, text=col)

            # Get data from the database
            data = self.cursor.execute(f"SELECT * FROM {table_name}").fetchall()
            for row in data:
                self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def get_columns(self, table_name):
        columns = self.cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
        return [col[1] for col in columns]

    def create_attribute_buttons(self):
        attributes = self.get_columns(self.current_table)
        for i, attr in enumerate(attributes):
            btn = tk.Button(self.page2, text=attr, command=lambda attr=attr: self.show_operation_buttons(attr), bg="#2E86C1", fg="white", font=("Arial", 10, "bold"), padx=10)
            btn.grid(row=4, column=i, padx=5, pady=5, sticky="ew")

    def show_operation_buttons(self, attribute):
        operations = ["Min", "Max", "Sum", "Count", "Average"]
        for i, op in enumerate(operations):
            btn = tk.Button(self.page2, text=op, command=lambda op=op:self.calculate_operation(attribute, op), bg="#FF5733", fg="white", font=("Arial", 10, "bold"), padx=10)
            btn.grid(row=5, column=i, padx=5, pady=5, sticky="ew")
    def calculate_operation(self, attribute, operation):
        try:
            result = self.get_operation_result(attribute, operation)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"{operation} of {attribute} is: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while performing the operation: {str(e)}")

    def get_operation_result(self, attribute, operation):
        try:
            if operation == "Min":
                query = f"SELECT MIN({attribute}) FROM {self.current_table}"
            elif operation == "Max":
                query = f"SELECT MAX({attribute}) FROM {self.current_table}"
            elif operation == "Sum":
                query = f"SELECT SUM({attribute}) FROM {self.current_table}"
            elif operation == "Count":
                query = f"SELECT COUNT({attribute}) FROM {self.current_table}"
            elif operation == "Average":
                query = f"SELECT AVG({attribute}) FROM {self.current_table}"

            # Execute the query and fetch
            result = self.cursor.execute(query).fetchone()[0]
            return result
        except Exception as e:
            raise e


root = tk.Tk()
app = TaxiServiceGUI(root)
root.mainloop()
