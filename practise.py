for i in range(1,6):
    if i == 3:
        continue
    print(i)

for i  in range(1,21):
    if i % 2 !=0:
        continue
    print(i)

for i in range (1,21):
    if i%2==0:
        continue
    print(i)

for i  in range(1,21):
    if i == 5:
        break
    print(i)

for i in  'abcdefghijklmnopqrstuvwxyz':
    if i == 'h':
    
        break
    print(i)

for i in range(1,21):
    if i%7==0:
        break
    print(i)

num=int(input('Enter a number:'))
for i in range(1,num+1):
    if i%2==0:
        print(i)

s1='welcome to python class'
print(s1.split())

try:
    num = int(input('Enter a number:'))
    for i in range(1, num+1):
        if i % 2 == 0:
            print(i)
except ValueError:
    print('Invalid input! please enter an integer')





num = 5
a = 0
b =1
count = 0
while count<num:
    print(a)
    a,b = b,a+b
    count+=1


num=10
a=0
b=1
for i in range(10):
    print(a)
    a,b=b,a+b

num = 10
a = 0
b =1
count = 0
while count<num:
    print(a)
    a,b = b,a+b
    count+=1


num = 123
rev = 0
while num >0:
    # digit = num % 10
    rev = rev*10+num%10
    num=num//10
print(rev)

num=123
rev=0
for i in str(num):
    rev=rev*10+num%10
    num=num//10
print(rev)

def rev_number(n):
    rev=0
    while n >0:
        rev=rev*10+n%10
        n=n//10
    return rev
# n=int(input("Enter a number to reverse: "))
print("reversed number:")
rev_number(1234)

num = 121
temp = num
rev = 0
while num > 0:
    digit=num%10
    rev = rev*10+digit
    num=num//10
if temp==rev:
    print(f'{temp} is a palindrome')
else:
    print(f'{temp} is not a palindrome')


num=121
temp=num
rev=0
for i in str(num):
    if int(num)>0:
        digit = num%10
        rev = rev * 10+digit
        num=num//10
if temp==rev:
    print(f'{temp} is palindrome')
else:
    print(f'{temp} is not a palindrome')




def rev_number(n):
    rev=0
    while n >0:
        rev=rev*10+n%10
        n=n//10
    return rev
def is_palindrome(n):
    return n == rev_number(n)
# n=int(input("enter a number to cheak palindrome: "))
if is_palindrome(num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
is_palindrome(121)



num=153
temp=num
sum_cubes=0
length=len(str(num))
while num>0:
    digit=num%10
    sum_cubes=sum_cubes+digit**length
    num=num//10
if temp ==sum_cubes:
    print(f'{temp} is a armstrong')
else:
    print(f'{temp} is not a armstrong')

num=153
temp=num
sum_cubes=0
length=len(str(num))
for i in str(num):
    if num>0:
        digit=num%10
        sum_cubes=sum_cubes+digit**length
        num=num//10
if temp==sum_cubes:
    print(f'{temp} is a armstrong num')
else:
    print(f'{temp} is not a armstrong num')


def is_armstrong(num):
    temp=num
    digits=len(str(num))
    total=0
    while temp>0:
        digit=temp%10
        total=total+digit**digits
        temp=temp//10
    if total==num:
        print(f'{num} is a armstrong num')
    else:
        print(f'{num} is not a armstrong num')
# num=int(input("enter a number:"))
is_armstrong(153)




num=5
i=1
count=0
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1
if count == 2:
    print(f'{num} is a prime num')

else:
    print(f'{num} is not a prime num')

num=11
i=1
count=0
for i in range(1,num+1):
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f'{num} is a prime num')
else:
    print(f'{num} is not a prime num')


def is_prime(num):
    if num <=1:
        return "not a prime num"
    for i in range(2,num):
        if num%i==0:
            return "not a prime num"
    return "prime num"
    print(i)
is_prime(5)

n=5
a,b=0,1
count=0
while count<n:
    print(a,end='')
    a,b=b,a+b
    count+=1

n=10
a=0
b=1
count=0
for i in range(10):
    print(a,end='')
    a,b=b,a+b

def fibonacci(n):
    a,b=0,1
    count=0
    while count<n:
        print(a,end='')
        a,b=b,a+b
        count+=1
fibonacci(10)


num=9
sum_digits=0
temp=num
while temp>0:
    digit=temp%10
    sum_digits+=digit
    temp=temp//10
