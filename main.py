from re import search
import tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
import os
import tkinter.messagebox as messagebox
from turtle import left


ElNajahSchool = tk.Tk()
ElNajahSchool.title("El Najah School")
ElNajahSchool.geometry("1024x768")
ElNajahSchool.attributes('-fullscreen', True)



menubar = tk.Menu(ElNajahSchool)
file_menu = tk.Menu(menubar, tearoff=0 )
file_menu.add_command(label="Exit", command=ElNajahSchool.quit)
menubar.add_cascade(label="File", menu=file_menu)
ElNajahSchool.config(menu=menubar)

label = tk.Label(ElNajahSchool, text="Welcome to El Najah School", font=("Arial", 24))
label.pack(pady=20)

frame = tk.Frame(ElNajahSchool)
frame.pack(pady=0, padx=20, fill='x')

left_half = tk.Frame(frame, width=480, height=60)
left_half.pack(side='left', fill='y', expand=True)
left_half.pack_propagate(False)

right_half = tk.Frame(frame, width=480, height=60)
right_half.pack(side='left', fill='y', expand=True)
right_half.pack_propagate(False)

def top_level_tap():
    top = tk.Toplevel(ElNajahSchool)
    top.title("New Student Registration")
    top.geometry("500x300")
    label = tk.Label(top,text="add new student", font=("Arial", 24))
    label.pack( pady=20) 
    frame = tk.Frame(top)
    frame.pack(pady=10, padx=20, fill='x')

    entry = tk.Entry(frame, font=("Arial", 18), justify='right')
    entry.pack(side='left', fill='x', expand=True)

    radio_var = tk.StringVar(value="pay")
    radio1 = tk.Radiobutton(frame, text="paid", variable=radio_var, value="paid")
    radio2 = tk.Radiobutton(frame, text="unpaid", variable=radio_var, value="unpaid")
    radio1.pack(side='left', padx=10, pady=10)
    radio2.pack(side='left', padx=10, pady=10)


left_button = tk.Button(left_half, text="add student", font=("Arial", 16), command=top_level_tap)
left_button.place(relx=0.5, rely=0.5, anchor="center")


def top_level_tap():
    top = tk.Toplevel()
    top.title("New group registration")
    top.geometry("500x300")
    label = tk.Label(top, text="add new group", font=("Arial", 24))
    label.pack(pady=20)

    frame = tk.Frame(top)
    frame.pack(pady=10, padx=20, fill='x')

    entry = tk.Entry(frame, font=("Arial", 18), justify='right')
    entry.pack(side='left', fill='x', expand=True)

    botton = tk.Button(frame, text="add group")
    botton.pack(side='right', padx=10)


right_button = tk.Button(right_half, text="add group", font=("Arial", 16), command=top_level_tap)
right_button.place(relx=0.5, rely=0.5, anchor="center")


# Search functionality
search_frame = tk.Frame(ElNajahSchool)
search_frame.pack(pady=10)

search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var, width=40, font=("Arial", 16), justify="right", bg="#969696", fg="#FFFFFF")
search_entry.pack(side="left", padx=5, expand=True )

search_button = tk.Button(search_frame, text="Search", command=search)
search_button.pack(side="left")


# Function to handle search
table_container = tk.Frame(ElNajahSchool)
table_container.pack(fill="x")  

button_row = tk.Frame(table_container)
button_row.grid(row=0, column=0, sticky="ew")

button_row.grid_columnconfigure(0, minsize=173)
button_row.grid_columnconfigure(1, minsize=372)
button_row.grid_columnconfigure(2, minsize=313)
button_row.grid_columnconfigure(3, minsize=160)

btn_id = tk.Button(button_row, text="ID", command=lambda: open_top("ID"))
btn_id.grid(row=0, column=0, sticky="ew")

btn_name = tk.Button(button_row, text="Name", command=lambda: open_top("Name"))
btn_name.grid(row=0, column=1, sticky="ew")

btn_group = tk.Button(button_row, text="Groups", command=lambda: open_top("Groups"))
btn_group.grid(row=0, column=2, sticky="ew")

btn_pay = tk.Button(button_row, text="Pay", command=lambda: open_top("Pay"))
btn_pay.grid(row=0, column=3, sticky="ew")



def open_top(column_name):
    top = tk.Toplevel()
    top.title(f"{column_name} Options")
    tk.Label(top, text=f"This is the {column_name} top window").pack(pady=10)

# Treeview setup
style = ttk.Style()
style.theme_use("default")


style.configure("Treeview",
    rowheight=30,
    font=("Arial", 12),
    bordercolor="#cccccc",
    borderwidth=1
)
style.configure("Treeview.Heading",
    font=("Arial", 12, "bold"),
    background="#e0e0e0",
    bordercolor="#cccccc",
    borderwidth=1
)

style.map('Treeview', background=[('selected', '#d0f0ff')])


columns = ("id", "name", "group", "pay")
tree = ttk.Treeview(ElNajahSchool, columns=columns, show="headings")

tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("group", text="Groups")
tree.heading("pay", text="Pay")

tree.column("id", anchor="center", width=80)
tree.column("name", anchor="center", width=280)
tree.column("group", anchor="center", width=220)
tree.column("pay", anchor="center", width=75)
tree.pack( fill="both", expand=True)


sample_students = [
    (1, "Alice Smith", "Group A", "Paid"),
    (2, "Bob Johnson", "Group B", "Unpaid"),
    (3, "Charlie Brown", "Group A", "Paid"),
    (4, "Diana Prince", "Group C", "Unpaid"),
    (8, "Hannah Montana", "Group B", "Paid"),
    (9, "Ian Malcolm", "Group C", "Unpaid"),
    (10, "Jane Doe", "Group A", "Paid"),
    (11, "Kevin Hart", "Group B", "Unpaid"),
    (12, "Laura Croft", "Group C", "Paid"),
    (13, "Mike Wazowski", "Group A", "Unpaid"),
    (14, "Nina Simone", "Group B", "Paid"),
    (15, "Oscar Wilde", "Group C", "Unpaid"),
    (16, "Paul Atreides", "Group A", "Paid"),
    (17, "Quinn Fabray", "Group B", "Unpaid"),
    (18, "Rachel Green", "Group C", "Paid"),
    (19, "Sam Winchester", "Group A", "Unpaid"),
    (20, "Tina Fey", "Group B", "Paid"),
    (21, "Uma Thurman", "Group C", "Unpaid"),
    (22, "Victor Frankenstein", "Group A", "Paid"),
    (23, "Wanda Maximoff", "Group B", "Unpaid"),
    (24, "Xander Harris", "Group C", "Paid"),
    (25, "Yara Shahidi", "Group A", "Unpaid"),
    (26, "Zoe Saldana", "Group B", "Paid")
]
for student in sample_students:
    tree.insert("", tk.END, values=student)


ElNajahSchool.mainloop()