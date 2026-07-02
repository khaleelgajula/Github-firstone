#SQL connection in python
#for CREATE table
import sqlite3
conn=sqlite3.connect('pythonE18db')
cur=conn.cursor()
cur.execute ('''
    create table employee
    (empno    integer,
    ename      text,
    sal        real)
''')
conn.commit()
conn.close()

#for INSERT 
import sqlite3
conn=sqlite3.connect('pythonE18db')
cur=conn.cursor()
cur.execute ('''
    INSERT INTO employee (empno,ename,sal)
    VALUES (7839 , 'king' , 5000)
''')
cur.execute('''
INSERT INTO employee(empno,ename,sal)
VALUES (7889 , 'scott' , 6000)
''')

cur.execute('''
INSERT INTO employee(empno,ename,sal)
VALUES (7777 , 'tillu' ,78000)
''')
conn.commit()
conn.close() 


#For read
import sqlite3

conn = sqlite3.connect('pythonE18db')
cur = conn.cursor()

cur.execute('select * from employee')
rows=cur.fetchall()
for row in rows:
    print(row)
conn.commit()
conn.close()

#For update 

import sqlite3
conn=sqlite3.connect('pythonE18db')
cur = conn.cursor()
cur.execute('''
update employee set sal = 98000 where ename = 'king'
''')
conn.commit()
conn.close()

#For delete 

import sqlite3
conn = sqlite3.connect('pythonE18db')
cur = conn.cursor()
cur.execute('''
delete from employee where ename = 'tillu' 
''')
conn.commit()
conn.close()


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