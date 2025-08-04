from jumlah import penjumlahan
from kali import perkalian
from kurang import pengurangan
from bagi import pembagian
def menu():
    print("\n🔢 KALKULATOR SEDERHANA 🔢")
    print("1. Penjumlahan")
    print("2. Pengurangan") 
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        penjumlahan ()
    elif pilihan == "2":
         pengurangan()
    elif pilihan == "3":
            perkalian()
    elif pilihan == "4":
            pembagian()
    elif pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator!")


def main():
        while True:
                menu()

if __name__ == "__main__":
        main()