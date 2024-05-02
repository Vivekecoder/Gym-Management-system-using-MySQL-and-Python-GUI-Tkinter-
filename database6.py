from tkinter import *
import mysql.connector

root = Tk()
root.geometry('1366x786')
root.title("Gym")

# Connect to MySQL database
db = mysql.connector.connect(host="localhost",user="root",password="vivek",database="gym")

cr = db.cursor()

# Adjust table creation queries and datatypes for MySQL
cr.execute("CREATE TABLE IF NOT EXISTS manager2 (user_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), id INT)")


# Adjust insert queries for MySQL
cr.execute('INSERT INTO manager2(name, age, email, password, id) VALUES ("sachin", 29, "sachi96754@gmail", "123456789Mm@@", 1)')
cr.execute('INSERT INTO manager2(name, age, email, password, id) VALUES ("vivek", 24, "vivek96754@gmail", "472003Mm@@", 2)')
cr.execute('INSERT INTO manager2(name, age, email, password, id) VALUES ("virat", 25, "virat912354@gmail", "85200389Mm@@", 3)')
cr.execute('INSERT INTO manager2(name, age, email, password, id) VALUES ("himanshu", 20, "himanshu912354@gmail", "85200389Mm@@", 5)')

# Adjust delete query for MySQL
cr.execute('DELETE FROM manager2 WHERE user_id=3')

db.commit()

# Adjust table creation query for MySQL
cr.execute("CREATE TABLE IF NOT EXISTS signup (user_id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), age INT, email VARCHAR(255), password VARCHAR(255), country VARCHAR(255))")

root.mainloop()
