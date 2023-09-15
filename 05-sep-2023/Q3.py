# Write a Python Program to convert binary to decimal
x=int(input("Enter a binary number: "))
y=x
z=0
i=0
while x>0:
    a=x%10
    z=z+a*(2**i)
    x=x//10
    i=i+1
print("The decimal equivalent of",y,"is",z)