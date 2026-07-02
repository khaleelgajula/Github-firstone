num=5
i = 1
count = 0
while i <= num:
    if num%i==0:
        count = count+1
    i = i+1
if count ==2:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')
# prime numbers are 2,3,5,7,11,13,17,19,.....


# armstrong number
num=153
temp=num
sum_cubes=0
length=len(str(num))
while num >0:
    digit=num%10
    sum_cubes=sum_cubes+digit**length
    num=num//10
if temp==sum_cubes:
    print(f'{temp} is Armstrong number')
else:
    print(f'{temp} is not a Armstrong number')
# Armstrong number means 153=1^3+5^3+3^3-->153
# ex:- 1634,8208,9474


# fibonacci sequence upto n terms
n = 5
a,b=0,1
count=0
while count < n:
    print(a,end='')
    a,b = b,a+b
    count+=1
# fibonacci means o+1=1,1,1+1=2,1+2=3.......


# Neon number or not
num=9
square=num*num
sum_digits=0
temp=square
while temp > 0:
    digit = temp % 10
    sum_digits+=digit
    temp=temp//10
if sum_digits == num:
    print(num,"is a neon number")
else:
    print(num,"is not a neon number")       
# neon means 9^2=81-->8+1==>9