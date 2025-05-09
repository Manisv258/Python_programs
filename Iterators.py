"""Iterators
Iteration - process of repeatedly executing the block of code
Iterable object - an object on which iteration can be performed (str,list,tuple,dict etc)
Iterator - object performs iteration on iterable object using iter() function
Manually control the iteration use iter and next 
"""

l1 = [1,2,3,4,5]

#create an iterator

i1 = iter(l1)

print(i1)
print(type(i1))

## fetch the elements using next() function
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))

## once the elements are over stop iteration error will get

print(next(i1,'NA'))


