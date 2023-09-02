# Write a Python Program to print the largest of 3 Numbers
fl1=float(input("Enter 1st number"))
fl2=float(input("Enter 2nd number"))
fl3=float(input("Enter 3rd number"))
li=[fl1,fl2,fl3]
lar=fl1
for i in li:
    if i>=lar:
        lar=i

print("the largset is: ",lar)