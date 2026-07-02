
class employee:
    ename='smith'
    sal=98000
    job='Analyst'
#creating object for class 
e1=employee()
#accessing class variables using object
print(f'employee name is :{e1.ename}.')
print(f'employee salary is :{e1.sal}.')
print(f'designation is :{e1.job}.')

class employee:
    pass
e1=employee()
e1.ename='smith'
e1.sal=5000


e2=employee()
e2.ename='King'
e2.sal=9000

print(f' first employee name : {e1.ename} and salary is:{e1.sal}.')
print(f' second employee name : {e2.ename} and salary is:{e2.sal}.')


class student:
    sname='Manke guido'
    mobile=9010433442
    sub1='python'
    sub2='sql'
    sub3='web'
s1=student()
print(f'student name is : {s1.sname}.')
print(f'student mobile no is: {s1.mobile}.')
print(f'student subjects are : {s1.sub1} , {s1.sub2} , {s1.sub3}.')


class car:
    brand= 'Renolt Duster'
    color='black'
    number='AP 39 BD 6785'
c1=car()
print(f'car name is : {c1.brand}.')
print(f'car color is : {c1.color}.')
print(f'car number is : {c1.number}.')