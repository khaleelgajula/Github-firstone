# FOR LOOP :-


# SYNTAX:
# FOR VARIABLENAME IN SEQUENCE:
#         #STATEMET BLOCK
# ELSE:
#         #STATEMENT BLOCK

# 1. Sequence of numbers from 1 to 5

for i in range(1,6):
    print(i , end='')           #12345

# 2. Sequence of numbers from 6 to 1
for i in range (5,0,-1):
    print(i , end='')               #54321

# 3.elements from given list
names=['smith','martin','scott']
for name in names:
    print(name)

# o/p:-
# smith
# martin
# scott

# 4.characters from string
subject='python'
for ch in subject:
    print(ch)

# o/p:-
# p
# y
# t
# h
# o
# n

for  i in range(10,51,10):
    print(i)

# o/p:-
# 10
# 20
# 30
# 40
# 50

for i in range(1,11):
    if i%2==0:
        print(f'{i} is even number')
    else:
        print(f'{i} is odd number')

#o/p:-
# 1 is odd number
# 2 is even number
# 3 is odd number
# 4 is even number
# 5 is odd number
# 6 is even number
# 7 is odd number
# 8 is even number
# 9 is odd number
# 10 is even number

# even numbers from 1 to 20
for i in range(1,21):
    if i % 2==0:
        print(f'{i} is even number')

# o/p:-
# 2 is even number
# 4 is even number
# 6 is even number
# 8 is even number
# 10 is even number
# 12 is even number
# 14 is even number
# 16 is even number
# 18 is even number
# 20 is even number

total=0
for i in range(1,11):
    total=total+i
print(f'sum of numbers:{total}')

# o/p:-sum of numbers:55

num=5
fact=1
for i in range (1,num+1):
    fact=fact+1
print(fact)         #6

num=3
for i in range (1,11):
    print(f'{num}*{i}:{num*i}')

# o/p:-
# 3*1:3
# 3*2:6
# 3*3:9
# 3*4:12
# 3*5:15
# 3*6:18
# 3*7:21
# 3*8:24
# 3*9:27
# 3*10:30

num=7438
count=0
for i in str(num):
    count=count+1
print(count)            #4

num=7438
sum=0
for i in  str (num):
    sum=sum+int(i)
print(sum)                  #22

num=1234
prod=1
for i in str(num):
    prod=prod*int(i)
print(prod)                 #24

num=123
rev=0
for i in str(num):
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)                  #321

num=7
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
if count ==2:
    print(f'{num} is prime number')
else:
    print(f'{num} is not a prime number')           #7 is prime number

text='education'
count=0
for ch in text:
    if ch in 'AEIOUaeiou':
        count=count+1
    print(count)

num=121
temp=num
rev=0
for i in str(num):
    if temp >0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
if rev==num:
    print(f'{num} is palindrome')
else:
     print(f'{num} is not palindrome')          #121 is palindrome
    
num=153
temp=num
total=0
length=len(str(num))
for i in str(num):
    if temp>0:
        digit=temp%10
        total=total+digit** length
        temp=temp//10
if total==num:
    print(f'{num} is armstrong number')
else:
    print(f'{num} is not armstrong number')             #153 is armstrong number

num=153
sum_of_powers=0
num_digits=len(str(num))
for digit in str(num):
    sum_of_powers=sum_of_powers+int(digit)**num_digits
if sum_of_powers==num:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")                 #153 is an Armstrong number