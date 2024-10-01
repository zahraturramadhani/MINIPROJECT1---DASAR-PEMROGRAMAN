# Login Sederhana menggunakan Nama, NIM, Password

# Masukkan Nama Anda
Nama = str(input("Masukkan Nama Anda:"))

# Masukkan NIM Anda dan wajib menggunakan angka
while True:
            try:
               NIM = int(input("Masukkan NIM Anda:"))
               break  # Keluar dari loop jika NIM valid (berupa integer)
            except ValueError:
               print('=========== NIM harus berupa angka! Silahkan Input NIM Anda Kembali!!! ===========')

# Masukan Password yang terdiri dari 8 angka dan tidak boleh lebih
while True:
   try:
      Password = input('Masukkan Password Anda (8 Angka): ')
      if len(Password) != 8 or not Password.isdigit():  
            raise ValueError
   except ValueError:
      print('===========Password yang Anda masukkan salah===========')
      print('===========Password harus terdiri dari 8 angka===========')
      continue  
   break # Keluar dari loop jika Password valid
      
print(f"Hello!, Selamat Datang {Nama} dengan NIM {NIM} dan password {Password} diaplikasi kami")
print("\n")  # Menambahkan Space line baru

# Menghitung total harga berdasarkan harga barang dan jumlah pembelian
harga_barang = int(input("Masukkan harga barang: "))
jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

# Menghitung total harga
total_harga = harga_barang * jumlah_pembelian
print(f"Menampilkan total harga: Rp {total_harga:.2f}")

# Mengecek Apakah total harga lebih dari 250000
if total_harga > 250000:
   diskon = total_harga * 0.25
   total_harga_diskon = total_harga - diskon
   print(f"Selamat Anda Mendapatkan diskon sebesar 25%: Rp {diskon:.2f}")
   print(f"total harga setelah diskon: Rp. {total_harga_diskon:.2f}")
else:
      print(f"Maaf Anda tidak mendapatkan diskon dikarenakan total harga kurang dari 250000 ")
      print(f"total harga: Rp. {total_harga:.2f}")
      print("\n")  # Menambahkan Space line baru

# Apakah Anda Mau Menghitung Lagi atau Keluar dari Aplikasi
pilihan = input("Apakah Anda ingin menghitung lagi? (y/t): ").lower()
if pilihan != 'y':
      print("Terima kasih telah menggunakan aplikasi ini. Program selesai.")
      
   


   



      


      


         
         


    
      
         






         



