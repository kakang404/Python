import pandas as pd

# Data login user
users = {
    "admin": "123",
    "aldi": "321"
}

# DataFrame kosong untuk menyimpan data mahasiswa
mahasiswa = pd.DataFrame(columns=["NIM", "Nama", "Jurusan"])

# Fungsi tambah mahasiswa
def tambah_mahasiswa():
    global mahasiswa
    jumlah = int(input("Berapa banyak mahasiswa yang ingin ditambahkan? "))
    
    for i in range(jumlah):
        print(f"\nData Mahasiswa ke-{i+1}")
        nim = input("Masukkan NIM: ")

        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")

        # Tambahkan data ke DataFrame
        data_baru = pd.DataFrame({"NIM": [nim], "Nama": [nama], "Jurusan": [jurusan]})
        mahasiswa = pd.concat([mahasiswa, data_baru], ignore_index=True)

        # Validasi agar NIM tidak ganda
        if nim in mahasiswa["NIM"].values:
            print("❌ NIM sudah terdaftar. Gunakan NIM lain.")
        break
        
    
    print(f"\n✅ {jumlah} data mahasiswa berhasil ditambahkan!")

# Fungsi tampilkan semua mahasiswa
def tampilkan_mahasiswa():
    if mahasiswa.empty:
        print("\n❌ Belum ada data mahasiswa.")
    else:
        print("\n============= DAFTAR MAHASISWA =============")
        print(mahasiswa.to_string(index=False))
        print("============================================")

# Fungsi cari mahasiswa berdasarkan NIM
def cari_mahasiswa():
    nim = input("\nMasukkan NIM yang dicari: ")
    hasil = mahasiswa[mahasiswa["NIM"] == nim]
    
    if not hasil.empty:
        print("\n============= HASIL PENCARIAN =============")
        print(hasil.to_string(index=False))
        print("===========================================")
    else:
        print("\n❌ Data tidak ditemukan.")

# Fungsi hapus mahasiswa
def hapus_mahasiswa():
    global mahasiswa
    nim = input("\nMasukkan NIM yang ingin dihapus: ")
    
    if nim in mahasiswa["NIM"].values:
        mahasiswa = mahasiswa[mahasiswa["NIM"] != nim]
        print("\n✅ Data berhasil dihapus.")
    else:
        print("\n❌ Data tidak ditemukan.")

# Menu utama
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
            print("👋 Terima kasih telah menggunakan program ini.")
            break
        else:
            print("\n❌ Pilihan tidak valid.\n")

# Fungsi login
def login():
    print("\n======================================")
    print("           HALAMAN LOGIN")
    print("======================================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"✅ Login berhasil! Selamat datang, {username}.")
        menu()
    else:
        print("❌ Login gagal. Username atau password salah.")
        login()

# Jalankan program
login()
