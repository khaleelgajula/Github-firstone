t1=(10,20,30,40)
print(t1)       #output : (10, 20, 30, 40)

t1=(10,20,30,40)
print(type(t1))     #output : <class 'tuple'>

t2= (10,98,100,True,False,200)
print(t2)           #output : (10, 98, 100, True, False, 200)

t2= (10,98,100,True,False,200)
print(type(t2))     #output : <class 'tuple'>

e = 10,20,98
print(e)            #output : (10, 20, 98)
print(type(e))      #output : <class 'tuple'>

e = (10)
print(type(e))      #output : <class 'int'>

e = (10,)
print(type(e))      #output : <class 'tuple'>

#indexing on tuple
t1 = (900,100,400,500,98,14,(1,2,3),'smith')
print(t1[0])        #900
print(t1[1])        #100
print(t1[2])        #400
print(t1[3])        #500
print(t1[4])        #98
print(t1[5])        #14
print(t1[6])        #(1,2,3)
print(t1[-1])       #smith
print(t1[-2])       #(1,2,3)
print(t1[-3])       #14
print(t1[-5])       #500


#slicing on tuple
#positive slicing
t1 = (900,100,400,500,98,14,(1,2,3),'smith')
print(t1[0:5:1])        #(900, 100, 400, 500, 98)
print(t1[1:7:1])        #(100, 400, 500, 98, 14, (1, 2, 3))
print(t1[2:8:2])        #(400, 98, (1, 2, 3))
print(t1[0:9:2])        #(900, 400, 98, (1, 2, 3))
print(t1[3:9:2])        #(500, 14, 'smith')
print(t1[4:9:1])        #(98, 14, (1, 2, 3), 'smith')
print(t1[1:9:2])        #(100, 500, 14, 'smith')
print(t1[0:8:4])        #(900, 98)
print(t1[2:9:3])        #(400, 14)
print(t1[5:9:1])        #(14, (1, 2, 3), 'smith')


#negative slicing
t1 = (900,100,400,500,98,14,(1,2,3),'smith')
print(t1[-9:-1:1])      #(900, 100, 400, 500, 98, 14, (1, 2, 3))
print(t1[-8:-2:1])      #(900, 100, 400, 500, 98, 14)
print(t1[-7:-1:3])      #(100, 98)
print(t1[-6:-2:1])      #(400, 500, 98, 14)
print(t1[-5:-1:2])      #(500, 14)
print(t1[-9:-3:2])      #(900, 400, 98)
print(t1[-8:-1:1])      #(900, 100, 400, 500, 98, 14, (1, 2, 3))
print(t1[-6:-1:2])      #(400, 98, (1, 2, 3))
print(t1[-7:-3:2])      #(100, 500)
print(t1[-4:-1:1])      #(98, 14, (1, 2, 3))


#reverse sling on tuple
t1 = (900,100,400,500,98,14,(1,2,3),'smith')
print(t1[::-1])     #('smith', (1, 2, 3), 14, 98, 500, 400, 100, 900)
print(t1[2::-2])    #(400, 900)
print(t1[-2::-2])   #((1, 2, 3), 98, 400, 900)


#SET datatype
s1 = {10,20,30,40}
print(s1)           #{10,20,30,40}
print(type(s1))     #<class 'set'>

s2 = {10,98.10,'smith',(1,2,3),45}
print(s2)           #{10,98.10,'smith',(1,2,3),45}
print(type(s2))     #<class 'set'>


#indexing on set
s1 = {10,20,30,40,98}
li=list(s1)
print(li)       #[98, 20, 40, 10, 30]

print(li[0])    #98
print(li[1])    #20

#slicing on set
s1 = {10,20,30,40,98}
li=list(s1)
print(li[1:5:1])        #[20, 40, 10, 30]


#dictionary datatype
d1 = {'a':10,'b':20,'c':30}
print(d1)           #{'a': 10, 'b': 20, 'c': 30}
print(type(d1))     #<class 'dict'>

data = {'ename':'smith','salary':98000,'job':'analyst'}
print(data)             #{'ename': 'smith', 'salary': 98000, 'job': 'analyst'}
print(type(d1))         #<class 'dict'>
print(data.keys())      #dict_keys(['ename', 'salary', 'job'])
print(data.values())    #dict_values(['smith', 98000, 'analyst'])


# example for nested dictionary
employees={
    'emp1':{'ename':'smith','sal':98000},
    'emp2':{'ename':'martin','sal':95000},
    'emp3':{'ename':'scott','sal':45000},
    'emp4':{'ename':'allen','sal':38000},
    'emp5':{'ename':'jones','sal':78500},
}
print(employees['emp3'])            #{'ename': 'scott', 'sal': 45000}
print(employees['emp3']['ename'])       #scott
print(employees['emp2'],employees['emp4'])      #{'ename': 'martin', 'sal': 95000} {'ename': 'allen', 'sal': 38000}
