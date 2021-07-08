import numpy as np

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

a_np = np.array(a)
b_np = np.array(b)

# operasi penjumlahan list (kontatinasi)
hasil = a + b
print(hasil)

# operasi penjumlah np array
hasil = a_np + b_np
print(hasil)

# operasi pengurangan np array
hasil = a_np - b_np
print(hasil)

# operasi perkalian np array
hasil = a_np * b_np
print(hasil)

# operasi pembagian np array
hasil = a_np / b_np
print(hasil)

# operasi kuadrat np array
hasil = a_np ** 2
print(hasil)

# operasi artimatika
## pada array multidimensi
c = np.array([[1, 2, 3],
	          [4, 5, 6]])
d = np.array([[7, 8, 9,],
	          [-1, -2, -3]])

hasil = c + d
print(hasil)

hasil = c - d
print(hasil)

hasil = c * d
print(hasil)

hasil = c / d
print(hasil)

hasil = c ** 2
print(hasil)