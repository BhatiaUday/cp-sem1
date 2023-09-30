# Write a Python program to replace last value of tuples in a list.
l=[(10,20,40),(40,50,60),(70,80,90)]
print(l)
l1=[]
for i in l:
    l1.append(i[:-1]+(100,))
print(l1)
