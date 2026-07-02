# write a program to check the given number is palindrome or not
num=121
temp=num
rev=0
while temp >0:
    digit=temp % 10
    rev=rev*10+digit
    temp=temp//10
if rev==num:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')             #121 is a palindrome

# write program to find highest digit from given number
num=894
highest=0
while num>0:
    digit= num % 10
    if digit > highest:
        highest = digit
    num=num//10
print(f'highest digit is :{highest}')               #highest digit is :9

# write a program to find lowest from given number
num=894
lowest= 9
while num>0:
    digit= num % 10
    if digit < lowest:
        lowest = digit
    num=num//10
print(f'lowest digit is :{lowest}')                 #lowest digit is :4

# WAP to print sum of digits of an given numbrer is even or odd
num=1345
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits = sum_digits + digit
    num = num // 10
if sum_digits % 2 == 0 :
    print(f'{sum_digits} is even number')
else:
    print(f'{sum_digits} is odd number')            #13 is odd number