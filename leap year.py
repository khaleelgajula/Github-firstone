year=2024
if (year % 4 ==0) and (year % 400 ==0 or year % 100 !=0):
    print(f'{year} is leap year')
    if year % 2 ==0:
        print(f'{year} is even year')
    else:
        print(f'{year} is odd year')
else:
    print(f'{year} is not leap year')