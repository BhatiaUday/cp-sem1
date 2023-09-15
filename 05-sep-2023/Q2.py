# Write a Python Program to print a dictionary in which the keys are numbers b/w (1,15) and values are their squares
d = {}
for i in range(1, 16):
    d[i] = i*i
print(d)