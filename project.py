import pandas as pd

users = {
    "admin": "123",
    "aldi": "321"
}

mahasiswa = []

# Fungsi tambah mahasiswa
def tambah_mahasiswa():
    jumlah = int(input("Berapa banyak mahasiswa yang ingin ditambahkan? "))
    for i in range(jumlah):
        print(f"\nData Mahasiswa ke - {i+1}")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        alamat = input("Masukkan Alamat: ")
        jk = input("Masukkan Jenis Kelamin: ")
        mahasiswa.append({"Nama": nama, "Nim": nim, "Jurusan": jurusan, "Alamat": alamat, "Jenis Kelamin": jk})
    print(f"\n{jumlah} ✅ Data mahasiswa berhasil ditambahkan!")

    # validasi agar nim mahasiswa tidak sama/double 
    for mhs in mahasiswa:
        if mhs["Nim"] == nim:
            print("❌ Nim sudah terdaftar. Gunakan Nim lain.")
        return
        
# Fungsi menampilkan data mahasiswa
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("\n❌ Belum ada data mahasiswa.")
    else:
        print("\n                                               Halaman Daftar Mahasiswa")
        print("===================================================================================================================")
        print(f"{'No':<5} {'Nama':<20} {'Nim':<20} {'Jurusan':<20} {'Alamat':<20} {'Jenis Kelamin':<20}")
        print("===================================================================================================================")
        for i, mhs in enumerate(mahasiswa, start = 1):
            print(f"{i:<5} {mhs['Nama']:<20} {mhs['Nim']:<20} {mhs['Jurusan']:<20} {mhs['Alamat']:<20} {mhs['Jenis Kelamin']:<20}")


# Fungsi cari mahasiswa
def cari_mahasiswa():
    nim = input("\nMasukkan Nim yang dicari: ")
    print("\n=====================================================================================================================")
    print("                                                     Halaman Cari Mahasiswa")
    print("=======================================================================================================================")
    print(f"{'No':<5} {'Nama':<20} {'Nim':<20} {'Jurusan':<20} {'Alamat':<20} {'Jenis Kelamin':<20}")
    print("=======================================================================================================================")
    for i, mhs in enumerate(mahasiswa, start = 1):
        if mhs["Nim"] == nim:
            print(f"{i:<5} {mhs['Nama']:<20} {mhs['Nim']:<20} {mhs['Jurusan']:<20}")
            return
    print("\n❌ Data tidak ditemukan.")

# Fungsi hapus mahasiswa
def hapus_mahasiswa():
    nim = input("\nMasukkan NIM yang ingin dihapus: ")
    for mhs in mahasiswa:
        if mhs["Nim"] == nim:
            mahasiswa.remove(mhs)
            print("\n✅ Data berhasil dihapus.")
            return
    print("\n❌ Data tidak ditemukan.")

def menu():
    while True:
        print("\n==============================================")
        print("      MENU PENGELOLAAN DATA MAHASISWA")
        print("==============================================")
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
            print("\n❌ Pilihan tidak valid.\n")

def login():
    print("\n======================================")
    print("           HALAMAN LOGIN")
    print("======================================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print("✅ Login berhasil! Selamat datang,", username)
        menu()
    else:
        print("❌ Login gagal. Username atau password salah.")
        login()

login()