import pandas as pd

mahasiswa = []

# Fungsi untuk memastikan input tidak boleh kosong
def input_wajib(pesan):
    data = input(pesan).strip()
    while data == "":
        print("❌ Input tidak boleh kosong!")
        data = input(pesan).strip()
    return data

def input_angka(pesan):
    while True:
        nilai = input(pesan)
        if nilai.isdigit():      
            return nilai
        print("❗ Input harus berupa angka dan tidak boleh kosong!")

# Fungsi tambah mahasiswa
def tambah_mahasiswa():
    jumlah = int(input("Berapa banyak mahasiswa yang ingin ditambahkan? "))

    for i in range(jumlah):
        print(f"\n--- Data Mahasiswa ke-{i+1} ---")

        # Input NIM (wajib diisi)
        nim     = input_angka("Masukkan NIM             : ")

        # Cek apakah NIM sudah ada
        for mhs in mahasiswa:
            if mhs["NIM"] == nim:
                print("❌ NIM sudah terdaftar. Gunakan NIM lain.")
                return

        # Input data lainnya (wajib diisi)
        nama    = input_wajib("Masukkan Nama            : ")
        jurusan = input_wajib("Masukkan Jurusan         : ")
        alamat  = input_wajib("Masukkan Alamat          : ")
        jk      = input_wajib("Masukkan Jenis Kelamin   : ")

        # Simpan data ke list
        mahasiswa.append({
            "NIM": nim,
            "Nama": nama,
            "Jurusan": jurusan,
            "Alamat": alamat,
            "Jenis Kelamin": jk
        })

    print(f"✅ {jumlah} data mahasiswa berhasil ditambahkan!")

# Fungsi menampilkan data mahasiswa
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("❌ Belum ada data mahasiswa.")
    else:
        print("\n\n\n" + "=" * 50)
        print("DAFTAR MAHASISWA".center(50))
        print("=" * 50)
        df = pd.DataFrame((mahasiswa))
        print(df.to_string())
        print("=" * 50)

# Fungsi cari mahasiswa
def cari_mahasiswa():
    nim = input("\nMasukkan NIM yang dicari: ")

    hasil = [mhs for mhs in mahasiswa if mhs["NIM"] == nim]

    if hasil:
        print("\n\n\n" + "=" * 50)
        print("DAFTAR DATA DITEMUKAN".center(50))
        print("=" * 50)
        df = pd.DataFrame((hasil))
        print(df.to_string())
        print("=" * 50)
    else:
        print("❌ Data tidak ditemukan.")

# Fungsi hapus mahasiswa
def hapus_mahasiswa():
    nim = input("\nMasukkan NIM yang ingin dihapus: ")

    for mhs in mahasiswa:
        if mhs["NIM"] == nim:
            mahasiswa.remove(mhs)
            print("\n✅ Data berhasil dihapus.")
            return

    print("❌ Data tidak ditemukan.")

# Funsi edit mahasiswa
def edit_mahasiswa():
    if len(mahasiswa) == 0:
        print("❌ Belum ada data mahasiswa!")
        return

    print("\n" + "=" * 50)
    print("EDIT DATA MAHASISWA".center(50))
    print("=" * 50)
    
    cari_nim = input_angka("Masukkan NIM mahasiswa yang ingin diedit: ")

    # Cari mahasiswa berdasarkan NIM
    for mhs in mahasiswa:
        if mhs["NIM"] == cari_nim:

            print("\nMahasiswa ditemukan!")
            print(f"Nama            : {mhs['Nama']}")
            print(f"Jurusan         : {mhs['Jurusan']}")
            print(f"Alamat          : {mhs['Alamat']}")
            print(f"Jenis Kelamin   : {mhs['Jenis Kelamin']}")

            print("\nPilih data yang ingin diedit:")
            print("1. Nama")
            print("2. Jurusan")
            print("3. Alamat")
            print("4. Jenis Kelamin")
            print("5. Batal")

            pilihan = input("Masukkan pilihan (1-5): ")

            if pilihan == "1":
                mhs["Nama"] = input_wajib("Masukkan nama baru: ")
                print("✅ Nama berhasil diperbarui!")

            elif pilihan == "2":
                mhs["Jurusan"] = input_wajib("Masukkan jurusan baru: ")
                print("✅ Jurusan berhasil diperbarui!")

            elif pilihan == "3":
                mhs["Alamat"] = input_wajib("Masukkan alamat baru: ")
                print("✅ Alamat berhasil diperbarui!")

            elif pilihan == "4":
                mhs["Jenis Kelamin"] = input_wajib("Masukkan jenis kelamin baru: ")
                print("✅ Jenis kelamin berhasil diperbarui!")

            elif pilihan == "5":
                print("❗ Edit dibatalkan.")
                return

            else:
                print("❌ Pilihan tidak valid!")

            return

    print("❌ NIM tidak ditemukan!")

# MENU UTAMA
def menu():
    while True:
        print("\n\n\n" + "=" * 50)
        print("MENU PENGELOLAAN DATA MAHASISWA".center(50))
        print("=" * 50)
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Edit Mahasiswa")
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
            edit_mahasiswa()
        elif pilihan == "6":
            if not mahasiswa:
                print("\n❌ Tidak ada data untuk di-download.")
            else:
                df = pd.DataFrame(mahasiswa)
                df.to_excel("download_data_mahasiswa.xlsx", index=False)
                print("\n📥 File BERHASIL di-download sebagai:")
                print("📁 download_data_mahasiswa.xlsx")
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

    if username == "admin" and password == "123":
        print(f"✅ Login berhasil! Selamat datang, {username}")
        menu()
    else:
        print("❌ Login gagal. Username atau password salah.")
        login()

login()
