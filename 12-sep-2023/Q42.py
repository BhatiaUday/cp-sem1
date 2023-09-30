# Write a Python program to check if a specified element presents in a tuple of tuples.
t=(('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))
print(t)
print(type(t))
x=input("Enter the element you want to check: ")
x=x.title()
for i in t:
    if x in i:
        print("Yes")
        break
else:
    print("No")