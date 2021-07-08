import numpy as np

# membuat matriks dengan tipe data tertentu
a = np.array([[1, 2, 3],
	          [4, 5, 6]], dtype=float)
print(a)

# membuat matriks menggunakan function
def kuadrat(baris, kolom):
	return kolom ** 2

def jumlah(baris, kolom):
	return kolom + baris

b = np.fromfunction(kuadrat, (1, 10), dtype=int)
print(b)

c = np.fromfunction(jumlah, (4, 4), dtype=float)
print(c)

# membuat array menggunakan iterable
iterable = [x+x for x in range(0, 5)]

d = np.fromiter(iterable, dtype=int)

print(d)

# multitype array
data = [("ucup", 150),
        ("otong", 100),
        ("mario", 130)]
dtipe = [("nama", "S255"), ("tinggi", int)]

e = np.array(data, dtype=dtipe)
print(e)