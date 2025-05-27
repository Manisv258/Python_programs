"""Modify the behavior of the function without changing the actual code.
   Also decorator is a function which takes another function as argument and returns new function(wrapper).
"""
def decorator(func):
    def wrapper(*args,**kwargs):
        print(f"The function name is {func.__name__} and args is {args} and kwargs is {kwargs}")
        result = func(*args,**kwargs)
        print(f"The result is {result}")
        return result
    return wrapper

@decorator

def addition(a,b,c):
    return a + b + c

addition(10,20,c=30)