#Recursion in python
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial (num-1)
print(factorial(5))             #120

def total (num):
    if num == 0:
        return 0
    else:
        return num+total(num-1)
print(total(10))                #55

def count_digit (num):
    if num == 0:
        return 0
    else:
        return 1+count_digit(num//10)
print(count_digit(78567))               #5


def sum_digit(num):
    if num==0:
        return 0
    else:
        return num %10 + sum_digit(num//10)
print(sum_digit(876875))                #41

#palindrome or not 
def palindrome(num,rev=0):
    if num==0:
        return rev
    else:
        return palindrome(num//10 ,rev*10+num%10)
num=121
print(num==palindrome(num))                 #True