### Positional argument
"""Passing the argument values in order of their position"""

### default/optional argument
"""default argument value to be given at function definition and optional while calling the function
if the value is given takes the value else it takes default value"""

### Keyword argument
""" while calling the function we can pass the value with argument name as keyword"""

def add(a, b):
    print(f"a: {a}")
    print(f"b: {b}")
    return a + b

print(add(10,20))
print(add(a=20,b=10))

### Variable Length Arguments
def add(*args):
    pass
"""*args - will take variable length arguments"""

def add(*nums):
    print(nums)
    total = sum(nums)
    print(f"Total is {total}")
    print(type(nums))

add(4,5,6)
add(1,2,2,5,6,7,0)

### Variable length keyword arguments
def f1(**kwargs):
    pass
"""*kwargs - will take variable length arguments along with keyword"""

def f1(**kwargs):
    print(kwargs)
    print(type(kwargs))

f1(x=10,y=20)

### Calculate the percentage for different number of arguments
def calculate_percent(**kwargs):
    total_marks = sum(kwargs.values())
    no_of_subs = len(kwargs)
    percent = total_marks / no_of_subs
    return f"{percent}%"

print(calculate_percent(math=99,phy=96,chem=96))
print(calculate_percent(math=95,phy=100))