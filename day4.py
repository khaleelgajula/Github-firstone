#list collection datatype
# c = [10 , 20 ,40 , 70 , 98 , 270]
# print(c[0])         #10
# print(c[1])         #20
# print(c[2])         #40
# print(c[3])         #70
# print(c[5])         #270
# print(c[-1])        #270
# print(c[-3])        #70
# print(c[-9])        #IndexError: list index out of range

#nested list
# a = (10,20,['smith',100,200],98,270)
# print(a[2][0])      #smith
# print(a[2][1])      #100
# print(a[2][-1])     #200
# print(a[-3][-3])    #smith
# print(a[-3][-2])    #100
# print(a[-3][-1])    #200
# print(a[4])         #270

#slicing of list
# li = [10,'python',3.14,True,[1,2],{"a":1},(5,6)]
# print(li[0:3:1])       
# print(li[1:4:1])          
# print(li[2:6:1])       
# print(li[3:7:1])        
# print(li[0:4:1])        
# print(li[2:7:1])      
# print(li[1:6:2])       
# print(li[0:7:2])
# print(li[0:7:3])
# print(li[4:7:1])
#  #output : [10, 'python', 3.14]
#           #['python', 3.14, True]
#         #[3.14, True, [1, 2], {'a': 1}]
#         #[True, [1, 2], {'a': 1}, (5, 6)]
#         #[10, 'python', 3.14, True]
#         #[3.14, True, [1, 2], {'a': 1}, (5, 6)]
#         #['python', True, {'a': 1}]
#         #[10, 3.14, [1, 2], (5, 6)]
#         #[10, True, (5, 6)]
#         #[[1, 2], {'a': 1}, (5, 6)]



li = [10,'python',3.14,True,[1,2],{"a":1},(5,6)]
print(li[-7:-4:1])
print(li[-6:-3:1])
print(li[-5:-2:1])
print(li[-4:-1:1])
print(li[-3:7:1])
print(li[-7:7:2])
print(li[-6:6:2])
print(li[-5:6:1])
print(li[-4:6:1])
print(li[-7:-1:1])


li = [10,'python',3.14,True,[1,2],{"a":1},(5,6)]
print(li[6::-1])        #[(5,6),{'a':1},[1,2],True,3.14,'python',10]
print(li[6:0:-1])       #[(5,6),{'a':1},[1,2],True,3.14,'python']
print(li[5:1:-1])       #[{'a':1},[1,2],True,3.14]
print(li[4::-1])        #[[1,2],True,3.14,'python',10]
print(li[6:2:2])        #[]