# Write a Python program to add an item in a tuple.
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
t=tuple(l)
print(t)
x=int(input("Enter the element to be added: "))
t1=t+(x,)
print(t1)
print(type(t1))