# Write a Python Program to make a simple calculator
while True:
    n1=float(input("Enter 1st number: "))
    n2=float(input("Enter 2nd number"))
    print("What do you want to do: ")
    u=int(input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
    if u==1:
        print("The sum is ", n1+n2)
    elif u==2:
        print("The diffrence is ",n1-n2)
    elif u==3:
        print("The product is ",n1*n2)
    elif u==4:
        print("The difference is ",n1/n2)
    else:
        print("Invalid input")