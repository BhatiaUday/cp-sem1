#  Write a Python Program to print the Fibonacci series
a=int(input("Enter the number of terms: "))
x=0
y=1
if a<=0:
    print("Invalid range Input!")
else:
    for i in range(a):
        print(x)
        n=x+y
        x=y
        y=n