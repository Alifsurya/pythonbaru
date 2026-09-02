print ("===========================")
print ("|| Program Konversi Suhu ||")
print ("===========================")
print ("\n")
print ("========================")
kelvin = float(input('Masukkan suhu'))
print("Suhu saat ini adalah", kelvin, "Kelvin")

celcius = kelvin - 273.15
print("Suhu saat ini adalah", celcius, "Celcius")

fahrenheit = ((kelvin - 273.15) * 9/5) + 32
print("Suhu saat ini adalah", fahrenheit, "Fahrenheit")

reamur = (4/5) * (kelvin-273)
print("Suhu saat ini adalah", reamur, "Reamur")
print ("========================")

