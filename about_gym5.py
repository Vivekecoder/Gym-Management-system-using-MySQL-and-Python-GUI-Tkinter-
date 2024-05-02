from tkinter import *
from PIL import Image, ImageTk


top = Tk()
top.title("About Us")
top.geometry('1366x786')


def exit_func():
    top.destroy()
    import home3


about = LabelFrame(top,bg='#FFB100')
about.pack()


icon = Image.open('E:/self work/project/gym/5eb3cb4bc8c459000443515c.png')
icon = icon.resize((163, 100))
icon_tk = ImageTk.PhotoImage(icon)
lbl = Label(about, text="About Gold's Gym", compound='bottom', image=icon_tk, bg='#FFB100',font=("Times", 24, "bold"))
lbl.pack(pady=10)

# ----------------------------- Label 2 ----------------------------------------
lbl2 = Label(about, text='''What’s the history of Gold’s Gym? Why is it so popular?
        Gold's Gym is one of the most well-known and respected fitness chains in the world. 
    It was founded in Venice Beach, California in 1965 by Joe Gold, a bodybuilder and weightlifting enthusiast. 
    Gold's Gym quickly became popular among bodybuilders, powerlifters, and other fitness enthusiasts, 
    thanks to its focus on strength training and its excellent equipment.
    One of the reasons for its popularity is that it was one of the first gyms to focus on weightlifting and bodybuilding. 
    It has also been the home gym of some of the most famous bodybuilders of all time, such as Arnold Schwarzenegger, 
    Lou Ferrigno, and Frank Zane.
    In addition to its reputation as a "Mecca of Bodybuilding," Gold's Gym is also known for its diverse range of training options, 
    including cardio, group fitness, and personal training. It has also been featured in numerous movies, TV shows and music videos, 
    which helped to increase its exposure and popularity.
    Gold's Gym has always been a leader in the fitness industry and continues to be a major player today with gyms all over the world.''',
                 fg="black", font=("Arial", 14), bg='#FFB100')
lbl2.pack(pady=5, after=lbl)

# ----------------------------- Label 3 ----------------------------------------
lbl3 = Label(about, text='''Who is the Golds gym model?
    (April 26, 2022) Gold's Gym, the most iconic name in fitness, 
    has named bodybuilder and fitness mega-influencer Simeon Panda as the new face of the brand. 
    The partnership bridges the famed, Venice-born gym's storied past to the future of the evolving brand ''',
                 bg="#FFB100", fg="black", font=("Arial", 15))
lbl3.pack(pady=10, after=lbl2)

# ----------------------------- Label 4 ----------------------------------------
lbl4 = Label(about, text='''What is special about gold gym?
    ABOUT GOLD'S GYM
    It was the place for serious fitness. Opened long before the modern-day health club existed, 
    the original Gold's Gym featured homemade equipment and a dedication to getting results. 
    It was an instant hit. Gold's Gym quickly became known as “The Mecca of Bodybuilding''', bg="#FFB100", fg="black",
                 font=("Arial", 15))
lbl4.pack(pady=10, after=lbl3)


H = PhotoImage(file='E:/self work/project/gym/home.png')
home = Button(about, text='Home', compound='left', highlightcolor='black', image=H, fg='#43380D',bg='#CAA928',font="Arial 10 bold", bd=0, padx=8, pady=8,command=exit_func)
home.place(x=0, y=0)


top.config()
top.mainloop()