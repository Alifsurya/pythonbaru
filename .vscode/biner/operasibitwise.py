a = int(input("Masukkan Angka"))
b = int(input("Masukkan Angka"))

# Operasi AND
print(a & b)  # Hasil: 2 (Biner: 0010)
print('\n======AND=======')
print('nilai:', a,', binary:', format(a, '08b'))
print('nilai:', b,', binary:', format(b, '08b'))
# Operasi OR
print(a | b)  # Hasil: 7 (Biner: 0111)
print('nilai:', a,', binary:', format(a, '08b'))
print('nilai:', b,', binary:', format(b, '08b'))
# Operasi XOR
print(a ^ b)  # Hasil: 5 (Biner: 0101)
print('nilai:', a,', binary:', format(a, '08b'))
print('nilai:', b,', binary:', format(b, '08b'))
