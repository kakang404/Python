import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Data pengguna untuk login
users = {
    "admin": "123",
    "aldi": "321"
}

# Data mahasiswa
mahasiswa = pd.DataFrame(columns=["NIM", "Nama", "Jurusan"])

# ----------------- Fungsi utama -----------------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for i, row in mahasiswa.iterrows():
        tree.insert("", "end", values=(row["NIM"], row["Nama"], row["Jurusan"]))

def tambah_data():
    global mahasiswa
    nim = entry_nim.get().strip()
    nama = entry_nama.get().strip()
    jurusan = entry_jurusan.get().strip()

    if not nim or not nama or not jurusan:
        messagebox.showwarning("Peringatan", "Semua field harus diisi!")
        return

    if nim in mahasiswa["NIM"].values:
        messagebox.showerror("Error", "❌ NIM sudah terdaftar!")
        return

    mahasiswa = pd.concat([mahasiswa, pd.DataFrame({"NIM": [nim], "Nama": [nama], "Jurusan": [jurusan]})], ignore_index=True)
    refresh_table()
    entry_nim.delete(0, tk.END)
    entry_nama.delete(0, tk.END)
    entry_jurusan.delete(0, tk.END)
    messagebox.showinfo("Sukses", "✅ Data mahasiswa berhasil ditambahkan!")

def hapus_data():
    global mahasiswa
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
        return

    nim = tree.item(selected[0])["values"][0]
    mahasiswa = mahasiswa[mahasiswa["NIM"] != nim]
    refresh_table()
    messagebox.showinfo("Sukses", "✅ Data berhasil dihapus!")

def cari_data():
    nim_cari = entry_cari.get().strip()
    hasil = mahasiswa[mahasiswa["NIM"].str.contains(nim_cari, case=False, na=False)]

    for row in tree.get_children():
        tree.delete(row)
    for i, row in hasil.iterrows():
        tree.insert("", "end", values=(row["NIM"], row["Nama"], row["Jurusan"]))

def reset_tabel():
    refresh_table()
    entry_cari.delete(0, tk.END)

# ----------------- Login Window -----------------
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Sukses", f"Selamat datang, {username}!")
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror("Gagal", "Username atau password salah!")

# ----------------- Main Window -----------------
def main_window():
    global entry_nim, entry_nama, entry_jurusan, entry_cari, tree

    root = tk.Tk()
    root.title("📘 Sistem Data Mahasiswa")
    root.geometry("720x480")
    root.configure(bg="#f0f4f8")

    # Judul
    tk.Label(root, text="Data Mahasiswa", font=("Arial", 18, "bold"), bg="#f0f4f8").pack(pady=10)

    # Frame input
    frame_input = tk.Frame(root, bg="#f0f4f8")
    frame_input.pack(pady=5)

    tk.Label(frame_input, text="NIM:", bg="#f0f4f8").grid(row=0, column=0, padx=5, pady=5)
    entry_nim = tk.Entry(frame_input, width=20)
    entry_nim.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_input, text="Nama:", bg="#f0f4f8").grid(row=0, column=2, padx=5, pady=5)
    entry_nama = tk.Entry(frame_input, width=20)
    entry_nama.grid(row=0, column=3, padx=5, pady=5)

    tk.Label(frame_input, text="Jurusan:", bg="#f0f4f8").grid(row=0, column=4, padx=5, pady=5)
    entry_jurusan = tk.Entry(frame_input, width=20)
    entry_jurusan.grid(row=0, column=5, padx=5, pady=5)

    tk.Button(frame_input, text="Tambah", command=tambah_data, bg="#4caf50", fg="white").grid(row=0, column=6, padx=10)
    tk.Button(frame_input, text="Hapus", command=hapus_data, bg="#f44336", fg="white").grid(row=0, column=7, padx=10)

    # Frame cari
    frame_cari = tk.Frame(root, bg="#f0f4f8")
    frame_cari.pack(pady=10)
    tk.Label(frame_cari, text="Cari NIM:", bg="#f0f4f8").grid(row=0, column=0)
    entry_cari = tk.Entry(frame_cari, width=25)
    entry_cari.grid(row=0, column=1, padx=5)
    tk.Button(frame_cari, text="Cari", command=cari_data, bg="#2196f3", fg="white").grid(row=0, column=2, padx=5)
    tk.Button(frame_cari, text="Reset", command=reset_tabel, bg="#9c27b0", fg="white").grid(row=0, column=3, padx=5)

    # Tabel Mahasiswa
    tree = ttk.Treeview(root, columns=("NIM", "Nama", "Jurusan"), show="headings")
    tree.heading("NIM", text="NIM")
    tree.heading("Nama", text="Nama")
    tree.heading("Jurusan", text="Jurusan")
    tree.pack(pady=10, fill="both", expand=True)

    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.configure("Treeview", font=("Arial", 10))

    refresh_table()
    root.mainloop()

# ----------------- Login Window UI -----------------
login_window = tk.Tk()
login_window.title("Login Sistem Mahasiswa")
login_window.geometry("350x250")
login_window.configure(bg="#e3f2fd")

tk.Label(login_window, text="Login", font=("Arial", 18, "bold"), bg="#e3f2fd").pack(pady=10)
tk.Label(login_window, text="Username:", bg="#e3f2fd").pack()
entry_user = tk.Entry(login_window, width=25)
entry_user.pack(pady=5)

tk.Label(login_window, text="Password:", bg="#e3f2fd").pack()
entry_pass = tk.Entry(login_window, width=25, show="*")
entry_pass.pack(pady=5)

tk.Button(login_window, text="Login", command=login, bg="#2196f3", fg="white", width=15).pack(pady=15)
login_window.mainloop()
