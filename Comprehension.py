#comprehension in python
nums=[a for a in range (1,11)]
print (nums)                #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nums = [a*a for a in range (1,11)]
print(nums)                 #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

nums = [a**2 for a in range (1,6)]
print(nums)                 #[1, 4, 9, 16, 25]

even_nums=[num for num in range(1,11) if num%2==0]
print(even_nums)             #[2, 4, 6, 8, 10]


odd_nums=[num for num in range(1,11) if num%2!=0]
print(odd_nums)                 #[1, 3, 5, 7, 9]

li=[11,303,29, 76,89,27,90,78]
even_nums=[num for num in li if num % 2==0]
print(even_nums)            #[76, 90, 78]

words =['python' , 'java' , 'sql']
result=[w.upper() for w in words]
print(result)                   #['PYTHON', 'JAVA', 'SQL']

words =['python' , 'java' , 'sql']
result=[f'{w}:{len(w)}' for w in words]
print(result)           #['python:6', 'java:4', 'sql:3']

nums = [a*a for a in range (1,11) if a%2==0]
print(nums)                 #[4, 16, 36, 64, 100]

nums =[0 if num%2==0 else num for num in range(1,11)]
print(nums)                 #[1, 0, 3, 0, 5, 0, 7, 0, 9, 0]

string = 'python'
chars = (ch for ch in string)
print(list(chars))              #['p', 'y', 't', 'h', 'o', 'n']

nums = {a:a*a for a in range(1,6)}
print(nums)                 #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

nums = {a:a*a for a in range(1,11) if a%2==0}
print(nums)                 #{2: 4, 4: 16, 6: 36, 8: 64, 10: 100}

data ={'a':1 , 'b':2 , 'c':3}
result={v:k for k,v in data.items()}
print(result)           #{1: 'a', 2: 'b', 3: 'c'}

words = ['python' , 'java' , 'sql']
result=[w[::-1] for w in words]
print(result)               #['nohtyp', 'avaj', 'lqs']