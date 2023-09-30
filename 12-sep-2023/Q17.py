# Write a Python program to append a list to the second list
l=[1,2,3,4,5]
l1=[6,7,8,9,10]
l2=[]
for i in l:
    l2.append(i)
for i in l1:
    l2.append(i)
print(l2)