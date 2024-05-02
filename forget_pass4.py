import re
import tkinter as tk
from tkinter import messagebox
import mysql.connector

top = tk.Tk()
top.title("Check Row by Email")
top.geometry('1366x786')


def check_row():
    Email = Email_entry.get()
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  # format Email
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="vivek", db="Gym")
        cursor = connection.cursor()
        query = "SELECT * FROM signupdetails WHERE Email = %s"
        cursor.execute(query, (Email,))
        row = cursor.fetchone()

        if len(Email) == 0:
            messagebox.showerror('Error', "Enter your Email")
        if (re.fullmatch(regex, Email)):
            messagebox.showinfo("Row Found",
                                f"First_Name: {row[0]}\nLast_Name: {row[1]}\nEmail:{row[4]}\nPassword:{row[5]}")
            print("Row Found", f"Row with Email {Email} found:\n{row}")

        elif len(Email) > 0:
            Email = "not"
            messagebox.showerror('Error', "Invalid Email")

        connection.close()
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error connecting to MySQL: {error}")


Email_label = tk.Label(top, text="Enter Email:", font="Arial 15 bold", bg='yellow', bd=0, fg='black')
Email_label.place(x=500, y=120)
Email_entry = tk.Entry(top, width=25, font="Arial 15 bold")
Email_entry.place(x=620, y=120)

check_button = tk.Button(top, text="Check Row", fg="green", font="Arial 20 bold", bg='yellow', command=check_row)
check_button.place(x=600, y=200)

top.mainloop()
