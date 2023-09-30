# Write a Python program to create a tuple with numbers and print one item.
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
t=tuple(l)
print(t)
print(type(t))
x=int(input("Enter the index of the element to be printed: "))
print(t[x])