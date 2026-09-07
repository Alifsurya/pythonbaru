# operaasi dan manipulasi string
# concacenate
nama1 = "ucup"
nama2 = "lagi"
nama3 = "maen"

nameLengkap = nama1 + " " + nama2 + " " + nama3
print(nameLengkap)

# hitung panjang str
panjang = len(nameLengkap)
print(panjang)

# indexing
print("index ke 0-3 :" + nameLengkap[0:4])
print("index ke 0-3 :" + nameLengkap[0:11:2])
print("index ke 0-3 :" + nameLengkap[-1])

print("paling kecil :" + min(nameLengkap))
print("paling kecil :" + max(nameLengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah" + str(ascii_code))

# pake method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = " + str(jumlah))
# merubah case dari string (upper case)
salam = "Bro"
salam = salam.upper()
print(salam)
salam1 = salam.lower()
print(salam1)
contoh = "genjor"
apakah_lower = contoh.islower()
print("Hasilnya apa" + str(apakah_lower))

# isalpha (cek huruf) + isalnum (cek huruf angka)
contoh1 = "genjor"
judul = "The Burger".startswith("The")
# cekjudul = judul.istitle()
print("Benar? " + str(judul))

# join
pisah = ['aku','sedang', 'belajar']
gabungan = ' '.join(pisah)
print(gabungan)
gabungan1 = "akuwwsedangwwbelajar"
print(gabungan1.split('ww'))

# alokasi karakter
kanan = "kanan".rjust(10)
print("'"+kanan+"'")
kiri = "kiri".ljust(10)
print("'"+kiri+"'")
tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# strip kebalikannya
tengah = tengah.strip("-")
print("'"+tengah+"'")

kanan = kanan.strip()
print("'"+kanan+"'")