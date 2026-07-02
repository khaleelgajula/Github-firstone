#print even nums
num=16
if num % 2 == 0:
    print(f'{num} is a even number')

# even or add
num=17
if num % 2 == 0:
    print(f'{num} is a even number')
else:
    print(f'{num} is a odd number')

# rev a str
str = 'hello'
print(str[::-1])

def rev_str(s):
    return s[::-1]
print(rev_str("python"))

#find the largest num in the list
nums=[10,20,35]
largest=nums[0]
for i in nums:
    if i > largest:
        largest = i
print(largest)

nums=[1,2,34,6,88,987]
largest= nums[2]
for i in nums:
    if  i > largest:
        largest=i
print(largest)

def largest(lst):
    max_val=lst[0]
    for x in lst:
        if x >max_val:
            max_val= x
    return max_val
print(largest([1,3,6,87,9,]))

#count of vowels in word

str='hello'
result = ''
for ch in str:
    if ch in 'AEIOUaeiou' or ch == '':
        result=result+ch
print(result)

str = 'python'
s1=''
for ch in str:
    if ch not in 'aeiou':
        s1=s1+ch
print(result)


print('hello')
name ="khaleel"
age = 23
print(name)
print(age)

clg = 'Dr kv subba reddy institute of technology'
coaching = 'Qspiders'
print(clg)
print(coaching)

name = input("Enter your name : ")
print("hello" , name)

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou' )
print(count_vowels('khaleel'))

name = "khaleel"
print(name[::-1])

def count_vowels(k):
    return sum(1 for c in k.lower() if c in 'aeiou')
print(count_vowels('nikhil'))
