from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk

top = Tk()
top.geometry("1366x786")

# .........  Background Image..........................
path = 'E:/self work/project/gym/sign2.jpg'
img = ImageTk.PhotoImage(Image.open(path))
l5 = Label(top, image=img)
l5.pack()

top.title("Registration form")

# Data insert function in the sql
def Registration():
    k1 = efName.get()
    k2 = elname.get()
    k3 = eage.get()
    k4 = egender.get()
    k5 = eemail.get()
    k6 = epassword.get()
    k7 = countryc.get()

    import pymysql as sql
    db = sql.connect(host="localhost", user="root", password="vivek", db="Gym")
    cur = db.cursor()
    s = "insert into signupdetails values ('%s','%s','%s','%s','%s','%s','%s')" % (k1, k2, k3, k4, k5, k6, k7)

    result = cur.execute(s)
    if result > 0:
        messagebox.showinfo("Result", "Record inserted successfully")
    else:
        messagebox.showinfo("Result", "Record is not inserted")
    db.commit()

def Clear():
        efName.delete(0, "end")
        elname.delete(0, "end")
        egender.delete(0, "end")
        eage.delete(0, "end")
        eemail.delete(0, "end")
        epassword.delete(0, "end")
        countryc.delete(0, "end")

def exit():
    if messagebox.askokcancel("Exit","Do you want to exit"):
        top.destroy()

def login():
    top.destroy()
    import login2


DF1 = LabelFrame(top, text='sign up', font=("Arial 20 bold"), fg='white', bd=2, bg='black', width=370, height=680, relief='groove')
DF1.place(x=100, y=20)

# ....................... Label Data Frame ..............................
lfName = Label(DF1, text='First_Name', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lfName.place(x=5, y=100)
efName = Entry(DF1, width=25, font=("Arial 13 bold"))
efName.place(x=130, y=105)

llname = Label(DF1, text='Last_Name', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
llname.place(x=5, y=150)
elname = Entry(DF1, width=25, font=("Arial 13 bold"))
elname.place(x=130, y=155)

lage = Label(DF1, text='Age', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lage.place(x=5, y=200)
eage = Entry(DF1, width=25, font=("Arial 13 bold"))
eage.place(x=130, y=205)

lgender = Label(DF1, text='Gender', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lgender.place(x=5, y=250)
egender = ttk.Combobox(DF1, values=['Male', 'Female', 'Other'], font='Arial 13', state='readonly')
egender.place(x=130, y=252)
egender.set('Select Gender ')

lemail = Label(DF1, text='Email', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lemail.place(x=5, y=300)
eemail = Entry(DF1, width=25, font=("Arial 13 bold"))
eemail.place(x=130, y=300)

lpassword = Label(DF1, text='Password', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lpassword.place(x=5, y=350)
epassword = Entry(DF1, width=25, show='*', font=("Arial 13 bold"))
epassword.place(x=130, y=350)

lcountry = Label(DF1, text='Country', font=("Arial 16 bold"), bg='black', bd=0, fg='white')
lcountry.place(x=5, y=400)
countryc = ttk.Combobox(DF1, values=['Egypt', 'England', 'India', 'Nepal', 'Germany', 'Morocco', 'Algeria', 'Palestine', 'Switzerland', 'America', 'Argentina', 'Brazil'], font='Arial 13', state='readonly')
countryc.place(x=130, y=400)
countryc.set("Select Country")

savebtn = Button(DF1, text='Save', width=10, height=2, font='arial 12 bold', bg='lightgreen', command=Registration)
savebtn.place(x=50, y=450)
resetbtn = Button(DF1, text='Reset', width=22, height=2, font='arial 12 bold', bg='lightpink',command=Clear)
resetbtn.place(x=60, y=590)
exitbtn = Button(DF1, text='Exit', width=22, height=2, font='arial 12 bold', bg='grey', command=exit)
exitbtn.place(x=60,y=520)
loginbutton = Button(DF1, text="Login", width=10, height=2, font='arial 12 bold', bg='lightgreen',command=login)
loginbutton.place(x=200, y=450)


top.config()
top.mainloop()
