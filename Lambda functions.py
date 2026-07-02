#Lambda functions
addtion = lambda a,b :a+b
print(addtion (100,500))            #600

square = lambda num: num*num
print(square(5))                    #25

number = lambda n:'even' if n%2==0 else 'odd'
print(number(98))               #even

height = lambda a,b:a if a>b else b
print(height(10,98))            #98

s1 = lambda s:s.upper()
print(s1('python'))             #PYTHON

length = lambda l:len(l) 
print(len('education'))         #9

rev=lambda s:s[::-1]
print(rev('python'))            #nohtyp

