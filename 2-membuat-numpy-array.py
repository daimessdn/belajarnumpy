import numpy as np

# inisiasi vektor
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# display hasil
print(a)
print(b)

# membaut vektor dengan range tertentu
c = np.arange(1, 10, 2)
print(c)

# membuat linspace
d = np.linspace(1, 10, 4)
print(d)

# array multidimensi
e = np.array([[1, 2, 3],
	          [4, 5, 6]])
print(e)

# matriks dengan nilai 0
f = np.zeros((5, 5))
print(f)

# matriks dengan nilai 1
g = np.ones((5, 5))
print(g)

# matriks identitas
h1 = np.identity(5)
h2 = np.eye(5)

print(h1)
print(h2)