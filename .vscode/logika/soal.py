inputUser = float(input("masukan nilai :"))

# soal 1:
assign = (inputUser > 0)
assign2 = (inputUser < 5)
assign3 = (inputUser > 8)
assign4 = (inputUser < 11)

assign5 = (assign and assign2 or assign3 and assign4)
print("hasil akhir: ",assign5)

# soal 2:
assign   = (inputUser < 0)
assign2  = (inputUser > 5)
assign3  = (inputUser < 8)
assign4  = (inputUser > 11)
hasilakhir = (assign or assign2 and assign3 or assign4)
print("hasil akhirnya :",hasilakhir)