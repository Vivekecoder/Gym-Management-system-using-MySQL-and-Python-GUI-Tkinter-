from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

top = Tk()
top.title("Buy")
top.geometry('1366x786')
top.resizable(False, False)

v1_rbtn = IntVar()
v1_rbtn.set(1)

v1_co = IntVar()
v1_co.set(1)


def CreateTables():
    db = mysql.connector.connect(host="localhost", user="root", password="vivek", db="Gym")
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(id INT Primary key, prod VARCHAR(200), amount INT)""")


def insert_data(ID, pro, am):
    db = mysql.connector.connect(host="localhost", user="root", password="vivek", db="Gym")
    cursor = db.cursor()
    cursor.execute(f"""INSERT INTO products (id, prod, amount) VALUES ({ID}, '{pro}', {am})""")

    db.commit()


def show_data():
    db = mysql.connector.connect(host="localhost", user="root", password="vivek", db="Gym")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    for data in results:
        print(data)


def decrease_value(n):
    db = mysql.connector.connect(host="localhost",user="root",password="vivek",database="gym")

    cursor = db.cursor()
    cursor.execute(f"UPDATE products SET amount = amount - 1 WHERE id = {n}")
    db.commit()
    show_data()
    print("#" * 20)

# product 1    1x1.............................................

l1 = Label(top, text='Classic Joe Classic\n\nBlender Bottle 20oz\n\n$10.00', font=('Arial', 15, 'bold'))
l1.place(x=40, y=10)
b1 = Button(top, text="Buy", command=lambda: decrease_value(1))
b1.place(x=50, y=170)

i1 = Image.open("E:/self work/project/gym/IMG_421.png")
img1 = i1.resize((150, 200))
img_tk1 = ImageTk.PhotoImage(img1)
bt1 = Button(top, image=img_tk1).place(x=250, y=10)


# product 2 1x2............................................
l2 = Label(top, text='Classic Joe Tee \n\n    $24.00', font=('Arial', 15, 'bold'))
l2.place(x=500, y=30)

btn21 = Radiobutton(top, text='L', value=1, variable=v1_rbtn)
btn21.place(x=530, y=115)
rbtn22 = Radiobutton(top, text='XL', value=2, variable=v1_rbtn)
rbtn22.place(x=560, y=115)
rbtn23 = Radiobutton(top, text='2XL', value=3, variable=v1_rbtn)
rbtn23.place(x=595, y=115)
b2 = Button(top, text="Buy", command=lambda: decrease_value(2))
b2.place(x=530, y=170)

i2= Image.open("E:/self work/project/gym/IMG_422.png")
img2 = i2.resize((150, 200))
img_tk2 = ImageTk.PhotoImage(img2)
bt2 = Button(top, image=img_tk2).place(x=690, y=10)


# product 3  1x3.....................................
l3= Label(top, text=" Hand Grip Strengthener", font=('Arial', 15, 'bold'))
l3.place(x=930, y=10)
b3 = Label(top, text='$90.00', font=('Arial', 15, 'bold'))
b3.place(x=965, y=60)
btn31 = Radiobutton(top, text='Green', value=1, variable=v1_co)
btn31.place(x=950, y=100)
rbtn32 = Radiobutton(top, text='Black', value=2, variable=v1_co)
rbtn32.place(x=1010, y=100)
txt33 = Button(top, text='Buy', command=lambda: decrease_value(3))
txt33.place(x=950, y=170)

i3 = Image.open("E:/self work/project/gym/IMG_4133.png")
img3 = i3.resize((150, 200))
img_tk3 = ImageTk.PhotoImage(img3)
imglbl = Label(top, image=img_tk3)
bt3 = Button(top, image=img_tk3).place(x=1200, y=10)



# product 4 2x1.................................
l4 = Label(top, text='Drawstring Bag\n\n  $25.00', font=('Arial', 15, 'bold'))
l4.place(x=25, y=357)
b4 = Button(top, text="Buy", command=lambda: decrease_value(4))
b4.place(x=45, y=470)

i4 = Image.open("E:/self work/project/gym/IMG_4244.png")
img4 = i4.resize((150, 200))
img_tk4 = ImageTk.PhotoImage(img4)
imglbl = Label(top, image=img_tk4)
bt4 = Button(top, image=img_tk4).place(x=250, y=350)


# product 5 2x2.............
l5 = Label(top, text='Gloves\n\n$265.00', font=('Arial', 15, 'bold'))
l5.place(x=530, y=350)
b5 = Button(top, text="Buy", command=lambda: decrease_value(5))
b5.place(x=540, y=460)

i5 = Image.open("E:/self work/project/gym/IMG_4255.png")
img5 = i5.resize((150, 200))
img_tk5 = ImageTk.PhotoImage(img5)
imglbl5 = Label(top, image=img_tk5)
bt5 = Button(top, image=img_tk5).place(x=680, y=350)

# product 6 2x3...............................
l6 = Label(top, text='SportQ Cement Barbell Set  \n\n   $1.350', font=('Arial', 15, 'bold'))
l6.place(x=920, y=350)
b6 = Button(top, text="Buy", command=lambda: decrease_value(8))
b6.place(x=1020, y=445)

i6 = Image.open("E:/self work/project/gym/IMG-2026666.png")
img6 = i6.resize((150, 200))
img_tk6 = ImageTk.PhotoImage(img6)
imglbl6 = Label(top, image=img_tk6)
bt6 = Button(top, image=img_tk6).place(x=1200, y=350)


# product 7 3x1......................
l7 = Label(top, text='Creatine Monohydrate \n\n Powder  \n\n   $1000', font=('Arial', 15, 'bold'))
l7.place(x=25, y=585)
b7 = Button(top, text="Buy", command=lambda: decrease_value(7))
b7.place(x=45, y=755)

i7 = Image.open("E:/self work/project/gym/IMG-20277.png")
img7 = i7.resize((150, 200))
img_tk7 = ImageTk.PhotoImage(img7)
imglbl7 = Label(top, image=img_tk7)
bt7 = Button(top, image=img_tk7).place(x=250, y=590)



# product 8 3x2.....................
l8 = Label(top, text='Commandos\n\n Re-Load weight\n\n Gainer 3KG \n\n       $1500 ', font=('Arial', 13, 'bold'))
l8.place(x=530, y=585)
b8 = Button(top, text="Buy", command=lambda: decrease_value(6))
b8.place(x=560, y=750)

i8 = Image.open("E:/self work/project/gym/IMG_4266.png")
img8 = i8.resize((150, 200))
img_tk8 = ImageTk.PhotoImage(img8)
imglbl8 = Label(top, image=img_tk8)
bt8 = Button(top, image=img_tk8).place(x=680, y=590)


# product 9  3x3 ....................
l9 = Label(top, text='Optimum Nutrition (ON) \n\n Serious Mass High \n\n Protein $3.500',font=('Arial', 14, 'bold'))
l9.place(x=910, y=585)
b9 = Button(top, text="Buy", command=lambda: decrease_value(9))
b9.place(x=1010, y=755)

i9 = Image.open("E:/self work/project/gym/IMG-2099.png")
img9 = i9.resize((150, 200))
img_tk9 = ImageTk.PhotoImage(img9)
imglbl9 = Label(top, image=img_tk9)
bt9 = Button(top, image=img_tk9).place(x=1150, y=590)




top.config()
top.mainloop()
