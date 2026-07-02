#TYPE CASTING 
#1.IMPLICT TYPE CASTING
a=7
b=4
c=a+b
print(type(c))      #<class 'int'>

a = 98.45
b = 4
d = a+b
print(type(d))      #<class 'float'>

#2.EXPLICT TYPE CASTING
a = 98
print(float(a))             #98.0
print(complex(a))           #(98+0j)
print(bool(a))              #True
print(str(a))               #98


a = 98
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))
#output : TypeError

a = 98.45
print(int(a))       #98
print(complex(a))       #98.45+0j
print(bool(a))      #True
print(str(a))       #98.45


print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))
#TypeError


a = 10+5j
print(bool(a))      #True
print(str(a))       #(10+5j)


print(int(a))
print(float(a))
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))
#TypeError

a = True
print(int(a))            #1
print(float(a))          #1.0
print(complex(a))       #(1+0j)
print(str(a))           #True


print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))
#TypeError


s1 = 'Python'
print(list(s1))         #['P', 'y', 't', 'h', 'o', 'n']
print(tuple(s1))       #('P', 'y', 't', 'h', 'o', 'n')
print(set(s1))         #{'n', 'y', 'P', 't', 'h', 'o'}
print(bool(s1))        #True


print(int(s1))            
print(float(s1))          
print(complex(s1))       
print(dict(s1))
#ValueError

li = [10,20,30,40]
print(str(li))      #[10, 20, 30, 40]
print(tuple(li))    #(10, 20, 30, 40)
print(set(li))      #{40, 10, 20, 30}
print(bool(li))     #True

print(int(li))
print(float(li))
print(complex(li))
print(dict(li))
#TypeError

t1 = (10, 20, 30, 40)
print(str(t1))      #(10, 20, 30, 40)
print(list(t1))     #[10, 20, 30, 40]
print(set(t1))      #{40, 10, 20, 30}
print(tuple(t1))    #(10, 20, 30, 40)

print(int(t1))
print(float(t1))
print(complex(t1))
print(dict(t1))
#TypeError


s1 = {98,45,30,89,17}
print(str(s1))          #{17, 98, 89, 45, 30}
print(tuple(s1))        #(17, 98, 89, 45, 30)
print(list(s1))         #[17, 98, 89, 45, 30]
print(bool(s1))         #True

print(int(s1))
print(float(s1))
print(complex(s1))
print(dict(s1))
#TypeError


d1 = {'ename':'smith','salary':98000}
print(str(d1))      #{'ename': 'smith', 'salary': 98000}
print(tuple(d1))    #('ename', 'salary')
print(set(d1))      #{'ename', 'salary'}
print(bool(d1))     #True

print(int(d1))
print(float(d1))
print(complex(d1))
#TypeError