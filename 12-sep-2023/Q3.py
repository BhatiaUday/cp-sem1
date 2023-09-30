# rite a Python program to get the smallest number from a list.
l=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))    
min=l[0]
for i in l:
    if i<min:
        min=i
print(min)