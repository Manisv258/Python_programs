"""Modify the behavior of the function without changing the actual code.
   Also decorator is a function which takes another function as argument and returns new function(wrapper).
"""
def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator

def greet():
    print("Hello Mani")

greet()