#DIVISION OPERATOR
#1.TRUE DIVISION(/)
a=98
b=45
print(a/b)          #2.1777777777777776

a=6
b=3
print(a/b)          #2.0


#2.FLOOR DIVISION(//)
a=91
b=45
print(a//b)     #2

a=39
b=3
print(a//b)         #13

a=45.98
b=23.78
print(a//b)         #1.0

num = 784568
print(num//10)      #78456

num = 784568
print(num//100)       #7845

num = 784568
print(num//1000)        #784

#MODULAS(%)
a=11
b=2
print(a%b)      #1

a=10
b=2
print(a%b)      #0

num = 784568
print(num%10)       #8

num = 784568
print(num%100)      #68

num = 784568
print(num%1000)     #568

num = 784568
print(num%10000)     #4568

#EXPONENT OPERATOR(**)
print(2**3)     #8

#RELATIONAL OPERATOR
a=98
b=98
print(a==b)         #True


a=98
b=45
print(a==b)         #False

s1= 'jspiders'
s2= 'JSPIDERS'
print(s1==s2)     #False

l1=[10,20,30]
l2=[10,20,30]
print(l1==l2)           #True

a=98
b=100
print(a!=b)             #True

s1='python' 
s2='java'
print(s1!=s2)           #True

s3='apple'
s4='microsoft' 
print(s3!=s4)           #True

a=198
print(a>100)            #True

s1='python' 
s2='java'
print(s1>s2)        #True

s3='apple'
s4='microsoft' 
print(s4>s3)            #True

print(ord('p'))         #112
print(ord('j'))         #106

char='A'
print(ord(char))        #65

char='a'
print(ord(char))        #97

s1='A'
result=(ord(s1)+32)
print(chr(result))      #a

s2='a'
result=(ord(s2)-32)
print(chr(result))      #A

#SWAPPING TWO NUMBERS
a=5
b=10
a,b=b,a
print(a,b)      #10,5

a=5
b=10
print(f'before swapping a:{a}and b:{b}')        #before swapping a:5and b:10
a,b=b,a
print(f'after sawpping a:{a}and b:{b}')         #after sawpping a:10and b:5



a=5
b=10
print(f'before swapping a:{a}and b:{b}')            #before swapping a:5and b:10  
temp=a
a=b
b=temp
print(f'after swapping a:{a}and b:{b}')             #after swapping a:10and b:5