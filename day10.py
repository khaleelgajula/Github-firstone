#ASSIGNMENT OPERATOR
#1.+=(add and assign)
a=6
a+=2
print(a)        #8

a=6
a=a+2
print(a)       #8

#2.-=(subtract and assign)
a=6
a-=2
print(a)        #4

a=10
a-=5
print(a)        #5

#3.*=(multiply and assign)
a=9
a*=2
print(a)                  #18

a=10
a*=5
print(a)            #10

#4./=(divide and assign)
a=48
a/=3
print(a)        #16.0

a=45
a/=5
print(a)            #9.0

#5.//=(divide and assign)
a=48
a//=2
print(a)            #24

a=24
a//=2
print(a)            #12

#6.%=(modules and assign)
a=6
a%=2
print(a)            #0

a=7
a%=2
print(a)            #1

#7.**=(power and assign)
a=6
a**=2
print(a)        #36

a=24
a**=4
print(a)        #331776

#LOGICAL OPERATOR
a=98
b=10
print(a>b and b<a)          #True

a=97
b=11
print(a>b or b<a)           #True

a=11
b=95
print(a>b or a==b)          #False

a=98
b=10
print(not(a>b))         #False

a=100
b=100
print(not(a!=b))        #True

a=100
b=90
c=60
print(a>b and b>c and b<a)          #true

a=200
b=100
c=200
print(a>b or b<c or a!=c)           #True

a=97 
b=25
c=50
print(not(a<b<c))                   #True

#MEMBERSHIP OPERATOR
s1='python'
print('p' in s1)        #True

s2='education'
print('j' in s2)        #False

s3='eduation'
print('s' not in s3)        #True

s4='python programming in pyspiders'
print('python' in s4)                   #True

s1='python'
s2='n'
print(s1 in s2)                         #False

s5='welcome to python'
print('PYTHON' in s5)                   #False

li=[10,20,30]
print(10 in li)                     #True

list1=[10,20,30,40,98]
print(98 in list1)                  #True

#IDENTITY OPERATOR
a=98
b=98
print(id(a))                    #140703589294232
print(id(b))                    #140703589294232

a=98
b=98
print(a is b)                   #True

s1='python'
s2='java'
print(s1 is s2)                 #False

s1='python' 
s2='python'                     
print(s1 is s2)                 #True
print(s1 is not s2)             #False

list1=[10,20,30]
list2=[10,20,30]
print(id(list1))                #2018210337600
print(id(list2))                #2018210337472
print(list1 is list2)           #False
print(list1 is not list2)       #True