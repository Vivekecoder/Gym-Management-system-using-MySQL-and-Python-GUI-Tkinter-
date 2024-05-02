from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

top = Tk()
top.geometry('1366x786')
top.title("Gym")

path = 'E:/self work/project/gym/log in.jpg'
img=ImageTk.PhotoImage(Image.open(path))
l5=Label(top,image=img)
l5.place(x=0,y=0)



def login():
    import pymysql as sql
    db = sql.connect(host="localhost", user="root", password="vivek", db="Gym")
    cur = db.cursor()
    cur.execute("select * from signupdetails where email=%s and password=%s", (eemail.get(), epassword.get()))
    row = cur.fetchone()
    if row == None:
        messagebox.showerror("error", "Invalid username and password")
    else:
        top.destroy()
        import home3


#function to move to sign up
def move():
    top.destroy()
    import signup1


#function to forget password
def forget():
    top.destroy()
    import forget_pass4


# Frame .....................................
DF1 = LabelFrame(top, text='Login', font=("Arial 20 bold"), fg='white', bd=2, bg='gray', width=330, height=786, relief='groove')
DF1.place(x=1010, y=0)

logwelcome = Label(DF1, text='Welcome Back', font=("Arial 20 bold"), bg='gray', bd=0, fg='white')
logwelcome.place(x=70, y=30)

# insert logo img
logoimg = Image.open('E:/self work/project/gym/logoresize.png')
logoimg_tk = ImageTk.PhotoImage(logoimg)
btnlogo = Button(DF1, compound='right', image=logoimg_tk, bd=0, bg='#CAA928')  # ,width=150,height=150
btnlogo.place(x=110, y=70)

# ....................... Label Data Frame ..............................
lemail = Label(DF1, text='Email/User', font=("Arial 13 bold"), bg='gray', bd=0, fg='white')
lemail.place(x=5, y=200)
eemail = Entry(DF1, width=22, font=("Arial 13 bold"))
eemail.place(x=110, y=200)

lpassword = Label(DF1, text='Password', font=("Arial 13 bold"), bg='gray', bd=0, fg='white')
lpassword.place(x=5, y=250)
epassword = Entry(DF1, width=22, show='*', font=("Arial 13 bold"))
epassword.place(x=110, y=250)
def show_password():
    if epassword.cget('show')=='*' :
        epassword.config(show='')
    else :
        epassword.config(show='*')


notacc = Label(DF1, text="for registration ",font=("Arial 13 bold"), bg='gray', bd=0, fg='white')
notacc.place(x=160, y=430)


# Button ................................................

showpassword=Checkbutton(DF1,text="Show password",command=show_password)
showpassword.place(x=110,y=280)
forgetpass = Button(DF1, text="Forget Password?", bg='orange', fg='white',font=("Arial 10 bold"),command=forget)
forgetpass.place(x=110, y=380)

login_img = PhotoImage(file='E:/self work/project/gym/login.png')
login_nav = Button(DF1, text='Login', compound='left', image=login_img, fg='white', bg='orange', font=("Arial 15 bold"), bd=0, padx=8, pady=8,command=login)
login_nav.place(x=120, y=310)

sign_img=PhotoImage(file='E:/self work/project/gym/sign up.png')
sign_nav=Button(DF1,text="click here",compound='left',image=sign_img,fg='white',bg='orange',font=("Arial 8 bold"),bd=0,padx=8,pady=8,command=move)
sign_nav.place(x=50,y=420)


top.config()
top.mainloop()