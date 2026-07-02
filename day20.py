# perfect number or not
# 6-->1,2,3 ==>1+2+3-->6
num=6
i = 1
sum=0
while i < num:
    if num % i == 0:
        sum = sum+i
    i = i + 1
if sum == num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not a perfect number')                 #6 is perfect number

# spy number or not
# 1124 --> 1+1+2+4 ==>8 & 1*1*2*4 ==>8
# 123 --> 1+2+3 ==>8  & 1*2*3 ==>8
num = 123
temp = num
sum = 0
prod = 1
while num >0:
    digit = num%10
    sum = sum + digit
    prod = prod * digit
    num = num//10
if sum == prod:
    print(f'{temp} is a spy number')
else:
    print(f'{temp} is not a spy number')                #123 is a spy number

# STRING PROGRAMMING USING WHILE LOOP
# ASCII VALUE OF CHARACTERS
string='smith'
i = 0
while i < len(string):
    print(string[i], ':' ,ord(string[i]))
    i = i + 1
#o/p:-
# s : 115
# m : 109
# i : 105
# t : 116
# h : 104

# string on into upper case
s = 'pytHon'
i = 0
result = ''
while i < len(s):
    if s[i] >= 'a' and s[i] <= 'z':
        result = result + chr (ord(s[i])-32)
    else:
        result=result+s[i]
    i=i+1
print(result)                           #PYTHON


# string on into lower case
s='PYTHON'
i = 0
result='' 
while i < len(s):
    if s[i] >='A' and s[i] <='Z':
        result=result+chr(ord(s[i])+32)
    else:
        result=result+s[i]
    i=i+1
print(result)                       #python


# count total occarance of characters in a string
s='python' 
count=0
i=-0
while i < len(s):
    count=count+1
    i=i+1
print(count)                #6


# count total occarance of alphabets present  in a given string
s='pyspiders'
ch='s'
i=0
count=0
while i<len(s):
    if s[i] == ch:
        count=count+1
    i=i+1
print(count)                    #2


# finding vowels in a given string
s='education'
i=0
count=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        count=count+1
    i=i+1
print(count)                #5


# finding vowels & consonants in a given string
s='education'
i=0
vowels=0
consonants=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        vowels=vowels+1
    else:
        consonants=consonants+1
    i=i+1
print(f'count of vowels is : {vowels}')                 #count of vowels is : 5
print(f'count of consonants is : {consonants}')         #count of consonants is : 4

# toggle characters case
s='PytHoN' 
i=0
result=''
while i < len(s):
    ch=s[i]
    if ch >= 'A' and ch <='Z':
        result=result+chr(ord(ch)+32)
    else:
        result=result+ch
    i=i+1
print(result)                       #python