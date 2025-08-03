def penjumlahan(a, b):
  return a + b
  
def pengurangan (a, b):
  return a - b

def perkalian (a, b):
  return a * b

def pembagian (a, b):
  if b == 0:
    return "Error! Pembagian tidak dapat dilakukan karena pembagi adalah 0."
  else:
    return a / b


# Langsung eksekusi tanpa if __name__
print("🔢 KALKULATOR SEDERHANA 🔢")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
hasil = penjumlahan(angka1, angka2)
print(f"Hasil penambahan: {hasil}")
