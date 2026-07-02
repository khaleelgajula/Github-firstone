#SIMPLE CALCULATOR
print("====simple calculator====")
print('select operation:')
print('1.addition')
print('2.subtraction')
print('3.multication')
print('4.division')
choice=input('Enter choice (1/2/3/4):')
num1=float (input ('Enter the first number:'))
num2=float (input ('Enter the first number:'))
if choice=='1':
    print(f'the result of the addition:{num1+num2}')
elif choice=='2':
    print(f'the result of the subtraction:{num1-num2}')
elif choice=='3':
    print(f'the result of the multiplication:{num1*num2}')
elif choice=='4':
    print(f'the result of the division{num1/num2}')
else:
    print('error: division by zero is not allowed')
