# Write a Python program to find the repeated items of a tuple.
t=('a','b','c','d','e','a','b','c','d','e')
print(t)
print(type(t))
l=[]
for i in t:
    if i not in l:
        l.append(i)
print(l)