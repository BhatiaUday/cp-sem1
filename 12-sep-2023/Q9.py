# Write a Python program to find the list of words that are longer than n from a given list of words.
l=["abc","xyz","aba","1221"]
n=int(input("Enter the number: "))
l1=[]
for i in l:
    if len(i)>n:
        l1.append(i)
print(l1)