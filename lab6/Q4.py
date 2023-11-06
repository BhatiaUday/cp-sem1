# Write a NumPy program to compute the determinant of a given square array. 
import numpy as np
a = np.array([[1, 0], [1, 2]])
print("Original 2-d array")
print(a)
print("Determinant of the said 2-D array:")
print(np.linalg.det(a)) 