# Struktur data: list of dictionary
mahasiswa = []

# Fungsi tambah data
def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")
    mahasiswa.append({"NIM": nim, "Nama": nama, "Jurusan": jurusan})
    print("Data berhasil ditambahkan.\n")

# Fungsi tampilkan semua data
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("Belum ada data mahasiswa.\n")
    else:
        print("\nDaftar Mahasiswa:")
        for mhs in mahasiswa:
            print(f"NIM: {mhs['NIM']}, Nama: {mhs['Nama']}, Jurusan: {mhs['Jurusan']}")
        print()

# Fungsi cari mahasiswa
def cari_mahasiswa():
    nim = input("Masukkan NIM yang dicari: ")
    for mhs in mahasiswa:
        if mhs["NIM"] == nim:
            print(f"Data ditemukan: Nama: {mhs['Nama']}, Jurusan: {mhs['Jurusan']}\n")
            return
    print("Data tidak ditemukan.\n")

# Fungsi hapus mahasiswa
def hapus_mahasiswa():
    nim = input("Masukkan NIM yang ingin dihapus: ")
    for mhs in mahasiswa:
        if mhs["NIM"] == nim:
            mahasiswa.remove(mhs)
            print("Data berhasil dihapus.\n")
            return
    print("Data tidak ditemukan.\n")

# Menu utama
def menu():
    while True:
        print("=== Menu Pengolahan Data Mahasiswa ===")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")

# Jalankan program
menu()

# def adalah fungsi
# fungsi adalah kumpulan2 perintah2 yg dapat di panggil berulang kali

# TAMBAH MAHASISWA MENGGUNAKAN LOOPING/FOR
# mahasiswa = [] - fungsinya adalah untuk membuat sebuah list kosong yang akan digunakan sebagai wadah penyimpanan data mahasiswa.

def tambah_mahasiswa():
    jumlah = int(input("Berapa banyak mahasiswa yang ingin ditambahkan? "))
    for i in range(jumlah):
        print(f"\nData Mahasiswa ke-{i+1}")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        mahasiswa.append({"NIM": nim, "Nama": nama, "Jurusan": jurusan})
    print(f"\n{jumlah} data mahasiswa berhasil ditambahkan!\n")

# for mhs in mahasiswa:
#     if mhs["Nim"] == nim:
#         print("❌ Nim sudah terdaftar. Gunakan Nim lain.")
#     return