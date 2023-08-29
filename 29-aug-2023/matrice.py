import numpy as np

A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[1,2,3,4],
   [4,5,6,7],
   [6,7,8,9]]

result=np.dot(A,B)
for r in result:
   print(r)