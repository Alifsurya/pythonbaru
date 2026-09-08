# atur multilane
nama_lengkap = "alif surya pratama"
nama_biasa = "alif"
ukuran_sepatu = "42"
ukuran_baju = "L"
tinggi = "154"
berat = "50"
data_diri = f"Nama Lengkap saya adalah {nama_lengkap}, \nbiasa dipanggil = {nama_biasa}, \nukuran sepatu saya = {ukuran_sepatu}, \nukuran baju = {ukuran_baju}, \ntinggi = {tinggi}, \nberat = {berat}"
print(5*"="+ "DATA DIRI" + 5*"=")
print(data_diri)

data_diri1 = f""" 
Nama Lengkap saya adalah {nama_lengkap}
biasa dipanggil     = {nama_biasa:>5}
nukuran sepatu saya = {ukuran_sepatu:>5} 
ukuran baju         = {ukuran_baju:>5}
tinggi              = {tinggi:>5}
berat               = {berat:>5} 
"""
print(5*"="+ "DATA DIRI" + 5*"=")
print(data_diri1)

import datetime as dt
hari_ini = dt.date.today()
print(f"hari ini adalah {hari_ini:%a}")
tanggal = dt.date(2026, 9, 7)
print("Tanggal sekarang adalah", tanggal)
print(f"hari ini adalah {tanggal:%A}")

print(5*"-" + "Silahkan Masukkan tanggal lahir anda" + 5*"-")
tanggal = int(input("Masukkan tanggal lahir\t"))
bulan = int(input("Masukkan bulan lahir\t"))
tahun = int(input("Masukkan tahun lahir\t"))
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal kamu lahir adalah {tanggal_lahir}")
print(f"Hari kamu lahir adalah {tanggal_lahir:%A}")

hari_ini = dt.date.today()
umur = hari_ini - tanggal_lahir
umur_tahun = umur.days // 365
print(f"Umur anda sekarang adalah {umur_tahun} tahun")

print (10*"="+" Data Lahir "+"="*10)
tanggal=int (input("tanggal lahir \t: "))
bulan=int (input("bulan lahir \t: "))
tahun=int (input("tahun lahir \t: "))
tanggal_lahir= dt.datetime(tahun,bulan,tanggal)
print (f"tanggal Lahir adalah {tanggal_lahir}")
print (f"hari Lahir adalah  {tanggal_lahir:%A}")
umur = hari_ini.year - tanggal_lahir.year
bulan_lahir = hari_ini.month - tanggal_lahir.month
print (f"Umur anda adalah {umur} tahun, {bulan_lahir} Bulan")
