# Write a Python program to remove an empty tuple(s) from a list of tuples
l=[(),(),('',),('a','b'),('c','d','e'),('f',),('g','h','i')]
print(l)
l1=[]
for i in l:
    if i!=():
        l1.append(i)
print(l1)