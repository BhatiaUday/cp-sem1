# Write a Python program to print the numbers of a specified list after removing even numbers from it.
l=[1,2,3,4,5,6,7,8,9,10]
l1=[]
for i in l:
    if i%2!=0:
        l1.append(i)
print(l1)