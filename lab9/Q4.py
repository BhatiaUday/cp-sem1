# Write a Python program to read a given CSV file as a dictionary.
import csv
data = csv.DictReader(open("test.csv"))
print("CSV file as a dictionary:\n")
for row in data:
    print(row)
