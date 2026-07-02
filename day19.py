# to print sum of all numbers present in a list
list = [10,45,68,95,40]
i = 0
result = 0
while i < len(list):
    result = result+list[i]
    i = i+1
print(f'sum of all elements is {result}')               #sum of all elements is 258

# To print sum of all even numbers in a list
list = [10,45,68,95,40]
i = 0
result = 0
while i < len(list):
    if list[i]%2==0:
        result=result+list[i]
    i = i + 1
print(f'sum of all even digit elements:{result}')               #sum of all even digit elements:118


# Factors of a number
num = 6
i = 1
while i <=num:
    if num % i ==0:
        print(i)
    i=i+1                   #1,2,3,6


# sum of all factors of  number
num = 6
i=1
sum=0
while i <=num:
    if num % i ==0:
        sum=sum+i
    i=i+1
print(sum)                  #12


# Factorial of number
num=5
fact=1
while num >0:
    fact=fact*num
    num=num-1
print(fact)                     #120

# To check strong number
num=145
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if sum == temp:
    print("strong number")
else:
    print("not a strong number")                        #strong number