import numpy as np

a = np.array([[1, 2, 3],
	          [4, 5, 6]])

# dimensi matriks
print("dimensi matriks a: ", a.shape)

# transpose matriks
print("transpose matriks dari a:")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# flatten array
## vektor baris
print("flatten array matriks a: ")
print(a.ravel())
print(np.ravel(a))

# reshape matriks
print("reshape matriks a:")
print(a.reshape(6, 1))

# resize matriks
## merubah dimensi matriks a
print("resize matriks a:")
print(a.resize(6, 1))
print("dimensi matriks a: ", a.shape)
print(a)