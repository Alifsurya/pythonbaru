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

# format string
# contoh generic
nama = "marlene"
format_str = f"hello {nama}"
print(format_str)

# angka
angka = 2007.2
format_str = f"angka = {angka}"
print(format_str)

bool = True
format_str = f"bool = {bool}"
print(format_str)

angka = 20070000
format_str = f"angka = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2007.1232
format_str = f"angka = {angka:.2f}"
print(format_str)

angka = 2007.1232
format_str = f"angka = {angka:010.2f}"
print(format_str)

# menampilkan + atau -
angkaminus = -10
angkaplus = +10.1929
format_minus = f"angka = {angkaminus:+d}"
format_plus = f"angka = {angkaplus:+.2f}"
print(format_minus)
print(format_plus)

#format persen
persentase = 0.046
format_persen = f"persen {persentase:.2%}"
print(format_persen)