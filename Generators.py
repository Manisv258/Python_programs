"""Generator - user defined function that returns sequence of values.
   it is an iterator
   range and generator will used to generate the sequence of values
   range - cannot control the flow and only work on integers
   generator - can control the flow and yield or return anything as per requirement. 
   (Characters also we can generate in sequence using generators)
""" 

print(type(range(2,8)))
print(list(range(2,8)))

def gene1(a,b):
    while a < b:
        yield a
        a+=1

print(type(gene1(2,8)))
print(list(gene1(2,8)))


### write a generator function to generate 'a' to 'j' characters.

def gene2(start,stop,step):
    while start <= stop:
        yield chr(start)
        start+= step

print(list(gene2(ord('a'),ord('j'),1)))

print(list(gene2(ord('a'),ord('z'),2)))

print(list(gene2(ord('A'),ord('H'),2)))

