#  Write a NumPy program to compute the inverse of a given matrix. 
import numpy as np
m = np.array([[1,2],[3,4]])
print("Original matrix:")
print(m)
result = np.linalg.inv(m)
print("Inverse of the said matrix:")
print(result) 