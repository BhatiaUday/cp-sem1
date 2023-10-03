# Write a Python program to get a list sorted in increasing order by the last element in each tuple from a given list of not empty tuples.
ls=[ (2,6),(1,3),(4,4),(2,2),(2,5),(2,1)]
ls.sort(key=lambda x: x[-1])
print(ls)