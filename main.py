import sqlite3
import datetime
import os

# Creates database file
conn = sqlite3.connect('pim.db')

c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS users (
            first text,
            last text,
            gender text
            )""")

# User information
user_first = input("What is your first name?")
user_last = input("What is your last name?")
user_gender = input("What is your gender?")

c.execute("""
INSERT INTO users (first, last, gender)
VALUES (?,?,?)
""", (user_first, user_last, user_gender))

conn.commit()

c.execute("SELECT * FROM users")

# This makes the program aware of it being Morning, Afternoon, or Evening
now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")

if 0 <= datetime.datetime.now().hour < 12:
    if user_gender == "male" or user_gender == "Male":
        print("Good Morning Sir, is there anything that I can do for you?")
    elif user_gender == "female" or user_gender == "Female":
        print("Good Morning Ma'am, is there anything that I can do for you?")
    else:
        print("Good Evening, is there anything that I can do for you?")

elif 14 > datetime.datetime.now().hour >= 12:
    if user_gender == "male" or user_gender == "Male":
        print("Good Afternoon Sir, is there anything that I can do for you?")
    elif user_gender == "female" or user_gender == "Female":
        print("Good Afternoon Ma'am, is there anything that I can do for you?")
    else:
        print("Good Evening, is there anything that I can do for you?")

elif 24 > datetime.datetime.now().hour >= 14:
    if user_gender == "male" or user_gender == "Male":
        print("Good Evening Sir, is there anything that I can do for you?")
    elif user_gender == "female" or user_gender == "Female":
        print("Good Evening Ma'am, is there anything that I can do for you?")
    else:
        print("Good Evening, is there anything that I can do for you?")

receive_task = input()

# Creates table to keep track of the tasks
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
            request text
            )""")

c.execute("""
INSERT INTO tasks (request)
VALUES (?)
""", (receive_task,))

conn.commit()

c.execute("SELECT * FROM tasks")

if 'open' in receive_task:
    if 'chrome' in receive_task or 'Chrome' in receive_task:
        os.startfile(r"C:\Users\Public\Desktop\Google Chrome.lnk")
        print("Opening Chrome ...")
    elif 'firefox' in receive_task or 'Firefox' in receive_task:
        os.startfile(r"C:\Users\Public\Desktop\Firefox.lnk")
        print("Opening Firefox ...")

    conn.close()
