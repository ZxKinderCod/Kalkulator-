from jumlah import penjumlahan
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
            print("Fitur pengurangan belum tersedia")
    elif pilihan == "3":
            print("Fitur perkalian belum tersedia")
    elif pilihan == "4":
            print("Fitur pembagian belum tersedia")
    elif pilihan == "5":
            print("Terima kasih telah menggunakan kalkulator!")

menu()