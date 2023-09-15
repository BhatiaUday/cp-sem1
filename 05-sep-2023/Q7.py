# Write a Python Program to sort a dict in ascending and descending order by value
d1={1:25,2:16,3:9,4:4,5:1}
d2={}
l=[]
for i in d1:
    l.append((i,d1[i]))
l.sort(key=lambda x:x[1])
for i in l:
    d2[i[0]]=i[1]
print(d2)