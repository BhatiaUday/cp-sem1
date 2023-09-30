# Write a Python program to create a tuple.
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
t=tuple(l)
print(t)
print(type(t))