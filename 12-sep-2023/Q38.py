# Write a Python program to sort a tuple by its float element in descending order.
l=[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
l.sort(key=lambda x:float(x[1]),reverse=True)
print(l)