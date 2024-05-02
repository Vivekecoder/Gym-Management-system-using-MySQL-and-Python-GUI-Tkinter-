from tkinter import *
from PIL import Image, ImageTk

top = Tk()
top.geometry('1366x786')
top.title("Home")

# insert main picture
path = 'E:/self work/project/gym/mainimg.jpg'
img=ImageTk.PhotoImage(Image.open(path))
l5=Label(top,image=img)
l5.pack()

def home():
    top.destroy()
    import home3

def aboutgym():
    top.destroy()
    import about_gym5

def databases():
    top.destroy()
    import database6

def buyproduct():
    top.destroy()
    import buyproduct7

def subscriber():
    top.destroy()
    import subscriber8

def memberdetails():
    top.destroy()
    import memberdetails9

def profile():
    top.destroy()
    import profile10



# right side
lblri = Label(top, bg='gold', height=776, width=146)
lblri.place(x=1200, y=0)
lblri1 = Label(top, text='Golds Gym', font=("Times", "24", "bold italic"), fg='white', bd=0, bg='#CAA928')
lblri1.place(x=1202, y=150)


# insert logo img
logoimg = Image.open('E:/self work/project/gym/logoresize.png')
logoimg_tk = ImageTk.PhotoImage(logoimg)
btnlogo = Button(top, compound='right', image=logoimg_tk, bd=0, bg='#CAA928')
btnlogo.place(x=1217, y=250)


# features of gold gym
lge = Label(top, text='Group Exercise', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lge.place(x=1210, y=400)

lpt = Label(top, text='Personal Training', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lpt.place(x=1202, y=440)

lpools = Label(top, text='Pools', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lpools.place(x=1250, y=480)

lce = Label(top, text='Cardio Equipment', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lce.place(x=1202, y=520)

lcc = Label(top, text='Cardio Cinema', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lcc.place(x=1220, y=560)

lfw = Label(top, text='Free Weights.', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lfw.place(x=1220, y=600)

lgc = Label(top, text='Group Cycle.', bg='yellow', fg='black', font=('Arial', "13", "bold"))
lgc.place(x=1225, y=640)

# create navigator
nav = LabelFrame(top, text='Navigator', font=20, bg='yellow', fg='black', bd=2, width=1366, height=100,relief='groove')
nav.place(x=0, y=0)

# create buttons
H = PhotoImage(file='E:/self work/project/gym/home.png')
home = Button(top, text='Home', compound='left', highlightcolor='black', image=H,fg='black', bg='yellow', font=('Arial', "13", "bold"), bd=0, padx=8, pady=8,command=home)
home.place(x=50, y=33)

SS = PhotoImage(file='E:/self work/project/gym/services.png')
bss = Button(top, text='Subscriber services', compound='left', image=SS,fg='black', bg='yellow',font=('Arial', "13", "bold"), bd=0, padx=3, pady=8,command=memberdetails)
bss.place(x=150, y=33)

ANP = PhotoImage(file='E:/self work/project/gym/add.png')
baanp= Button(top, text='Add a new package', compound='left', image=ANP,fg='black', bg='yellow',font=('Arial', "13", "bold"), bd=0, padx=3, pady=8,command=subscriber)
baanp.place(x=400, y=33)

gabout = PhotoImage(file='E:/self work/project/gym/about.png')
bab = Button(top, text='About', compound='left', image=gabout,fg='black', bg='yellow',font=('Arial', "13", "bold"), bd=0, padx=8, pady=8,command=aboutgym)
bab.place(x=610, y=33)

gbp = PhotoImage(file='E:/self work/project/gym/buy.png')
bbp = Button(top, text='buy products', compound='left', image=gbp,fg='black',bg='yellow', font=('Arial', "13", "bold"), bd=0, padx=8, pady=8,command=buyproduct)
bbp.place(x=720, y=33)

gym5_img=PhotoImage(file='E:/self work/project/gym/gym5.png')
btn5_nav=Button(top,text='Sports Sets',compound='left',image=gym5_img,fg='black', bg='yellow',font=('Arial',"13", "bold"),bd=0,padx=8,pady=8)
btn5_nav.place(x=900,y=33)


#button login
"""
login_img=PhotoImage(file='E:/self work/project/gym/login.png')
login_nav=Button(top,text='Login',compound='left',image=login_img,fg='white', bg='yellow',font=('',"13", "bold"),bd=0,padx=8,pady=8)
login_nav.place(x=1050,y=33)

#button sign up
sign_img=PhotoImage(file='E:/self work/project/gym/sign up.png')
sign_nav=Button(top,text='Sign Up',compound='left',image=sign_img,fg='black', bg='yellow',font=('',"13", "bold"),bd=0,padx=8,pady=8)
sign_nav.place(x=1150,y=33)
"""

# button profile
profile_img=PhotoImage(file='E:/self work/project/gym/profile.png')
btn6_nav=Button(top,text='My Profile',compound='left',image=profile_img, bg='yellow',fg='black',font=18,bd=0,padx=8,pady=8,command=profile)
btn6_nav.place(x=1200,y=33)


top.config()
top.mainloop()
