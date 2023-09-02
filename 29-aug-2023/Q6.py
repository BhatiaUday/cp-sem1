# Write a Python Program to make a list of all even numbers between 4 and 30
x=4
li=[]
while x<=30:
    if x%2==0:
        li.append(x)
    x+=1

print(li)