if sum_digits==num:
    print(num,"is a neon num")
else:
    print(num,"is not a neon num")

a=9
n=a*a
sum=0
for digit in str(n):
    sum=sum+int(digit)
if sum==a:
    print('neon num')
else:
    print('not a neon num')

def is_neon(n):
    square=n*n
    sum_digits=0
    temp=square
    while temp>0:
        sum_digits+=temp%10
        temp=temp//10
    if sum_digits==n:
        print('neon num')
    else:
        print('not a neon num')
is_neon(9)


num=6
i=1
while i < num:
    if num %i==0:
        print(i)
    i=i+1


num=6
i=1
for i in range(1,num+1):
    if num%i==0:
        print(i)

def factors(n):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
factors(6)

num=5
fact=1
while num >0:
    fact=fact*num
    num=num-1
print(fact)

num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
factorial(5)

num=145
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    i=1
    while i <= digit:
        fact=fact*i
        i=i+1

    sum=sum+fact
    num=num//10
if sum == temp:
    print('strong num')
else:
    print('not a strong num')

num=145
total=0
for i  in str(num):
    fact=1
    for i in range(1,int(i)+1):
        fact=fact*i
    total=total+fact
if total==num:
    print('strong num')
else:
    print('not a strong num')

def factorial(num):
    fact=1
    for i  in range(1,num+1):
        fact *= i
    return fact
def is_strong(num):
    temp=num
    sum=0
    while temp>0:
        sum+=factorial(temp%10)
        temp=temp//10
    if sum==num:
        print('strong num')
    else:
        print('not a strong num')
is_strong(145)

num=6
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
if sum==num:
    print('perfect num')
else:
    print('not a perfect num')

num=6
sum=0
temp=num
for i  in range(1,num):
    if num%i==0:
        sum=sum+i
if temp==sum:
    print('perfect num')
else:
    print('not a perfect num')

def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        print('perfect num')
    else:
        print('not a perfect num')
is_perfect(6)

num=123
temp=num
sum=0
prod=1
while num>0:
    digit=num%10
    prod=prod*digit
    sum=sum+digit
    num=num//10
if sum==prod:
    print('spy num')
else:
    print('not a spy num')

num=123
sum=0
prod=1
for digit in str(num):
    sum=sum+int(digit)
    prod=prod*int(digit)
if sum==prod:
    print('spy num')
else:
    print('not s spy num')


def is_spy(n):
    sum_digits=0
    prod_digits=1
    temp=n
    while temp>0:
        r=temp%10
        sum_digits+=r
        prod_digits*=r
        temp//=10
    if sum_digits==prod_digits:
        print('spy num')
    else:
        print('not a spy num')
is_spy(123)

num=894
highest=0
while num>0:
    digit=num%10
    if digit>highest:
        highest=digit
    num=num//10
print(f'{highest}')

num=[10,20,68]
highest=num[0]
for i in num:
    if i>highest:
        highest=i
print(f'{highest}')

def largest(lst):
    max_val=lst[0]
    for x in lst:
        if x>max_val:
            max_val=x
    return max_val
print(largest([1,4,8]))

num=894
lowest=6
while num>0:
    digit=num%10
    if digit<lowest:
        lowest=digit
    num=num//10
print(f'{lowest}')

nums = [2,34,5,6]
lowest=num[34]
for i in nums:
    if i<lowest:
        lowest=i
print(f'{lowest}')

def lowest(lst):
    min_val=lst[0]
    for x in lst:
        if x<min_val:
            min_val=x
    return min_val
print(lowest([1,2,56]))

def large_small(lst):
    max_val=lst[0]
    min_val=lst[0]
    for x in lst:
        if x>max_val:
            max_val=x
        if x<min_val:
            min_val=x
    return max_val,min_val
print(large_small([2,4,6,78,88]))



class employee:
    def __init__ (self,ename,empno):
        self.ename=ename
        self.empno=empno
class emp_Details(employee):
    def __init__(self,ename,sal,empno,job) :
        super().__init__(ename,empno)
        self.sal=sal
        self.job=job
    def display(self):
        print(f'empno is :{self.empno}')
        print(f'ename is : {self.ename}')
        print(f'salary is : {self.sal}')
        print(f'jab is : {self.job}')
obj = emp_Details('kamal',98000,4557,'python developer')
obj.display()