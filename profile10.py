from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from tkinter.ttk import Combobox
import passlib #encript password
import re


root=Tk()
root.geometry('1366x786')
root.title("Gym")

#insert main picture
mainimg=Image.open('E:/self work/project/gym/pro.jpg')
mainimg_tk=ImageTk.PhotoImage(mainimg)
btn=Button(root,compound='left',image=mainimg_tk)
btn.place(x=0,y=0)

#make profile
navprofile=LabelFrame(root,text='Your Profile',font='Arial 18 bold',fg='white',bd=2,bg='black',width=340,height=768,relief='groove')
navprofile.place(x=1000,y=5)
def exit():
    root.destroy()

def showimg():
    global filename
    global img
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='select img file',filetypes=(('JPG File','*.jpg'),('PNG File','*.png'),('ALL File','*.txt')))
    img=(Image.open(filename))
    resizeimg=img.resize((200,200))
    photo2=ImageTk.PhotoImage(resizeimg)
    lbl.config(image=photo2)
    lbl.image=photo2
f=Frame(root,bg='black',width=193,height=190,relief='groove')
f.place(x=1079,y=70)
imgprofile=PhotoImage(file='E:/self work/project/gym/upload photo.png')
lbl=Label(f,image=imgprofile)
lbl.place(x=0,y=0)

# label

lblnameprfile=Label(root,text='Name:',font='arial 10 bold',bg='black',bd=0,fg='white')
lblnameprfile.place(x=1039,y=380)
lblageprofile=Label(root,text='age:',font='arial 10 bold',bg='black',bd=0,fg='white')
lblageprofile.place(x=1039,y=430)
lblemailprofile=Label(root,text='Email:',font='arial 10 bold',bg='black',bd=0,fg='white')
lblemailprofile.place(x=1039,y=480)
lblpassprofile=Label(root,text='Password:',font='arial 10 bold',bg='black',bd=0,fg='white')
lblpassprofile.place(x=1039,y=530)
lblchangepassprofile=Label(root,text='Change Password',font='arial 16 bold',bg='lightblue',bd=0,fg='black',width=19,height=2)
lblchangepassprofile.place(x=1049,y=575)

#button
exitbtnprofile=Button(root,text='Exit',width=19,height=2,font='arial 12 bold',bg='grey',command=exit)
exitbtnprofile.place(x=1074,y=640)
uploadbtn=Button(root,text='Upload',width=19,height=2,font='arial 12 bold',bg='lightblue',command=showimg)
uploadbtn.place(x=1079,y=300)




root.mainloop()