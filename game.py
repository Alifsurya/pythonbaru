import random

pesan = "Selamat Datang di Game acak"
position = random.randint(1, 4)

print("*********************************")
print(f"** {pesan} **")
print("*********************************")

user = input("Masukkan Nama Kamu: ")
print(f'''
halo {user}! Perhatikan goa dibawah ini
|_| |_| |_| |_|
''')

pilihan = int(input("Menurut kamu di goa nomor berapa marmut berada? [1, 2, 3, 4]: "))

if pilihan == position:
    print(f"Selamat {user} kamu menang! posisi marmut ada di nomor goa {position} dan pilihan kamu benar")
else:
    print(f"Kamu Kalah! marmut bukan berada disitu, tapi ada di goa nomor {position}. Sedangkan kamu memilih {pilihan}")
    