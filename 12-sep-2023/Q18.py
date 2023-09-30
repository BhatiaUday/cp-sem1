# Write a python program to check whether two lists are circularly identical.
l1=[1,2,3,4,5]
l2=[3,4,5,1,2]
l1.extend(l1)
for i in range(len(l1)):
    if l2==l1[i:i+len(l2)]:
        print("Lists are circularly identical")
        break
else:
    print("Lists are not circularly identical")
    