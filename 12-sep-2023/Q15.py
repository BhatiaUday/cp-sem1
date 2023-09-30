# Write a Python program to find the index of an item in a specified list.
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
print(l)
x=int(input("Enter the element: "))
print(l.index(x))
