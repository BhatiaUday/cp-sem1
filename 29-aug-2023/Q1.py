# Write a Python Program to Find the sum of 1st n natural numbers
n=int(input("Enter the number of terms: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of the first",n,"natural numbers is:",sum)