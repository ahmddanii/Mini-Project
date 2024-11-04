# Mini-Project
## Nama : Ahmad Dani
## NIM : 2409116074
## Kelas : Kelas B

## Program menghitung total harga barang berdasarkan harga barang dan jumlah pembelian.

FLowchart :
![Program menghitung jumlah barang](https://github.com/user-attachments/assets/1abe8754-3e22-4182-88ed-d3bdca6192a4)

Hasil Program  
![Capture](https://github.com/user-attachments/assets/d61d2b7e-a1ff-474b-ae1a-218a4efaf389)

''' python 
Penjelasan baris code : 
import getpass\n
menggunakan modul getpass untuk menyembunyikan password saat login\n
\n
print("---------Silahkan Register---------")\n
r_username = input("Masukkan Username: ")\n
r_nim = input("Masukkan NIM: ")\n
print("\n------Berhasil Register------")\n
proses register dengan menginputkan nama dan nim sebagai password\n
\n
l_username = input("Masukkan Username: ")\n
l_nim = getpass.getpass("Masukkan NIM: ")\n
proses login menggunakan username dan nim yang sudah di register tadi\n
\n
if l_username == r_username and l_nim == r_nim:\n
    print("Login berhasil, Selamat Datang " + r_username)\n
pengecekan apakah username yang diinput sesuai dengan yang diregister\n
    repeat_program = 'y'\n
    while repeat_program.lower() == "y":\n
membuat kondisi perulangan program\n
        # Input harga barang\n
        harga_barang = float(input("Masukkan Harga Barang: "))\n
        # Input jumlah barang\n
        jumlah_barang = int(input("Masukkan Jumlah Barang: "))\n
menginput jumlah barang dan harga barang\n
        # Menghitung total harga\n
        total_barang = harga_barang * jumlah_barang\n
menghitung total harga dari harga dan jumlah barang yang diinput\n
        # Pengecekan untuk diskon\n
        if total_barang > 250000:\n
percabangan jika total barang lebih dari Rp. 250.000 maka akan memberikan diskon 25%\n
            diskon = 0.25 * total_barang\n
            harga_setelah_diskon = total_barang - diskon\n
            print("Total harga sebelum diskon: ", total_barang)\n
            print("Diskon: 25% -Rp", diskon)\n
            print("Total harga setelah diskon: ", harga_setelah_diskon)\n
        else:\n
percabangan jika total barang kurang dari Rp. 250.000\n
            print("Total harga: ", total_barang)\n
\n
        # Menanyakan kepada pengguna jika ingin menghitung lagi\n
        repeat_program = input("Apakah Anda ingin menghitung lagi? (y/n): ")\n
menanyakan apakah ingin mengulang program lagi\n
    # Pesan terima kasih jika keluar dari loop\n
    print("Terima kasih telah menghitung menggunakan program ini")\n
jika tidak ingin mengulang maka akan muncul pesan ini\n
else:\n
    print("Login gagal! Username atau NIM salah.")\n
jika print tidak berhasil akan muncul pesan ini\n
'''
