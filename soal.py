grade = ""
nilai = int(input("Masukkan nilai"))

if nilai >= 90:
    grade = "A"
elif nilai >= 85 and nilai <= 89:
    grade = "B"
elif nilai >= 60  and nilai <= 84:
    grade = "C"
else:
    grade = "D"
print("anda dinyatakan mendapatkan grade = " + grade)