#IF ELSE:
num=int(input())
if num >5:
    print(num**2)
else:
    print(num**3)
print("program ended")

num=int(input())
if num>=3 and num<=7:
    print(num,num,num,sep='\n')
else:
    print(num%10)
print('program ended')


num=int(input())
if num%3==0 and num%5==0:
    num+1
    print(num)
else:
    print(num//10)
print('program ended')


num=int(input())
if num%12==0 and num%16==0: