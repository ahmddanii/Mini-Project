import getpass

print("---------Silahkan Register---------")

r_username = input("Masukkan Username: ")
r_nim = input("Masukkan NIM: ")
print("\n------Berhasil Register------")

l_username = input("Masukkan Username: ")
l_nim = getpass.getpass("Masukkan NIM: ")

if l_username == r_username and l_nim == r_nim:
    print("Login berhasil, Selamat Datang " + r_username)

    repeat_program = 'y'
    while repeat_program.lower() == "y":
        # Input harga barang
        harga_barang = float(input("Masukkan Harga Barang: "))
        # Input jumlah barang
        jumlah_barang = int(input("Masukkan Jumlah Barang: "))
        
        # Menghitung total harga
        total_barang = harga_barang * jumlah_barang

        # Pengecekan untuk diskon
        if total_barang > 250000:
            diskon = 0.25 * total_barang
            harga_setelah_diskon = total_barang - diskon
            print("Total harga sebelum diskon: ", total_barang)
            print("Diskon: 25% -Rp", diskon)
            print("Total harga setelah diskon: ", harga_setelah_diskon)
        else:
            print("Total harga: ", total_barang)

        # Menanyakan apakah ingin menghitung lagi
        repeat_program = input("Apakah Anda ingin menghitung lagi? (y/n): ")

    # Pesan terima kasih jika keluar dari loop
    print("Terima kasih telah menghitung menggunakan program ini")
else:
    print("Login gagal! Username atau NIM salah.")
