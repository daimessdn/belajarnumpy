import numpy as np

a = np.arange(10) ** 2
print(a)

# mengambil nilai
print("elemen ke 1 dari a: ", a[0])
print("elemen ke 7 dari a: ", a[6])
print("elemen terakhir dari a: ", a[-1])

# slicing
print("elemen dari 1 hingga 6: ", a[0:5]) # a[start:end]
print("elemen dari 1 hingga 6 dua inteval: ", a[0:5:2]) # a[start:end:step]
print("elemen dari 3 hingga akhir: ", a[3:]) # a[start]

# iterasi
for i in a:
	print(i)