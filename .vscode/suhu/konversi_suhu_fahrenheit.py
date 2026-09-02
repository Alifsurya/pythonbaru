print ("===========================")
print ("|| Program Konversi Suhu ||")
print ("===========================")
print ("\n")
print ("========================")

fahrenheit = float(input("Masukkan Suhu"))
print("Suhu saat ini adalah", fahrenheit, "Fahrenheit")

reamur = (fahrenheit - 32) * (4/9)
print("Suhu saat ini adalah", reamur, "Reamur")

celcius = (fahrenheit - 32) * (5/9)
print("Suhu saat ini adalah", celcius, "Celcius")


kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("Suhu saat ini adalah", kelvin, "Kelvin")
print ("========================")

