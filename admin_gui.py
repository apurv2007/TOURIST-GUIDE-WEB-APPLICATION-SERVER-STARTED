"""
Tkinter Admin GUI Application
Provides a Desktop GUI management window for the Tourist Guide Website.
Strictly maps to CE0525 (Unit III: GUI Programming - Tkinter, Dropdowns, Images, Controls).
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox
import csv

from utils import load_destinations, load_guides, load_bookings, DATA_DIR

class TouristAdminGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Indus Tourist Guide - Admin Management Tool (Tkinter)")
        self.root.geometry("850x600")
        self.root.configure(bg="#f4f6f9")

        # Title Banner
        title_frame = tk.Frame(self.root, bg="#2b5c8f", pady=10)
        title_frame.pack(fill=tk.X)
        title_label = tk.Label(
            title_frame, 
            text="INDUS TOURIST GUIDE MANAGEMENT SYSTEM", 
            font=("Helvetica", 16, "bold"), 
            fg="white", 
            bg="#2b5c8f"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame, 
            text="Course Code: CE0525 | Desktop Admin Interface (Tkinter)", 
            font=("Helvetica", 10, "italic"), 
            fg="#e0e8f5", 
            bg="#2b5c8f"
        )
        subtitle_label.pack()

        # Create Notebook Tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 1: View Destinations
        self.tab_destinations = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_destinations, text="Destinations Catalog")
        self.build_destinations_tab()

        # Tab 2: Add New Destination Form
        self.tab_add_spot = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_add_spot, text="Add Destination")
        self.build_add_spot_tab()

        # Tab 3: Currency & Fare Calculator Tool
        self.tab_calculator = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_calculator, text="Tour Fare Calculator")
        self.build_calculator_tab()

        # Tab 4: Course Syllabus Mapping
        self.tab_syllabus = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_syllabus, text="Syllabus Mapping (CE0525)")
        self.build_syllabus_tab()

    def build_destinations_tab(self):
        # Dropdown filter city/category
        filter_frame = tk.Frame(self.tab_destinations, pady=5)
        filter_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(filter_frame, text="Filter by Category:", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All", "Heritage", "Nature", "Spiritual", "Beach", "Adventure", "Modern", "Wildlife", "Culture"]
        dropdown = ttk.OptionMenu(filter_frame, self.category_var, "All", *categories, command=self.refresh_destinations)
        dropdown.pack(side=tk.LEFT, padx=5)

        btn_refresh = tk.Button(filter_frame, text="Refresh List", command=self.refresh_destinations, bg="#2b5c8f", fg="white")
        btn_refresh.pack(side=tk.LEFT, padx=10)

        # Treeview Table
        columns = ("ID", "Name", "Location", "Category", "Price", "Rating", "State")
        self.tree = ttk.Treeview(self.tab_destinations, columns=columns, show="headings", height=15)
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=110, anchor=tk.CENTER)

        self.tree.column("Name", width=180, anchor=tk.W)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.refresh_destinations()

    def refresh_destinations(self, *args):
        # Clear existing
        for item in self.tree.get_children():
            self.tree.delete(item)

        spots = load_destinations()
        selected_cat = self.category_var.get()

        for s in spots:
            if selected_cat == "All" or s.category.lower() == selected_cat.lower():
                self.tree.insert("", tk.END, values=(s.spot_id, s.name, s.location, s.category, f"₹{s.price:.0f}", s.rating, s.state))

    def build_add_spot_tab(self):
        form_frame = tk.Frame(self.tab_add_spot, padx=20, pady=20)
        form_frame.pack(fill=tk.BOTH, expand=True)

        labels = ["Destination Name:", "Location / City:", "Category:", "Price (₹):", "Rating (0-5):", "Duration (Days):", "State:"]
        self.entries = {}

        for i, text in enumerate(labels):
            tk.Label(form_frame, text=text, font=("Helvetica", 10, "bold")).grid(row=i, column=0, sticky=tk.W, pady=5)
            entry = tk.Entry(form_frame, width=40)
            entry.grid(row=i, column=1, pady=5, padx=10)
            self.entries[text] = entry

        # Description text area
        tk.Label(form_frame, text="Description:", font=("Helvetica", 10, "bold")).grid(row=len(labels), column=0, sticky=tk.NW, pady=5)
        self.txt_desc = tk.Text(form_frame, width=40, height=4)
        self.txt_desc.grid(row=len(labels), column=1, pady=5, padx=10)

        btn_save = tk.Button(form_frame, text="Save Destination", command=self.save_new_destination, bg="#2e8b57", fg="white", font=("Helvetica", 11, "bold"), padx=10, pady=5)
        btn_save.grid(row=len(labels)+1, column=1, sticky=tk.W, pady=15)

    def save_new_destination(self):
        try:
            name = self.entries["Destination Name:"].get().strip()
            location = self.entries["Location / City:"].get().strip()
            category = self.entries["Category:"].get().strip()
            price = float(self.entries["Price (₹):"].get().strip())
            rating = float(self.entries["Rating (0-5):"].get().strip())
            duration = int(self.entries["Duration (Days):"].get().strip())
            state = self.entries["State:"].get().strip()
            desc = self.txt_desc.get("1.0", tk.END).strip()

            if not name or not location:
                messagebox.showerror("Error", "Name and Location are required.")
                return

            spots = load_destinations()
            new_id = max([s.spot_id for s in spots]) + 1 if spots else 1

            dest_path = os.path.join(DATA_DIR, "destinations.csv")
            with open(dest_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([new_id, name, location, category, price, rating, desc, duration, state])

            messagebox.showinfo("Success", f"Destination '{name}' saved successfully!")
            self.refresh_destinations()
        except Exception as e:
            messagebox.showerror("Validation Error", str(e))

    def build_calculator_tab(self):
        calc_frame = tk.Frame(self.tab_calculator, padx=30, pady=30)
        calc_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(calc_frame, text="Quick Tour Price Calculator", font=("Helvetica", 14, "bold"), fg="#2b5c8f").pack(anchor=tk.W, pady=10)

        f_inputs = tk.Frame(calc_frame)
        f_inputs.pack(anchor=tk.W, pady=10)

        tk.Label(f_inputs, text="Base Price per Person (₹):", font=("Helvetica", 10)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.ent_base = tk.Entry(f_inputs, width=15)
        self.ent_base.insert(0, "2000")
        self.ent_base.grid(row=0, column=1, padx=10)

        tk.Label(f_inputs, text="Number of Persons:", font=("Helvetica", 10)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.ent_persons = tk.Entry(f_inputs, width=15)
        self.ent_persons.insert(0, "2")
        self.ent_persons.grid(row=1, column=1, padx=10)

        tk.Label(f_inputs, text="Guide Fee per Day (₹):", font=("Helvetica", 10)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.ent_guide = tk.Entry(f_inputs, width=15)
        self.ent_guide.insert(0, "800")
        self.ent_guide.grid(row=2, column=1, padx=10)

        btn_calc = tk.Button(calc_frame, text="Calculate Total Package Cost", command=self.calculate_total, bg="#d97736", fg="white", font=("Helvetica", 10, "bold"))
        btn_calc.pack(anchor=tk.W, pady=15)

        self.lbl_calc_result = tk.Label(calc_frame, text="Total Estimate: ₹0.00", font=("Helvetica", 12, "bold"), fg="#2e8b57")
        self.lbl_calc_result.pack(anchor=tk.W, pady=5)

    def calculate_total(self):
        try:
            base = float(self.ent_base.get())
            persons = int(self.ent_persons.get())
            guide = float(self.ent_guide.get())

            # Math computation
            subtotal = (base * persons) + guide
            gst = subtotal * 0.05  # 5% GST
            total = subtotal + gst

            self.lbl_calc_result.config(text=f"Total Estimate (incl. 5% GST): ₹{total:,.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values.")

    def build_syllabus_tab(self):
        s_frame = tk.Frame(self.tab_syllabus, padx=15, pady=15)
        s_frame.pack(fill=tk.BOTH, expand=True)

        txt_info = tk.Text(s_frame, font=("Consolas", 10), wrap=tk.WORD)
        txt_info.pack(fill=tk.BOTH, expand=True)

        syllabus_text = """
