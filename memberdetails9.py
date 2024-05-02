import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import StringVar, Entry, DISABLED
import mysql.connector
from PIL import ImageTk, Image
import home_page

def main():
    Mydb = mysql.connector.connect(host="localhost",user="root",password="vivek",database="gym")
    cursor = Mydb.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS subscribers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, joindate DATE, subtype VARCHAR(255), days INT, fees FLOAT, packagesub INT)")
    Mydb.commit()

    # Function to present data on the treeview
    def update_func(rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    # Function to search the database based on the name
    def search_func():
        q2 = q.get()
        query = f"SELECT id, name, age, joindate, subtype, fees, days, packagesub FROM subscribers WHERE name LIKE '%{q2}%'"
        cursor.execute(query)
        rows = cursor.fetchall()
        update_func(rows)

    # Function to refresh the table after every update, search, or delete
    def clear_func():
        query = "SELECT id, name, age, joindate, subtype, fees, days, packagesub FROM subscribers"
        cursor.execute(query)
        rows = cursor.fetchall()
        update_func(rows)

    # Function to update the remaining days of the subscribers
    def update_customer():
        days = t4.get()
        id = t1.get()
        if messagebox.askyesno("Confirm Update", "Are you sure you want to update the days?"):
            query = "UPDATE subscribers SET days = %s WHERE id = %s"
            cursor.execute(query, (days, id))
            Mydb.commit()
            clear_func()

    # Function to cancel the subscription
    def delete_customer():
        id = t1.get()
        package_number = t3.get()
        days = t4.get()
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this user?"):
            query = "DELETE FROM subscribers WHERE id = %s"
            cursor.execute(query, (id,))
            Mydb.commit()
            clear_func()
            if package_number in ["1", "2", "3"]:
                if package_number == "1":
                    remaining = ((200 - int(days)) / 200) * 250
                elif package_number == "2":
                    remaining = ((500 - int(days)) / 500) * 625
                elif package_number == "3":
                    remaining = ((700 - int(days)) / 700) * 930
                messagebox.showinfo("Change", f"The customer should receive: {remaining} as a change for canceling")

    # Function to reward a certain package subscribers with additional days
    def reward():
        increase_days = simpledialog.askinteger("Reward Days", "Enter the number of days to reward")
        package_num = simpledialog.askinteger("Rewarded Package", "Enter the number of the package rewarded")
        if messagebox.askyesno("Confirm Update", "Are you sure you want to increase the days?"):
            query = "UPDATE subscribers SET days = days + %s WHERE packagesub = %s"
            cursor.execute(query, (increase_days, package_num))
            Mydb.commit()
            clear_func()

    # Exit to home page function
    def exit_func():
        subscribers.destroy()
        home_page.display_home()

    subscribers = tk.Tk()  # the form
    q = StringVar()  # made for use in search function
    t1, t2, t3, t4 = StringVar(), StringVar(), StringVar(), StringVar()

    subscribers.title('Subscribers Modifications')
    screenwidth = subscribers.winfo_screenwidth()
    screenheight = subscribers.winfo_screenheight()
    subscribers.geometry(f'{screenwidth}x{screenheight}+0+0')

    #-----------------------------------------------------------------------------
    img=Image.open("E:/self work/project/gym/iiiiii.png")
    img=img.resize((screenwidth,screenheight))
    img_tk=ImageTk.PhotoImage(img)
    imglbl=tk.Label(subscribers,image=img_tk)
    imglbl.place(x=0,y=0,relwidth=1,relheight=1)
    #-----------------------------------------------------------------------------

    f1=tk.Frame(subscribers,bg="blue")
    f2=tk.Frame(subscribers,bg="blue")

    trv = ttk.Treeview(subscribers, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="10", selectmode='browse')
    trv.pack(side=tk.LEFT)
    trv.place(x=0, y=0)

    trv.heading(1, text="ID")
    trv.heading(2, text="Name")
    trv.heading(3, text="Age")
    trv.heading(4, text="Join Date")
    trv.heading(5, text="Subscription Type")
    trv.heading(6, text="Days")
    trv.heading(7, text="Subscription Fees")
    trv.heading(8, text="Package Number")

    trv.column(1, width=100, anchor='center')
    trv.column(2, width=300)
    trv.column(3, width=100, anchor='center')
    trv.column(4, width=250)
    trv.column(5, width=150, anchor='center')
    trv.column(6, width=150, anchor='center')
    trv.column(7, width=150, anchor='center')
    trv.column(8, width=150, anchor='center')

    style = ttk.Style()
    style.configure('Treeview', font=('arial', 11), foreground='black', background='yellow')
    style.configure('Treeview.Heading', font=('Arial 12 bold'))

    cursor.execute("SELECT id, name, age, joindate, subtype, fees, days, packagesub FROM subscribers")
    rows = cursor.fetchall()
    update_func(rows)

    lbl = tk.Label(f1, text="Search",font='Arial 12 bold',foreground='white',background="blue")
    lbl.pack(side=tk.LEFT, padx=10)
    ent = tk.Entry(f1, textvariable=q)
    ent.pack(side=tk.LEFT, padx=6)
    btn = tk.Button(f1, text="Search",font='Arial 12 bold' ,background="yellow", command=search_func)
    btn.pack(side=tk.LEFT, padx=10)
    Cbtn = tk.Button(f1, text='Clear',font='Arial 12 bold', background="yellow", command=clear_func)
    Cbtn.pack(side=tk.LEFT, padx=10)


    lbl1 = tk.Label(f2, text="Customer ID",font='Arial 12 bold',foreground='white', background="blue")
    lbl1.grid(row=0, column=0, padx=5, pady=3)
    ent1 = tk.Entry(f2, textvariable=t1)
    ent1.grid(row=0, column=1, padx=5, pady=3)


    lbl2 = tk.Label(f2, text="Name",font='Arial 12 bold',foreground='white', background="blue")
    lbl2.grid(row=1, column=0, padx=5, pady=3)
    ent2 = tk.Entry(f2, textvariable=t2)
    ent2.grid(row=1, column=1, padx=5, pady=3)


    lbl3 = tk.Label(f2, text="Subscription Type", font='Arial 12 bold',foreground='white',background="blue")
    lbl3.grid(row=2, column=0, padx=5, pady=3)
    ent3 = tk.Entry(f2, textvariable=t3)
    ent3.grid(row=2, column=1, padx=5, pady=3)


    lbl4 = tk.Label(f2, text="Days", font='Arial 12 bold',foreground='white',background="blue")
    lbl4.grid(row=3, column=0, padx=5, pady=3)
    ent4 = tk.Entry(f2, textvariable=t4)
    ent4.grid(row=3, column=1, padx=5, pady=3)

    up_btn = tk.Button(f2, text="Update Days",font='Arial 12 bold', background="yellow", command=update_customer)
    add_btn = tk.Button(f2, text="Reward Days",font='Arial 12 bold' ,background="yellow", command=reward)
    delete_btn = tk.Button(f2, text="Cancel Subscription",font='Arial 12 bold', background="yellow", command=delete_customer)
    Exit = tk.Button(f2, text="Exit to Main Menu", font='Arial 12 bold',background="yellow", command=exit_func)

    add_btn.grid(row=4, column=0, padx=3, pady=3)
    up_btn.grid(row=4, column=1, padx=3, pady=3)
    delete_btn.grid(row=4, column=2, padx=3, pady=3)
    Exit.grid(row=4, column=3, padx=3, pady=3)

    f1.pack(side="left", padx=150, pady=300)
    f2.pack(side="right", padx=30, pady=50)

    subscribers.mainloop()

if __name__ == "__main__":
    main()
