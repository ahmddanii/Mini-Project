# Mini-Project
## Nama : Ahmad Dani
## NIM : 2409116074
## Kelas : Kelas B

## Program menghitung total harga barang berdasarkan harga barang dan jumlah pembelian.

FLowchart :
![Program menghitung jumlah barang](https://github.com/user-attachments/assets/1abe8754-3e22-4182-88ed-d3bdca6192a4)

Hasil Program  
![Capture](https://github.com/user-attachments/assets/d61d2b7e-a1ff-474b-ae1a-218a4efaf389)

Penjelasan baris code : 
import getpass
menggunakan modul getpass untuk menyembunyikan password saat login

print("---------Silahkan Register---------")
r_username = input("Masukkan Username: ")
r_nim = input("Masukkan NIM: ")
print("\n------Berhasil Register------")
proses register dengan menginputkan nama dan nim sebagai password

l_username = input("Masukkan Username: ")
l_nim = getpass.getpass("Masukkan NIM: ")
proses login menggunakan username dan nim yang sudah di register tadi

if l_username == r_username and l_nim == r_nim:
    print("Login berhasil, Selamat Datang " + r_username)
pengecekan apakah username yang diinput sesuai dengan yang diregister
    repeat_program = 'y'
    while repeat_program.lower() == "y":
membuat kondisi perulangan program
        # Input harga barang
        harga_barang = float(input("Masukkan Harga Barang: "))
        # Input jumlah barang
        jumlah_barang = int(input("Masukkan Jumlah Barang: "))
menginput jumlah barang dan harga barang
        # Menghitung total harga
        total_barang = harga_barang * jumlah_barang
menghitung total harga dari harga dan jumlah barang yang diinput
        # Pengecekan untuk diskon
        if total_barang > 250000:
percabangan jika total barang lebih dari Rp. 250.000 maka akan memberikan diskon 25%
            diskon = 0.25 * total_barang
            harga_setelah_diskon = total_barang - diskon
            print("Total harga sebelum diskon: ", total_barang)
            print("Diskon: 25% -Rp", diskon)
            print("Total harga setelah diskon: ", harga_setelah_diskon)
        else:
percabangan jika total barang kurang dari Rp. 250.000
            print("Total harga: ", total_barang)

        # Menanyakan kepada pengguna jika ingin menghitung lagi
        repeat_program = input("Apakah Anda ingin menghitung lagi? (y/n): ")
menanyakan apakah ingin mengulang program lagi
    # Pesan terima kasih jika keluar dari loop
    print("Terima kasih telah menghitung menggunakan program ini")
jika tidak ingin mengulang maka akan muncul pesan ini
else:
    print("Login gagal! Username atau NIM salah.")
jika print tidak berhasil akan muncul pesan ini
