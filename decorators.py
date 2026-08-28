### Decorators
## functions
# def add(a,b):
#     print("start")
#     result= a+b
#     print(result)
#     print("end")
#     return result
# add(2,3)

### just assume i have have so many functions and i want to add some extra functionality to all of them, then i can use decorators
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):          
#     return a*b

## every time i call any of the above function, i want to print "start" and "end" before and after the function call, so if there is any changes need to be done in the sentence like i should add start opertion and end opertation sentence to start and end then i should change everywhere in the all 3 functions instead of that i can use decorators
# def my_deco(fun):
#     def wrap(*args,**kwargs):
#         print("start operation")
#         result=fun(*args,**kwargs)
#         print(result)
#         print("end operation")
#         return result
#     return wrap
# @my_deco
# def greet(name):
#     return f"hello {name}"

# @my_deco
# def add(a,b):
#     return a+b

# @my_deco
# def say_hi(name):
#     return f"hello {name}"

# add(2,3)
# greet("hi")
# say_hi("dhruva")


# def my_deco(func):
#     def wrap (*args,**kwargs):
#         print("start")
#         res=func(*args,**kwargs)
#         print(res)
#         print("end")
#         return res
#     return wrap
# @my_deco
# def add(a,b):
#     return a+b

# add(3,4)





### Decorator 1 — Logger (Most Common) dec(can be written anything which u pass in main function).__name__ gives you the name of the function as a string.
# def looger_method(dec):
#     def wrap(*args,**kwargs):
#         print(f"start'{dec.__name__}'")
#         result=dec(*args,**kwargs)
#         print(f"the total value of '{dec.__name__}' is {result}")
#         print(f"ended'{dec.__name__}'")
#         return result
#     return wrap
# @looger_method
# def add(a,b):
#     return a+b

# add(5,7)
        
# Decorator 2 — Timer (Performance Checking)

# import time
# def my_deco(arg):
#     def wrap(*args,**kwargs):
#         start=time.time()
#         res=arg(*args,**kwargs)
#         end=time.time()
#         print(f"the time taken to execute {arg.__name__} is {end-start:.4f} seconds")
#         return res
#     return wrap
# @my_deco
# def show_time():
#     time.sleep(1)
#     return "done"
# show_time


# Decorator 3 — Validator (Input Checking)
# def my_deco(func):
#     def wrap(*args,**kwargs):
#         for arg in args:
#             if isinstance(arg,(int,float)):
#                 if arg < 0:
#                     print(f"{arg}its invalid cannot enter negative value")
#                     return None
#         return func(*args,**kwargs)
#     return wrap
# @my_deco
# def salary_caluculate(salary,percent):
#     return salary*percent/100

# print(salary_caluculate(23000,10))
# print(salary_caluculate(-2300,1))


# With @property: will be using getter and setter
# class Engineer:
#     def __init__(self,salary):
#         self._salary=salary
#     @property
#     def salary(self):
#         return self._salary
#     @salary.setter
#     def salary(self,value):
#         if value < 0:
#             raise ValueError("invalid numbers")
#         self._salary=value

# res=Engineer(3)
# print(res.salary)
# res.salary=-3
# print(res.salary)
    

