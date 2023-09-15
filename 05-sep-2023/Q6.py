# Write a Python Program to join 2 dictionary and add the value for common keys
d1={1:1,2:4,3:9,4:16,5:25}
d2={1:36,2:49,3:64,4:81,5:100}
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    if i in d3:
        d3[i]=d3[i]+d2[i]
    else:
        d3[i]=d2[i]
print(d3)
    