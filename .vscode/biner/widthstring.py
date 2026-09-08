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