# Write a Python program to remove an item from a tuple.
t=('a','b','c','d','e')
print(t)
print(type(t))
l=list(t)
x=input("Enter the element to be removed: ")
l.remove(x)
del(t)
t=tuple(l)
print(t)
print(type(t))