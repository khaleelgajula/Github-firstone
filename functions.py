# wap to check given number is positive or negative or zero
def check_number(num):
    if num>0:
        return f'{num} is positive'
    elif num<0:
        return f'{num} is negative'
    else:
        return f'{num} is zero'
print(check_number(98))
#98 is positive

# wap to find factorial of given number
def factorial(num):
    fact=1
    for i in range (1 , num+1):
        fact=fact*i
    return fact
print(factorial(5))
#120

# wap to check the given number is prime numnber or not
def is_prime(num):
    if num <=1:
        return f'{num} is not prime'
    for i in range (2,num):
        if num%i==0:
            return f'{num} is not prime'
    return f'{num} is prime'
print(is_prime(7))
#7 is prime

# wap to reverse a number
def reverse (num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    return rev
print(reverse(1234))
#4321

# wap to find sum of digits
def sum_digits(num):
    sum_digits = 0
    while num > 0:
        digit = num % 10
        sum_digits = sum_digits + digit
        num = num // 10
    return sum_digits
print(sum_digits(1345))

# wap to check given number is palindrome or not
def palindrome(num):
    temp=num
    rev=0
    while temp>0:
        digit=temp % 10
        rev=rev*10+digit
        temp=temp//10
    if rev==num:
        return f'{num} is palindrome'
    else:
        return f'{num} is not palindrome'
print(palindrome(121))
#121 is palindrome

# wap to find largest of 2 numbers
def largest(num):

# wap to check number is armstrong  number
# wap to check number is strong number or not
# wap to check number is perfct number or not
# wap to print fibonacci of n term
def fibonacci(num):

# wap to find the count of digits
# wap to find sum of starting natural numbers(5)
# wap to find power of number
# wap to check number number is neon or not
# wap to check number is spy number or not