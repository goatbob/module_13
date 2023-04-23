"""
program: database_GUI.py
author: kyle godwin
last date modified: 18 april 2023

UI to connect to person and student databases,
add new rows, and return databases
"""
import tkinter as tk
import connect_to_database as db


def start_buttons():
    """
    sets add person and student buttons to normal
    """
    addperson_button.config(state="normal")
    addstudent_button.config(state="normal")


def get_id():
    """
    :return: id from person table
    """
    with db.conn:
        persons = db.select_all_persons(db.conn)
        for row in persons:
            if row[1] == firstname.get() and row[2] == lastname.get():
                return row[0]


def person_output():
    """
    :return: person table in output box
    """
    with db.conn:
        persons = db.select_all_persons(db.conn)
        for row in persons:
            output_box.insert(tk.END, row)


def student_output():
    """
    :return: student table in output box
    """
    with db.conn:
        students = db.select_all_students(db.conn)
        for row in students:
            output_box.insert(tk.END, row)


win = tk.Tk()
win.title("Database creation and input")
win.geometry("500x800")

# initialize variables
firstname = tk.StringVar()
lastname = tk.StringVar()
major = tk.StringVar()
startdate = tk.StringVar()


create_button = tk.Button(win, text="Create Database & Table", command=lambda: [start_buttons(),
                                                                                db.create_tables("pydb.db")])
create_button.pack()

firstname_label = tk.Label(win, text="Enter first name:")
firstname_label.pack()

firstname_input = tk.Entry(win, textvariable=firstname, width=25, bg="light cyan")
firstname_input.pack()

lastname_label = tk.Label(win, text="Enter last name:")
lastname_label.pack()

lastname_input = tk.Entry(win, textvariable=lastname, width=25, bg="light cyan")
lastname_input.pack()

# add person to database using first and last name input
addperson_button = tk.Button(win, text="Add Person", state="disabled", command=lambda:
                             db.create_person(db.conn, (firstname.get(), lastname.get())))
addperson_button.pack()

major_label = tk.Label(win, text="Enter major:")
major_label.pack()

major_input = tk.Entry(win, textvariable=major, width=25, bg="light cyan")
major_input.pack()

startdate_label = tk.Label(win, text="Enter start date:")
startdate_label.pack()

startdate_input = tk.Entry(win, textvariable=startdate, width=25, bg="light cyan")
startdate_input.pack()

# add student to database using major and start date input
addstudent_button = tk.Button(win, text="Add Student", state="disabled", command=lambda:
                              db.create_student(db.conn, (get_id(), major.get(), startdate.get())))
addstudent_button.pack()

# output box to display tables
output_box = tk.Text(win, width=25, bg="light cyan")
output_box.pack()

# displays person table in output box
viewpersontable_button = tk.Button(win, text="View Person Table", state="normal", command=person_output)
viewpersontable_button.pack()

# displays student table in output box
viewstudenttable_button = tk.Button(win, text="View Student Table", state="normal", command=student_output)
viewstudenttable_button.pack()

# exit button
exit_button = tk.Button(win, text='Exit', width=10, command=lambda: [db.conn.close(), win.destroy()])
exit_button.pack()


win.mainloop()