================================================================================
COURSE SYLLABUS COMPLIANCE VERIFICATION (CE0525)
Course: Programming for Scientific Computing (Python) | Semester V
================================================================================

[UNIT I]: Basic elements, Branching, Looping, Functions, Recursion, Global variables,
         Modules, File Handling, Structured Objects, Mutability (Lists, Tuples, Dicts),
         Higher-Order Functions (lambda, map, filter).
         => Implemented in: models.py, utils.py, data_initializer.py, app.py

[UNIT II]: Object-Oriented Programming (Classes, Encapsulation, Information Hiding),
          Inheritance (LocalGuide, AgencyGuide), Method Overriding,
          Data Structures (Singly Linked List for Itineraries),
          Searching (Linear & Binary Search), Sorting (Selection & Merge Sort),
          Regular Expressions (re for email/phone/date), Multithreading (threading.Thread).
          => Implemented in: models.py, utils.py

[UNIT III]: Graphics & GUI Programming (Tkinter GUI window, OptionMenu dropdown, 
           Treeview table, Entry forms, Messagebox, Canvas), Array computing & Curve Plotting
           (NumPy, SciPy, Matplotlib / PyLab bar & pie charts).
           => Implemented in: admin_gui.py, utils.py

[UNIT IV]: Python Pandas (Data alignment, aggregation, summarization, describe()),
          Basics of Web Development (Framework: Flask server & views).
          => Implemented in: utils.py, app.py
================================================================================
"""
        txt_info.insert(tk.END, syllabus_text)
        txt_info.config(state=tk.DISABLED)

def run_gui():
    root = tk.Tk()
    app = TouristAdminGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
