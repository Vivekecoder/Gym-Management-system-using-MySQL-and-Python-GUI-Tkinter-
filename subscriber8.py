import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
import mysql.connector

root = tk.Tk()
root.title("subscribers")

w = 1200
h = 600
x = 100
y = 50

root.geometry(f"{w}x{h}+{x}+{y}")

img = Image.open("E:/self work/project/gym/gym.jpg")
img = img.resize((1200, 600))
img_tk = ImageTk.PhotoImage(img)
imglbl = tk.Label(root, image=img_tk)
imglbl.pack()
def fromtarek():
    conn = mysql.connector.connect(host="localhost", user="root", password="vivek", db="Gym")
    cur = conn.cursor()

    # Create subscribers table if not exists
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        joindate VARCHAR(255),
        subtype VARCHAR(255),
        fees INT,
        days FLOAT,
        packagesub INT
    )
    """)
    conn.commit()

    def submit():
        choice = v2_rbtn.get()
        if choice == 1:
            tex = "monthly"
        else:
            tex = "premium"

        def exit():
            root.destroy()

        cur.execute("""
        INSERT INTO subscribers (name, age, joindate, subtype, fees, days, packagesub)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (en2.get(), int(en3.get()), en4.get(), tex, int(en7.get()), float(en5.get()), int(combo3.get())))

        conn.commit()

        messagebox.showinfo("Success", "Data inserted successfully.")

        en1.delete(0, tk.END)
        en2.delete(0, tk.END)
        en3.delete(0, tk.END)
        en4.delete(0, tk.END)
        en5.delete(0, tk.END)
        en7.delete(0, tk.END)

    DF1=tk.LabelFrame(root,width=300,height=300,bg='blue')
    DF1.place(x=50,y=150)

    lb1 = Label(DF1, text='ID:', font=('arial', 12, 'bold'),background='blue',foreground='yellow')
    lb1.place(x=10,y=30)
    en1 = Entry(DF1,width=30)
    en1.place(x=90,y=30)

    lb2 = Label(DF1, text='Name:', font=('arial', 12, 'bold'),background='blue',foreground='yellow')
    lb2.place(x=10,y=80)
    en2 = Entry(DF1,width=30)
    en2.place(x=90,y=80)

    lb3 = Label(DF1, text='Age:', font=('arial', 12, 'bold'), background="blue",foreground='yellow')
    lb3.place(x=10,y=130)
    en3 = Entry(DF1,width=30)
    en3.place(x=90,y=130)

    lb4 = Label(DF1, text='Join-date:', font=('arial', 12, 'bold'),  background="blue",foreground='yellow')
    lb4.place(x=10,y=180)
    en4 = Entry(DF1,width=30)
    en4.place(x=90,y=180)

    lb5 = Label(DF1, text='Fees:', font=('arial', 12, 'bold'), background="blue",foreground='yellow')
    lb5.place(x=10,y=230)
    en5 = Entry(DF1,width=30)
    en5.place(x=90,y=230)

    lb7 = Label(DF1, text='Days:', font=('arial', 12, 'bold'), background="blue",foreground='yellow')
    lb7.place(x=10,y=270)
    en7 = Entry(DF1,width=30)
    en7.place(x=90,y=270)

    # Data frame 2...................................................
    DF2 = tk.LabelFrame(root, width=300, height=300, bg='blue')
    DF2.place(x=815, y=150)


    v2_rbtn = tk.IntVar()
    v2_rbtn.set(1)

    rbtn3 = tk.Radiobutton(DF2, text='monthly',font='Arail 15 bold' ,value=1, variable=v2_rbtn,background='blue',foreground='black')
    rbtn3.place(x=10,y=50)
    rbtn4 = tk.Radiobutton(DF2, text='premium',font="Arial 15 bold", value=2, variable=v2_rbtn,background='blue',foreground='black')
    rbtn4.place(x=150,y=50)


    lb6 = Label(DF2, text='Package:', font=('arial', 12, 'bold'), background="blue",foreground='yellow')
    lb6.place(x=10,y=90)
    package_days = [0, 1, 2, 3]
    p_var = tk.IntVar()
    p_var.set(package_days[0])
    combo3 = Combobox(DF2, values=package_days, state='readonly', textvariable=p_var)
    combo3.place(x=100, y=90)


    btn2 = tk.Button(DF2, text='Add', font=('arial', 20, 'bold'), bg="yellow", fg="black", padx=50, pady=10, command=submit)
    btn2.place(x=50,y=130)

    btn3 = tk.Button(DF2, text='Exit', font=('arial', 20, 'bold'), bg="yellow", fg="black", padx=50, pady=10, command=root.destroy)
    btn3.place(x=50,y=210)





    root.mainloop()

if __name__ == "__main__":
    fromtarek()
