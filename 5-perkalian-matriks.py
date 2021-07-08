import numpy as np

a = np.array([[1, 2],
	          [3, 4]])
b = np.ones((2, 2))

print(a)
print(b)

# perkalian matriks
## (element-wise product)
c = a * b
print("matriks a * b")
print(c)

# perkalian matriks
## dot product
d1 = np.dot(a, b) # atau
d2 = a.dot(b)

print("matriks a . b")
print(d1)
print(d2)

