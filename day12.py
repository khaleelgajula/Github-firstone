#CONTROL STATEMENTS
#1.CONDITIONAL STATEMENTS
#IF STATEMENTS
a=98
b=45
if a>b:
    print(f'a:{a}is greater than b:{b}')                #a:98is greater than b:45

#indention
a=98
b=45
if a>b:
    print(f'a:{a}is greater than b:{b}')            #a:98is greater than b:45
print('program completed')                          #program completed

num=eval(input('enter the number:'))
if num>0:
    print(f'{num} is positive')

num=98
if num>0:
    print(f'{num} is positive')             #98 is positive

num=46
if num%2==0:
    print(f'{num} is even number')          #46 is even number

num=77
if num%2!=0:
    print(f'{num} is odd number')           #77 is odd number

num=15
if num%3==0:
    print(f'{num} is divisible by 3')           #15 is divisible by 3

num=50
if num%5==0:
    print(f'{num} is divisible by 5')           #50 is divisible by 5

num=15
if num%3==0 and num%5==0:
    print(f'{num} is divisible by 3 and 5')         #15 is divisible by 3 and 5

s1='apple'
if s1[0] in 'aeiouAEIOU':
    print(f'{s1} is starts with vowels')            #apple is starts with vowels

s2='you'
if s2[-1] in 'aeiouAEIOU':
    print(f'{s2} is ends with vowels')              #you is ends with vowels

s3='khaleel'
if s3[-1] not in 'aeiouAEIOU':
    print(f'{s3} is ends with consonants')          #khaleel is ends with consonants

ch='Apple'
if ch[0]>='A' and ch[0]<='Z':
    print(f'{ch} is starts with uppercase')         #Apple is starts with uppercase

ch='Apple' 
if 'A'<=ch[0]<='Z':
    print(f'{ch} is starts with uppercase')         #Apple is starts with uppercase

char='e'
if 'a'<=char<='z':
    print(f'{char} is lowercase')                   #e is lowercase

char='9'
if '0'<= char<='9':
    print(f'{char} is digit')                       #9 is digit

char= '$'
if not('A'<=char<='Z' or 'a'<=char<='z' or '0'<=char<='9'):
    print(f'{char} is special symbol')                  #$ is special 




num = 10
while num>5:
    print('hello')
    num-=1

    start =a
    end =K
    while start<=end:
        print(start)
        start+=1
