# Write a Python Program to check for Armstrong number
n=int(input("Enter the number: "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**(len(str(n)))
    temp//=10
if n==sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")