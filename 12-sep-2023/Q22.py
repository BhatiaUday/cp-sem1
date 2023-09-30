# Write a Python program to get the frequency of the elements in a list.
l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    l.append(int(input("Enter the element: ")))
print(l)
d1={}
for i in l:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print(d1)