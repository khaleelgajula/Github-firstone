#1.comprehension
#student marks analyser using comprehension
#project we can upodate it in resume also


students = {
    "smith" : 67,
    "martin" :82,
    "scott" : 39,
    "allen" : 91,
    "miller" : 28,
    "virat" : 97
}
 
 #Dictonary comprehension for results(pass/fail)
result = {
    name : ("pass" if marks >40 else "fail")
    for name ,marks in students.items()
 }

#Dictionary comprehension for grades
grades = {
    name : (
        "A" if marks >=75 else
        "B" if marks >=60 else
        "C" if marks >=40 else
        "F"
    )
    for name , marks in students.items()
}

#List of passed students 
passed_students = [name for name,status in result.items() if status == "Pass"]


#List of failed students 
failed_students = [name for name,status in result.items() if status == "Fail"]

#Bonus list for toppers
toppers=[name for name , marks in students.items() if marks >=75]
print(f"result : {result}")
print(f"Grades : {grades}")
print(f"passed_students : {passed_students}")
print(f"failed_students : {failed_students}")
print(f"toppers(bonuslist) : {toppers}")



#--------------------------employee management-------------------------------------------
#mini project
#employee mangement system sqlite3+python

import sqlite3
conn = sqlite3.connect('pE18db')
cur = conn.cursor()

#Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS emp(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ename  TEXT,
    job   TEXT,
    sal   REAL
 ) 
""")
conn.commit()

#Create
def add():
    ename = input("Enter name:")
    job = input("Enter job:")
    sal = float(input("Enter salary:"))
    cur.execute("INSERT INTO emp (ename , job , sal) VALUES (?,?,?)", (ename,job,sal))
    conn.commit()
    print("Added!")

#Read

def view():
    cur.execute("SELECT * FROM emp")
    for row in cur.fetchall():
        print(row)

#Update
def update():
    id = int (input("Enter id:"))
    ename = input("Enter new name:")
    job = input("Enter new job:")
    sal = float(input("Enter new salary:"))
    cur.execute("UPDATE emp SET ename=?,job=? , sal=? WHERE id=?", (ename,job,sal,id))
    conn.commit()
    print("Updated!")

#Delete
def delete():
    id =int(input("Enter id:"))
    cur.execute("DELETE FROM emp WHERE id=?",(id,))
    conn.commit()
    print("Deleted!")


#Menu
while True:
    print("\n 1.Add 2.View 3.Update 4.Delete 5.Exit")
    ch = input ("choice:")
    if ch == '1':
        add()
    elif ch == '2':
        view()
    elif ch =='3':
        update()
    elif ch =='4':
        delete()
    elif ch =='5':
        break
conn.close()


#------------------------OTP Generator---------------------------------------------------------
#Random
#OTP generator
import random
otp = ''
for i in range (6):
    digit = random.randint(0,9)
    otp = otp +str (digit)
print(f'Generated OTP is : {otp}')