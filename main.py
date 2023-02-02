#Mendefinisikan kelas yang berisi informasi data pembelian customer
class dataPembelianPerItem():
    def __init__(self):
        self.jumlahBarang = 0
        self.hargaBarang = 0
        
    def EnterData(self):
        """Fungsi untuk menambahkan informasi jumlah barang dan harga barang."""
        while True:
            try :
                self.jumlahBarang = int(input("Masukkan jumlah barang: "))
            except:
                print("Terdapat kesalahan input data, mohon input sesuai perintah\n")
                continue
            else:
                break

        while True:
            try :
                self.hargaBarang = int(input("Masukkan harga barang: "))
            except:
                print("Terdapat kesalahan input data, mohon input sesuai perintah\n")
                continue
            else:
                break
         

def masukkanDaftarBelanja(currentdaftarBelanja):
    """Fungsi untuk menambahkan daftar belanja customer."""
    
    informasiPerItem = dataPembelianPerItem()
    listInformasiPerItem = []
    jawab = 1
    #print(type(daftarBelanjaUpdated))
    print("============================= MASUKKAN DAFTAR BELANJA ================================")
    while jawab == 1:
        if currentdaftarBelanja != []:
            print("===================================")
        namaBarang_key = input('Masukkan nama barang: ') 
        daftarBelanja = {}
        listInformasiPerItem = []
        informasiPerItem.EnterData()
        listInformasiPerItem.append(informasiPerItem.jumlahBarang)
        listInformasiPerItem.append(informasiPerItem.hargaBarang)
        daftarBelanja = {namaBarang_key.lower() : listInformasiPerItem }
        currentdaftarBelanja.update(daftarBelanja)
        print("\nApakah semua data belanja sudah dimasukkan?")
        print("1. Belum")
        print("2. Sudah")
        while True:
            try :
                jawab = int(input("Masukkan jawaban (Masukkan 1 atau 2) : "))
            except:
                print("Terdapat kesalahan input data, mohon input sesuai perintah\n")
                continue
            else:
                break
    else:
        print("Pemesanan sudah benar")
        print("=============================================================")
    return currentdaftarBelanja

def printDaftarBelanja(currentdaftarBelanja):
    """Fungsi untuk menampilkan daftar belanja customer."""
    
    print("========================= TAMPILKAN DAFTAR BELANJA ====================================")
    if currentdaftarBelanja == {}:
        print("Daftar belanja masih kosong, silahkan pilih barang belanjaanmu terlebih dahulu.")
    else:
        print(currentdaftarBelanja)
    print("=============================================================================\n\n")

def ubahInformasiBarang_jumlah_harga(dict, key, indexValue, newValue):
    """Fungsi untuk mengubah informasi jumlah barang atau harga barang customer."""
    
    if key.lower() in dict.keys():
        print("Nama barang ditemukan")
        dict[key.lower()][indexValue] = newValue
        if indexValue == 0:
            print("========== Update jumlah %s berhasil ==========\n "%(key))
        elif indexValue == 1:
            print("========== Update harga %s berhasil ==========\n "%(key))       
    else:
        print("Nama barang tidak ditemukan, anda akan dialihkan ke menu utama")

def ubahInformasiBarang_nama(dict, key, newKey):
    """Fungsi untuk mengubah informasi nama barang customer."""
    newKey = newKey.lower()
    key = key.lower()
    if key in dict.keys():
        print("Nama barang ditemukan")
        dict[newKey] = dict.pop(key)
        print(f"========== Update harga {key} menjadi {newKey} berhasil ==========\n ")       
    else:
        print("Nama barang tidak ditemukan, anda akan dialihkan ke menu utama")

def hapusBarangTertentu(dict, key):
    """Fungsi untuk menghapus item tertentu dari daftar belanja customer."""
    
    if key.lower() in dict.keys():
        print("Nama barang ditemukan")
        dict.pop(key.lower())
        print("========== Barang %s berhasil dihapus ==========\n "%(key))
    else:
        print("Nama barang tidak ditemukan, anda akan dialihkan ke menu utama")

def hapusBarangKeseluruhan(dict):
    """Fungsi untuk menghapus seluruh daftar belanja customer."""
    dict.clear()
    print("========== Seluruh daftar barang berhasil dihapus ==========\n ")

