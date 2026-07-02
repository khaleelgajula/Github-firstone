
#18. write a program to print all vowel Uppercase characters into lowercase

input_str = "EDUCATION"
result = ''
for ch in input_str:
    if ch in 'AEIOU':
        lowercase_char = chr(ord(ch) + 32)
        result += lowercase_char
    else:
        result += ch
print("Result:", result)

# output : eDuCaTioN



#19. write a program to print all Uppercase characters from string

input_str = "Welcome To Python"
uppercase_chars = ''
for ch in input_str:
    if 'A' <= ch <= 'Z':  
        uppercase_chars = uppercase_chars +ch
print("Uppercase characters:", uppercase_chars)




#20. write a program to print all lowercase characters from string

input_str = "Welcome To Python"
lowercase_chars = ''

for ch in input_str:
    if 'a' <= ch <= 'z':  
        lowercase_chars += ch
print("Lowercase characters:", lowercase_chars)





#21. write a program to print only Digits from string 

input_str = "User123"
digits = ''
for ch in input_str:
    if '0' <= ch <= '9': 
        digits += ch
print("Digits in the string:", digits)




#22. write a program to print only special characters from string

input_str = "Hello @ python"
special_chars = ''
for ch in input_str:
    if not (('A' <= ch <= 'Z') or ('a' <= ch <= 'z') or ('0' <= ch <= '9')):
        if ch != ' ':       # Optional: ignore spaces
            special_chars += ch
print("Special characters:", special_chars)




#23. given string is Hello 123 python extract only vowels preserving spaces between words 

st = 'Hello 123 python'
result = ''
for ch in st:
    if ch in 'AEIOUaeiou' or ch == ' ':
        result = result + ch
print(result)


#24. Given string is "Hello 123 python" first extracts vowels then consonent and then digit

st = 'Hello 123 python'
vow = ''
con = ''
digit = ''
for ch in st:
    if ch in 'AEIOUaeiou':
        vow = vow + ch
    elif ch not in 'AEIOUaeiou' and not ch.isdigit():
        con = con + ch
    elif '0' <= ch <= '9':
        digit = digit + ch  
print("Vowels:", vow)
print("Consonants:", con)
print("Digits:", digit)

# Vowels: eoo  
# Consonants: Hll  pythn    
# Digits: 123












#25. write a program to extract all the lowercase character from the given string and add to new string using for loop


input_str = "Python"

lowercase_chars = ''
for ch in input_str:
    if 'a' <= ch <= 'z':
        lowercase_chars += ch

print("Lowercase characters:", lowercase_chars)





# using method

string = 'JspiderS'
s1 = ''
for char in string:
    if char.islower():
        s1=s1+char
print(s1)   






#26. write a program to extract only numbers from the given string 
string = 'python123jspiders'
s1 = ''
for char in string:
    if char.isdigit():
        s1=s1+char  
print(s1)               







#27. write a program to replace all the space in the given string with underscore using for loop



string = 'hello good evening'

out = ''

for i in string:
    if i == ' ':         
        out = out + '_' 
    else:
        out = out + i  
print(out)







# using isspace method

string = 'hello good evening'
out = ''
for i in string:
    if i.isspace():
       out=out+'_'
    else:
        out=out+i
print(out)  







#28. write a program to remove all the vowels from the given string
string = 'python'
s1 = ''
for char in string:
    if char not in 'aeuio':
        s1 = s1+char
print(s1)  





# strong number using nested for loop
num = 145
total =0
for i in str(num):
    fact = 1
    for j in range(1, int(i)+1):
        fact = fact * j
    total = total + fact        
if total == num :
    print(f'{num} is strong number')
else:
    print(f'{num} is not a strong number')

# output : 145 is strong number




#52. Write a program to check a given number is a perfect number or not
# Perfect number is the sum of the given number the proper factors excluding the given number should be equal to the given number.

# 6 can be divide by 1 , 2 , 3  so 1+2+3=6
# 28 can be divide by 1,2,4,7,14 so 1+2+4+7+14=28

num = 6
sum = 0 
temp = num
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if temp == sum:
    print(f'{temp} is a perfect number.')
else:
    print(f'{temp} is not a perfect number.')   



# 52.1.1 spy number program 
# sum of digits equals product of digits

num=1124
sum=0
prod = 1
for digit in str(num):
    sum = sum + int(digit)
    prod = prod * int(digit)
if sum == prod:
    print(num, 'is a spy number')
else:
    print(num, 'is not a spy number') 





# 52.1.2 Fibonacci sequence
# each number is sum of previous two number

num=10
a=0
b=1
for i in range(10):
    print(a , end=' ')
    a,b = b , a+b   

# 0 1 1 2 3 5 8 13 21 34 





# using for Loop
# # a number for which the sum of the digit of its square equals to original number 

a = 9
n = a * a
sum = 0
for digit in str(n):
    sum = sum + int(digit)
if sum == a:
    print(a, 'is Neon number')
else:
    print(a, 'is not Neon number')
