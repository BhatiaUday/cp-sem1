# Write a Python program to get unique values from a list
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
print(l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)