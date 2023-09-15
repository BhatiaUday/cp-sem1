# Write a Python Program to calculate the sum of numbers till the user enters 0
x=0
while True:
    n=int(input("Enter a number: "))
    x+=n
    if n==0:
        break
    else:
        print("Sum of numbers till now is",x)
print("Sum of numbers is",x)