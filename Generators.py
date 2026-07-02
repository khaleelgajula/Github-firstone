#Generators in python

#with using return statement
def numbers():
    return [1,2,3,4]
print(numbers())

#with using field statement
def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
gen =numbers()
print(next (gen))   #1
print(next (gen))   #2
print(next (gen))   #3
print(next (gen))   #4
print(next (gen))   #5

#with using yield statement, for loop

def numbers():
    yield 1
    yield 2
    yield 3
    yield 4
gen=numbers()
for num in gen:
    print(num)
#1
#2
#3
#4

#generate a square of numbers from an given list
li=[1,2,3,4,5]
def square():
    for digit in li :
        yield digit*digit
print(list(square()))           #[1, 4, 9, 16, 25]

#generate even numbers from 1 to 10
def even_gen():
    for i in range(1,11):
        if i%2==0:
            yield i
print(list(even_gen()))             #[2, 4, 6, 8, 10]

#for odd numbers
def odd_gen():
    for i in range(1,11):
        if i%2!=0:
            yield i
print(list(odd_gen()))          #[1, 3, 5, 7, 9]


def even():
    for i in range(1,11):
        if i%2==0:
            yield i*i
print(list(even()))         #[4, 16, 36, 64, 100]

#to print even or odd numbers using generator
li=[1,2,3,4,5,6,7,8,9]
def gen():
    even=[]
    odd=[]
    for i in li:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    yield even
    yield odd
nums = gen()
print(f'even numbers:{next(nums)}')         #even numbers:[2, 4, 6, 8
print(f'odd numbers:{next(nums)}')          #odd numbers:[1, 3, 5, 7, 9]


#Given number is palindrome or not using generstor without slicing
def palindrome_check(n):
    original=n
    reverse=0
    while n>0:
        digit = n%10
        reverse=reverse*10+digit
        n=n//10
    yield original == reverse
num=121
gen =palindrome_check(num)
if next(gen):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")         #121 is palindrome