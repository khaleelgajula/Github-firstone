#ELIF STATEMENTS
char=input()
if char>='A' and char<='Z':
    print(f'{char} is uppercase')
elif char>='a' and char<='z':
    print(f'{char} is lowercase')
else:
    print('error')