import numpy as np

# stacking matriks
## solusi untuk menyatukan 2 array

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# stacking matrix, menumpuk matrikx
## stacking horizontal
c = np.hstack((a, b))
print(c)

## stacking vertical
d = np.vstack((a, b))
print(d)

# init matriks multidimensi
mat_a = np.zeros((2, 3))
mat_b = np.ones((2, 3))

mat_c = np.hstack((mat_a, mat_b))
mat_d = np.vstack((mat_a, mat_b))

print(mat_c)
print(mat_d)