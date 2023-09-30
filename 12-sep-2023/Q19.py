# Write a Python program to find the second smallest number in a list. 
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
print(l)
l.sort()
print(l[1])