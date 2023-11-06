#  Write a NumPy program to compute the condition number of a given matrix.
import numpy as np
m = np.arange(6).reshape(2,3)
print("Original matrix:")
print(m)
result = np.trace(m)
print("Condition number of the said matrix:")
print(result) 