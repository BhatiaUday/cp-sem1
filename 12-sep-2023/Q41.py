# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
t=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
print(t)
print(type(t))
l=[]
for i in t:
    sum=0
    length=len(i)
    for j in i:
        sum=sum+j
    avg=sum/length
    l.append(avg)
print(l)