# Write a Python program to access specific index of a list
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
print(l)
x=int(input("Enter the index: "))
print(l[x])
