#RANGE DATATYPES
#example for STOP VALUE
r1 = range(11)
print(r1)       #(0,11)

r2 = range(11)
print(list(r2))         #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r3 = range(11)
print(tuple(r3))        #(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#example for (START,STOP)
r4 = range(1,7)
updated = list(r4)
print(updated)          #[1, 2, 3, 4, 5, 6]

r5 = range(10,17)
print(tuple(r5))        #(10, 11, 12, 13, 14, 15, 16)

#example for (START,STOP,STEP)
r6 = range(1,7,1)
print(list(r6))         #[1, 2, 3, 4, 5, 6]

r7 = range(1,11,2)
print(list(r7))         #[1, 3, 5, 7, 9]

r8 = range(2,11,2)
print(list(r8))         #[2, 4, 6, 8, 10]

r9 = range(10,101,10)
print(list(r9))         #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#examples to generate sequence of order in descending order
r1=range(10,0,-1)
print(list(r1))         #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

r2=range(10,0,-2)
print(list(r2))         #[10, 8, 6, 4, 2]

r3 = range(10,0,-3)
print(list(r3))         #[10, 7, 4, 1]



#INDEXING USING RANGE DATATYPE

r1=range(10,101,10)
updated=(list(r1))
print(updated)              #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(updated[0])           #10
print(updated[1])           #20
print(updated[2])           #30
print(updated[3])           #40
print(updated[4])           #50
print(updated[5])           #60
print(updated[6])           #70
print(updated[7])           #80
print(updated[8])           #90
print(updated[9])           #100

#SLICING USING RANGE DATATYPE
r1=range(10,101,10)
updated=(list(r1))
print(updated)              #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(updated[0:5])         #[10, 20, 30, 40, 50]
print(updated[1:9:2])       #[20, 40, 60, 80]
print(updated[:5])          #[10, 20, 30, 40, 50]
print(updated[5:])          #[60, 70, 80, 90, 100]
print(updated[0:10:3])      #[10, 40, 70, 100]
print(updated[3:8])         #[40, 50, 60, 70, 80]
print(updated[4:9:2])       #[50, 70, 90]
print(updated[6:10])        #[70, 80, 90, 100]
print(updated[2:5])         #[30, 40, 50]

#-ve slicing on range datatype
r1=range(10,101,10)
updated=(list(r1))
print(updated)              #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(updated[-1])          #100
print(updated[-3])          #80
print(updated[-5:-1])       #[60, 70, 80, 90]
print(updated[-7:-2])       #[40, 50, 60, 70, 80]
print(updated[-10:-5])      #[10, 20, 30, 40, 50]
print(updated[-8:])         #[30, 40, 50, 60, 70, 80, 90, 100]
print(updated[:-3])         #[10, 20, 30, 40, 50, 60, 70]
print(updated[-9:-4])       #[20, 30, 40, 50, 60]
print(updated[-6:-3])       #[50, 60, 70]
print(updated[-4:-1])       #[70, 80, 90]


#INPUT AND PRINT STATEMENTS
a = input('enter the value:')
print(a)
print(type(a))      #<class 'str'>

a = int (input('enter the value:'))
print(a)
print(type(a))

a = float (input('enter the value:'))
print(a)
print(type(a))

num = complex (input('enter the value:'))
print(num)
print(type(num))

Num = complex (input=('enter the value:'))
print(Num)
print(type(num))
