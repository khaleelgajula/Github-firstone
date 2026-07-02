#PRINT STATEMENTS
#EVAL STATEMENT
num=eval(('enter the value:'))
print(num)
print(type(num))

result = eval('2'+'2')
print(result)           #22

result = eval ('2+2')
print(result)          #4

#OPERATORS
#1.ADDITION (+)
print(100+200)      #300

print('100'+'200')      #100200

print(98+'hello')       #TypeError

print(98+True)          #99

print('Hello'+' smith')         #Hello smith

a=10
b=20
print(a+b)          #30

a=45
b=68
sum=(a+b)
print(sum)          #113

s1 = 'pyspiders'
s2 = ' jspiders'
s3 = ' qspiders'
s4 = ' prospiders'
s5 = ' Gspiders'
print(s1+s2+s3+s4+s5)       #pyspiders jspiders qspiders prospiders Gspiders

list1 = [10,20,30]
list2= [50,40,70]
result = list1+list2
print(result)               #[10, 20, 30, 50, 40, 70]

t1 = (1,2,3)
t2 = (10 ,20,30)
result=t1+t2
print(result)               #1, 2, 3, 10, 20, 30)


list1 = [10,20,30]
t1 = (1,2,3)
result=list1+t1
print(result)           #typeerror


s1={10,20,30}
s2={30,40,50}
result(s1+s2)
print(result)           #TypeError

#SUBTRACTION(-)
a=200
b=100
print(a-b)      #100

a =98
b =45.28
print(a-b)          #52.72

s1='smith'
s2='scott'
print(s1-s2)        #TypeError: unsupported operand type(s) for -: 'str' and 'str'

#MULTIPLICATION(*)
print(3*2)          #6

a=98
b=3
print(a*b)          #294

print(3*' python')          #python python python

print(2*[10,20])            #[10, 20, 10, 20]

print(4*(10,20))            #(10, 20, 10, 20, 10, 20, 10, 20)

print(3*{10,20,30})         #TypeError:

print(4*{'ename':'smith'})      #TypeError
