# Write a Python program to check whether an element exists within a tuple.
t=('a','b','c','d','e')
print(t)
print(type(t))
x=input("Enter the element to be checked: ")
if x in t:
    print("Element exists")
else:
    print("Element does not exist")
