# Write a Python Program to concatinate 2 dictionary to make a new one
d1={1:1,2:4,3:9,4:16,5:25}
d2={6:36,7:49,8:64,9:81,10:100}
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    d3[i]=d2[i]
print(d3)