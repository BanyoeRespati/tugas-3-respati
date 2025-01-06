import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambah kontak
def tambah_kontak():
    nama = nama_kontak.get()
    nomor = nomor_kontak.get()

    if nama and nomor:
        with open("kontak_pribadi.txt", "a") as file:
            file.write(f"{nama},{nomor}\n")
        nama_kontak.delete(0, tk.END)
        nomor_kontak.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Kontak berhasil ditambahkan!")
        tampilkan_kontak()
    else:
        messagebox.showwarning("Input tidak lengkap", "Harap masukkan nama dan nomor.")

# Fungsi untuk menampilkan semua kontak
def tampilkan_kontak():
    list_kontak.delete(0, tk.END)
    try:
        with open("kontak_pribadi.txt", "r") as file:
            for baris in file:
                list_kontak.insert(tk.END, baris.strip())
    except FileNotFoundError:
        messagebox.showwarning("File tidak ditemukan", "File kontak belum ada.")

# Fungsi untuk menghapus kontak
def hapus_kontak():
    kontak_terpilih = list_kontak.get(tk.ACTIVE)
    if kontak_terpilih:
        hapus_nama = kontak_terpilih.split(",")[0]
        
        with open("kontak_pribadi.txt", "r") as file:
            kontak = file.readlines()
        
        with open("kontak_pribadi.txt", "w") as file:
            for baris in kontak:
                if baris.split(",")[0] != hapus_nama:
                    file.write(baris)
        
        messagebox.showinfo("Sukses", f"Kontak {hapus_nama} berhasil dihapus.")
        tampilkan_kontak()
    else:
        messagebox.showwarning("Pilih Kontak", "Harap pilih kontak yang ingin dihapus.")

# Menampilkan GUI nya
root = tk.Tk()
root.title("Pengelola Kontak Pribadi")

# Label dan input untuk nama dan nomor telepon
label_nama = tk.Label(root, text="Nama:")
label_nama.grid(row=0, column=0, padx=10, pady=10)

nama_kontak = tk.Entry(root)
nama_kontak.grid(row=0, column=1, padx=10, pady=10)

label_nomor = tk.Label(root, text="Nomor Telepon:")
label_nomor.grid(row=1, column=0, padx=10, pady=10)

nomor_kontak = tk.Entry(root)
nomor_kontak.grid(row=1, column=1, padx=10, pady=10)

# Tombol untuk menambah kontak
tombol_tambah = tk.Button(root, text="Tambah Kontak", command=tambah_kontak)
tombol_tambah.grid(row=2, column=0, columnspan=2, pady=10)

# List kontak untuk menampilkan kontak yang ada
list_kontak = tk.Listbox(root, width=50, height=10)
list_kontak.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Tombol untuk menampilkan kontak
tombol_tampil = tk.Button(root, text="Tampilkan Kontak", command=tampilkan_kontak)
tombol_tampil.grid(row=4, column=0, columnspan=2, pady=10)

# Tombol untuk menghapus kontak
tombol_hapus = tk.Button(root, text="Hapus Kontak", command=hapus_kontak)
tombol_hapus.grid(row=5, column=0, columnspan=2, pady=10)

# Untuk menjalankan aplikasinya
root.mainloop()