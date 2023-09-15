# Write a Python Program to convert decimal to binary
x=int(input("Enter a decimal number: "))
y=x
z=0
i=0
while x>0:
    a=x%2
    z=z+a*(10**i)
    x=x//2
    i=i+1
print("The binary equivalent of",y,"is",z)