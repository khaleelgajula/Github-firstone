#Decorators in python
def my_decorator(func):
    def wrapper():
        print('Before function execution')
        func()
        print('After Function execution')
    return wrapper
@my_decorator
def say_hello():
    print('Hello Students')
say_hello()

#---------------------------------------------------
def my_decorator(func):
    def wrapper():
        func()
        print('After function execution')
    return wrapper
@my_decorator
def say_hello():
    print('Hello students')
say_hello()

#--------------------------------------------------------------
def my_decorator(func):
    def wrapper():
        print('Before function execution')
        func()
    return wrapper
@my_decorator
def say_hello():
    print('Hello Students')
say_hello()

#----------------------------------------------------------
def deco (fun):
    def inn(*args , **kwargs):
        print("welcome")
        fun(*args , **kwargs)
        print("Thank you")
    return inn
@deco
def wish (name):
    print(f'hello {name}')
wish("smith")

#-------------------------------------------------------------
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('function is about to execute')
        func(*args, **kwargs)
        print('function executed')
    return wrapper
@my_decorator
def add(a,b):
    print(f'sum of {a} and {b} : {a+b}')
add(100,200)
print()
@my_decorator
def greet (name):
    print(f'Hello {name}')
greet('khaleel')