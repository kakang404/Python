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
        print(f"\nData Mahasiswa ke-{i+1}")

        nim = input("Masukkan NIM: ")

        # validasi NIM
        for mhs in mahasiswa:
            if mhs["Nim"] == nim:
                print("❌ NIM sudah terdaftar. Gunakan NIM lain.")
                return

        nama = input("Masukkan Nama: ")
        jurusan = input("Masukkan Jurusan: ")
        alamat = input("Masukkan Alamat: ")
        jk = input("Masukkan Jenis Kelamin: ")

        mahasiswa.append({
            "Nama": nama,
            "Nim": nim,
            "Jurusan": jurusan,
            "Alamat": alamat,
            "Jenis Kelamin": jk
        })

    print(f"\n✅ {jumlah} data mahasiswa berhasil ditambahkan!")

# Fungsi menampilkan data mahasiswa
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("\n❌ Belum ada data mahasiswa.")
    else:
        print("\n====================== DAFTAR MAHASISWA ======================")
        df = pd.DataFrame((mahasiswa))
        print(df.to_string())
        print("==============================================================")

# Fungsi cari mahasiswa
def cari_mahasiswa():
    nim = input("\nMasukkan NIM yang dicari: ")

    hasil = [mhs for mhs in mahasiswa if mhs["Nim"] == nim]

    if hasil:
        print("\n====================== DATA DITEMUKAN ======================")
        df = pd.DataFrame(hasil)
        print(df.to_string())
        print("==============================================================")
    else:
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

# MENU UTAMA
def menu():
    while True:
        print("\n==============================================")
        print("      MENU PENGELOLAAN DATA MAHASISWA")
        print("==============================================")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Export ke Excel (Auto Save)")
        print("6. Download Hasil Data ke Excel")
        print("7. Keluar")
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == "1":
            tambah_mahasiswa()
        elif pilihan == "2":
            tampilkan_mahasiswa()
        elif pilihan == "3":
            cari_mahasiswa()
        elif pilihan == "4":
            hapus_mahasiswa()
        elif pilihan == "5":
            df = pd.DataFrame(mahasiswa)
            df.to_excel("data_mahasiswa.xlsx", index=False)
            print("\n📁 File berhasil disimpan sebagai data_mahasiswa.xlsx")
        elif pilihan == "6":
            if not mahasiswa:
                print("\n❌ Tidak ada data untuk di-download.")
            else:
                df = pd.DataFrame(mahasiswa)
                df.to_excel("download_data_mahasiswa.xlsx", index=False)
                print("\n📥 File BERHASIL di-download sebagai:")
                print("➡ download_data_mahasiswa.xlsx")
        elif pilihan == "7":
            print("Terima kasih!")
            break
        else:
            print("\n❌ Pilihan tidak valid.\n")

# Login
def login():
    print("\n======================================")
    print("           HALAMAN LOGIN")
    print("======================================")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"✅ Login berhasil! Selamat datang, {username}")
        menu()
    else:
        print("❌ Login gagal. Username atau password salah.")
        login()

login()