def ubahDaftarBelanja(currentdaftarBelanja):
    """Fungsi untuk menampilkan daftar menu yang bertujuan untuk mengubah atau menghapus informasi barang di daftar belanja
    """
    print("========================= UPDATE DAFTAR BELANJA ===============================")
    print("Silahkan pilih menu daftar belanja yang akan diubah :")
    print("1. Ubah jumlah barang item tertentu")
    print("2. Ubah harga barang item tertentu")
    print("3. Ubah nama barang item tertentu")
    print("4. Hapus item tertentu")
    print("5. Hapus semua daftar belanja")
    print("6. Menu utama")
    
    while True:
        try :
            choice = int(input("Masukkan pilihan: "))
        except:
            print("Input tidak sesuai, mohon input sesuai perintah\n")
            continue
        else:
            break
    
    if choice == (1 or 2 or 3 or 4):
        print("Berikut daftar belanja yang ada saat ini: \n")
        printDaftarBelanja(currentdaftarBelanja)
    
    if choice == 1:
        dataTidakDitemukan = True
        while dataTidakDitemukan:
            namaBarang = input("Masukkan nama barang yang akan diubah: ")
            if namaBarang.lower() in currentdaftarBelanja.keys():
                dataTidakDitemukan = False
                print("Nama barang ditemukan")
            else:
                print("Input tidak sesuai, masukkan nama barang sesuai daftar belanja\n")
        else:
            while True:
                try :
                    jumlahBarang = int(input("Masukkan jumlah barang yang baru: "))
                except:
                    print("Input tidak sesuai, mohon input sesuai perintah\n")
                    continue
                else:
                    break
            ubahInformasiBarang_jumlah_harga(currentdaftarBelanja, namaBarang, 0, jumlahBarang)
                 
    elif choice == 2:        
        dataTidakDitemukan = True
        while dataTidakDitemukan:
            namaBarang = input("Masukkan nama barang yang akan diubah: ")
            if namaBarang.lower() in currentdaftarBelanja.keys():
                dataTidakDitemukan = False
                print("Nama barang ditemukan")
            else:
                print("Input tidak sesuai, masukkan nama barang sesuai daftar belanja\n")
        else:
            while True:
                try :
                    hargaBarang = int(input("Masukkan harga barang yang baru: "))
                except:
                    print("Input tidak sesuai, mohon input sesuai perintah\n")
                    continue
                else:
                    break
            ubahInformasiBarang_jumlah_harga(currentdaftarBelanja, namaBarang, 1, hargaBarang)
                 
    elif choice == 3:
        dataTidakDitemukan = True
        while dataTidakDitemukan:
            namaBarang_lama = input("Masukkan nama barang yang akan diubah: ")
            if namaBarang_lama.lower() in currentdaftarBelanja.keys():
                dataTidakDitemukan = False
                print("Nama barang ditemukan")
            else:
                print("Input tidak sesuai, masukkan nama barang sesuai daftar belanja\n")
        else:
            dataDitemukan = True
            while dataDitemukan:
                namaBarang_baru = input("Masukkan nama barang yang baru: ")
                if not(namaBarang_baru.lower() in currentdaftarBelanja.keys()):
                    dataDitemukan = False
                    break
                else:
                    print("Nama barang sudah dimasukkan ke daftar belanja sebelumnya.")
            ubahInformasiBarang_nama(currentdaftarBelanja, namaBarang_lama, namaBarang_baru)
            
    elif choice == 4:
        dataTidakDitemukan = True
        while dataTidakDitemukan:
            namaBarang = input("Masukkan nama barang yang akan dihapus: ")
            if namaBarang.lower() in currentdaftarBelanja.keys():
                dataTidakDitemukan = False
                print("Nama barang ditemukan")
            else:
                print("Input tidak sesuai, masukkan nama barang sesuai daftar belanja\n")
        else:
            hapusBarangTertentu(currentdaftarBelanja, namaBarang)
    
    elif choice == 5:
        hapusBarangKeseluruhan(currentdaftarBelanja)
        
    elif choice == 6:
        menu()
   
    print("=============================================================================\n\n")

def totalBelanja(dict):
    """Fungsi untuk menghitung total biaya belanja customer.
    """
    print("========================= TOTAL BELANJA ===============================")
    totalBiayaBelanja = 0
    for i in dict:
        totalHargaPerItem = dict[i][0] * dict[i][1]
        totalBiayaBelanja = totalBiayaBelanja + int(totalHargaPerItem)
    
    if totalBiayaBelanja > 200000 and totalBiayaBelanja <= 300000:
        totalBiayaBelanja = totalBiayaBelanja + (totalBiayaBelanja*0.05)
        print(f"Selamat, anda mendapat diskon sebesar 5%. Total biaya belanja anda adalah Rp {totalBiayaBelanja:,.2f}\n")
    elif totalBiayaBelanja > 300000 and totalBiayaBelanja <= 500000:
        totalBiayaBelanja = totalBiayaBelanja + (totalBiayaBelanja*0.08)
        print(f"Selamat, anda mendapat diskon sebesar 8%. Total biaya belanja anda adalah Rp {totalBiayaBelanja:,.2f}\n")
    elif totalBiayaBelanja > 500000:
        totalBiayaBelanja = totalBiayaBelanja + (totalBiayaBelanja*0.10)
        print(f"Selamat, anda mendapat diskon sebesar 10%. Total biaya belanja anda adalah Rp {totalBiayaBelanja:,.2f}\n")
    else:
        print(f"Total biaya belanja anda adalah Rp {totalBiayaBelanja:,.2f}\n")

def tampilanMenu(nama):
    """Fungsi untuk menampilkan menu."""
    
    print("Hi %s, selamat berbelanja. Silahkan pilih menu : \n" %(nama))
    print("1. Masukkan daftar belanja")
    print("2. Update daftar belanja")
    print("3. Tampilkan daftar belanja")
    print("4. Total belanja")
    print("5. Exit")

def menu(): 
""" Daftar menu dari sistem Super Cashier."""
    choice = 0
    currentdaftarBelanja = {}

    print("-"*60)
    print("SELAMAT DATANG DI TOKO PACMANN SEJAHTERA")
    print("-"*60)
    nama = input("Silahkan masukkan nama: ")
        
    while choice != 5:
        tampilanMenu(nama)

        while True:
                try :
                    choice = int(input("Masukkan pilihan menu: "))
                except:
                    print("Input tidak sesuai, mohon input sesuai perintah\n")
                    continue
                else:
                    break
        
        if choice == 1:    
            currentdaftarBelanja = masukkanDaftarBelanja(currentdaftarBelanja)
        elif choice == 2:
            ubahDaftarBelanja(currentdaftarBelanja)
        elif choice == 3:
            printDaftarBelanja(currentdaftarBelanja)
        elif choice == 4:
            totalBelanja(currentdaftarBelanja)
        else:
            "Silahkan pilih sesuai daftar menu yang tersedia."
    else:
        print(f"Terima kasih sudah berbelanja di toko kami, {nama}. Sampai jumpa lagi")

#Code untuk menjalankan sistem Super Cashier
main()