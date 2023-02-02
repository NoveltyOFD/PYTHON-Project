# Python Project Pacmann - Super Cashier
Kasir self-service sistem sederhana dengan menggunakan bahasa pemrograman Python

# Tujuan Pengerjaan Project
Kasir self-service sistem adalah program untuk menyimpan informasi belanja customer. Sistem ini digunakan untuk mensupport kegiatan operasional harian di supermarket.

# Requirement atau Objektif
Bahasa pemrograman: Python 

Fitur yang dibutuhkan:
  1. Customer dapat memasukkan data diri
  2. Customer dapat memasukkan item yang akan dibeli
  3. Customer dapat melakukan mengubah informasi belanja seperti jumlah barang, harga barang, nama barang
  4. Customer dapat menghapus barang tertentu atau menghapus keseluruhan daftar belanja
  5. Customer dapat melihat daftar belanja terbaru
  6. Customer dapat melihat total harga belanja

# Flow chart

![image](https://user-images.githubusercontent.com/25927592/216376212-ff2a9177-e69c-478f-b4b5-7f9643cb8b62.png)

# Deskripsi Fungsi dan Kelas
  1. Kelas dataPembelianPerItem: Kelas untuk menampung informasi harga barang dan jumlah barang
  2. Fungsi masukkanDaftarBelanja : Untuk memasukkan daftar belanja
  3. Fungsi printDaftarBelanja : Untuk menampilkan daftar belanja
  4. Fungsi ubahInformasiBarang_jumlah_harga : Untuk mengubah informasi jumlah atau harga barang
  5. Fungsi ubahInformasiBarang_nama : Untuk mengubah nama barang
  6. Fungsi hapusBarangTertentu : Untuk menghapus barang tertentu
  7. Fungsi hapusBarangKeseluruhan : Untuk menghapus barang keseluruhan
  8. Fungsi ubahDaftarBelanja : Untuk menampilan pilihan menu mengubah daftar belanja
  9. Fungsi totalBelanja : Untuk menghitung dan menampilkan total belanja
  10. Fungsi tampilanMenu : Untuk menampilkan pilihan menu dalam menu utama
  11. Fungsi menu : Program utama

# Demonstrasi Code dan Test Case
1. Masukkan nama diri
![image](https://user-images.githubusercontent.com/25927592/216103086-e22381a5-ae1f-493d-8393-2dc25f8747ae.png)

2. Pilih menu masukkan daftar belanja
![image](https://user-images.githubusercontent.com/25927592/216103339-ff23d45f-e699-4368-9a3b-6a3190cd9e04.png)

3. Masukkan informasi nama barang, harga barang, dan jumlah barang
![image](https://user-images.githubusercontent.com/25927592/216104050-e386f211-622e-415f-b202-503df7115bfe.png)
![image](https://user-images.githubusercontent.com/25927592/216104133-ef44cfe1-7c31-4827-8ef7-7d29f80f380f.png)
![image](https://user-images.githubusercontent.com/25927592/216104266-313952fe-765b-4d00-bf13-91db843e5445.png)

4. Jika ingin menambah informasi data belanja, pilih menu no. 1 dan masukkan daftar belanja lainnya seperti sebelumnya
![image](https://user-images.githubusercontent.com/25927592/216104553-948284de-f70f-417d-bd27-039f79a7104f.png)
![image](https://user-images.githubusercontent.com/25927592/216105809-52dbe2da-aca6-438a-8992-7e2d904c1320.png)
![image](https://user-images.githubusercontent.com/25927592/216106751-4784d6e9-743a-43e4-a9a6-902efd6c9843.png)

5. Jika daftar belanja sudah dimasukkan semua, pilih opsi no. 2
![image](https://user-images.githubusercontent.com/25927592/216107233-9f55a76b-54e4-49c4-9dfc-f6cc909987a0.png)
![image](https://user-images.githubusercontent.com/25927592/216107366-3bd3074b-22b5-4061-a107-26c0e9bba9c1.png)

6. Jika ada daftar belanja yang ingin diupdate, pilih menu no. 2
![image](https://user-images.githubusercontent.com/25927592/216107569-0de8e1bb-7c4d-486b-865e-ec33902f2ac7.png)
untuk menghapus barang, pilih menu 4
![image](https://user-images.githubusercontent.com/25927592/216108253-cd581dff-fd64-4553-b2c2-8c840712e593.png)

7. Tampilkan daftar barang belanja saat ini dengan memilih menu no. 3
![image](https://user-images.githubusercontent.com/25927592/216108589-296e2151-c42b-4317-88bc-4813bf582a89.png)

8. Untuk menghitung total belanja, pilih menu no.4
![image](https://user-images.githubusercontent.com/25927592/216108738-4f6e7fbd-91ea-49b3-812b-f411905c0f37.png)

9. Untuk menghapus semua daftar belanja, pilih menu no.2
![image](https://user-images.githubusercontent.com/25927592/216108990-e559907a-ddd8-4764-9d26-0ce427185690.png)
lalu, pilih menu no.5
![image](https://user-images.githubusercontent.com/25927592/216109120-95ae5873-aad0-48ad-9cbe-225ce51b2df9.png)

10. Tampilkan daftar belanja setelah dihapus dengan memilih menu no. 3
![image](https://user-images.githubusercontent.com/25927592/216109310-a3d938a8-af14-4feb-aeaf-95ae4fd65f67.png)
