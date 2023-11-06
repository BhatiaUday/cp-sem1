# Write a NumPy program to compute the sum of the diagonal element of a given array. 
import numpy as np
n_array = np.array([[55, 25, 15], [30, 44, 2], [11, 45, 77]])
print("Numpy Matrix is:")
print(n_array)
result = np.trace(n_array)
print("\nSum of diagonal elements is:")
print(result)