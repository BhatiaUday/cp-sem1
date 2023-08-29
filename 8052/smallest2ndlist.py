x=int(input("enter how many items you want to enter in the list: "))
li=[]
for i in range(x):
    d=float(input("Enter item: "))
    li.append(d)
li.sort()
sm=li[0]
sm2=li[1]

print("the smallest is: ",sm)
print("the 2nd smallest is: ",sm2)
