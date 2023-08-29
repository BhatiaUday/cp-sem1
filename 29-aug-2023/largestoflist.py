x=int(input("enter how many items you want to enter in the list: "))
li=[]
for i in range(x):
    d=float(input("Enter item: "))
    li.append(d)
lar=li[0]
for i in li:
    if i>=lar:
        lar=i

print("the largset is: ",lar)