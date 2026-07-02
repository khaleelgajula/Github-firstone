#Filter Functions in python 
num=[1,2,3,45,98]
result = list (filter (lambda num :num%2==0,num))
print(result)           #[2, 98]

words = ['hello' , 'bye' , 'hi']
result= list(filter(lambda s:len(s)>3,words))
print(result)           #['hello']
