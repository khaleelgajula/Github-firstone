#Map functions
num=[1,2,3,4,5]
result = lambda num : num*num
print(result)                       #<function <lambda> at 0x000002BB5AF4E6C0>

num=[1,2,3,4,5]
result =map(lambda num : num*num,num)
print(result)                       #<map object at 0x000002BB58F26880>

num=[1,2,3,4,5]
result =list (map(lambda num : num*num,num))
print(result)                       #[1, 4, 9, 16, 25]

names = ['smith' , 'scott']
result=list(map(lambda w:w.upper(),names))
print(result)           #['SMITH', 'SCOTT']

list1=[1,2,3]
list2=[3,4,5]
result=list(map(lambda x,y : x*y ,list1,list2))
print(result)               #[3, 8, 15]
