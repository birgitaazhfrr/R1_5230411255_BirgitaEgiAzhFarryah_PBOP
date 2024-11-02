class Pegawai:
    def __init__(self, NIK, nama, alamat):
        self.NIK = NIK
        self.nama = nama
        self.alamat = alamat

class Produk:
    def __init__(self, kode, nama, jenis, harga, stok=0):
        self.kode = kode
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.stok = stok
    
    def info(self):
        return f"{self.kode}: {self.nama} ({self.jenis}) - Harga: Rp{self.harga}, Stok: {self.stok}"

class Snack(Produk):
    def __init__(self, kode, nama, harga, stok=0):
        super().__init__(kode, nama, "Snack", harga, stok)

class Makanan(Produk):
    def __init__(self, kode, nama, harga, stok=0):
        super().__init__(kode, nama, "Makanan", harga, stok)

class Minuman(Produk):
    def __init__(self, kode, nama, harga, stok=0):
        super().__init__(kode, nama, "Minuman", harga, stok)

class Transaksi:
    def __init__(self, no_transaksi, tanggal, pegawai):
        self.no_transaksi = no_transaksi
        self.tanggal = tanggal
        self.pegawai = pegawai
        self.detail = []

    def tambah_item(self, produk, jumlah):
        if produk.stok >= jumlah:
            produk.stok -= jumlah
            self.detail.append({"produk": produk, "jumlah": jumlah})
        else:
            print("Stok tidak cukup.")

    def total_harga(self):
        total = sum(item["produk"].harga * item["jumlah"] for item in self.detail)
        return total

class Penjualan:
    def __init__(self):
        self.transaksi_list = []

    def tambah_transaksi(self, transaksi):
        self.transaksi_list.append(transaksi)

    def tampilkan_transaksi(self):
        if not self.transaksi_list:
            print("Belum ada transaksi.")
            return
        
        print("===== Daftar Transaksi =====")
        for transaksi in self.transaksi_list:
            print(f"No. Transaksi: {transaksi.no_transaksi}, Tanggal: {transaksi.tanggal}, Pegawai: {transaksi.pegawai.nama}")
            for item in transaksi.detail:
                print(f"  {item['jumlah']} x {item['produk'].nama} = Rp{item['produk'].harga * item['jumlah']}")
            print(f"Total: Rp{transaksi.total_harga()}")
            print("---------------------------")

class Struk:
    def __init__(self, transaksi):
        self.transaksi = transaksi

    def cetak_struk(self):
        print("=============================")
        print("       Struk Pembelian       ")
        print("=============================")
        print(f"No. Transaksi: {self.transaksi.no_transaksi}")
        print(f"Tanggal: {self.transaksi.tanggal}")
        print(f"Nama Pegawai: {self.transaksi.pegawai.nama}")
        print("-----------------------------")
        for item in self.transaksi.detail:
            print(f"{item['jumlah']} x {item['produk'].nama} = Rp{item['produk'].harga * item['jumlah']}")
        print("-----------------------------")
        print(f"Total: Rp{self.transaksi.total_harga()}")
        print("=============================")

class Menu:
    def __init__(self):
        self.produk_list = self.inisialisasi_produk()

    def inisialisasi_produk(self):
        return [
            Snack("B01", "Danish Strawberry", 24000, 12),
            Snack("B02", "Cream Brulle", 25000, 21),
            Makanan("M01", "Nasi Goreng", 25000, 25),
            Makanan("M02", "Ayam Lengkuas", 31000, 25),
            Makanan("M03", "Ayam Bakar", 25000, 8),
            Minuman("G01", "Palma Coffee", 24000, 30),
            Minuman("G02", "Himalaya Coffee", 25000, 25),
            Minuman("G03", "Cookie Monster", 20000, 16),
            Minuman("G04", "Matcha Latte", 22000, 17),
            Minuman("G05", "Ice Tea", 12000, 21)
        ]

    def tampilkan_menu(self):
        if not self.produk_list:
            print("Menu kosong.")
        else:
            for produk in self.produk_list:
                print(produk.info())

    def hapus_menu(self, kode_produk):
        produk_ditemukan = next((p for p in self.produk_list if p.kode == kode_produk), None)
        if produk_ditemukan:
            self.produk_list.remove(produk_ditemukan)
            print(f"Produk dengan kode {kode_produk} telah dihapus.")
        else:
            print(f"Produk dengan kode {kode_produk} tidak ditemukan.")

if __name__ == "__main__":

    pegawai1 = Pegawai("1221", "Birgita", "Jl. Sakura")
    pegawai2 = Pegawai("2112", "Milanueva", "Jl. Bangkai")
    menu_app = Menu()
    penjualan_app = Penjualan()

    while True:
        print("============ Jiro's Market ============")
        print("\nMenu Utama:")
        print("1. Daftar Menu :")
        print("2. Hapus Menu :")
        print("3. Daftar Stok :")
        print("4. Input Penjualan :")
        print("5. Daftar Penjualan :")
        print("6. Cetak Struk :")
        print("7. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            menu_app.tampilkan_menu()
        elif pilihan == '2':
            kode_produk = input("Masukkan kode produk yang ingin dihapus: ")
            menu_app.hapus_menu(kode_produk)
        elif pilihan == '3':
            menu_app.tampilkan_menu()
        elif pilihan == '4':
            no_transaksi = input("Masukkan nomor transaksi: ")
            tanggal = input("Masukkan tanggal transaksi: ")
            transaksi = Transaksi(no_transaksi, tanggal, pegawai1)

            while True:
                kode_produk = input("Masukkan kode produk: ")
                if kode_produk.lower() == 'selesai':
                    break
                
                produk_ditemukan = next((p for p in menu_app.produk_list if p.kode == kode_produk), None)
                
                if not produk_ditemukan:
                    print("Produk tidak ditemukan.")
                    continue
                
                jumlah = int(input("Masukkan jumlah: "))
                transaksi.tambah_item(produk_ditemukan, jumlah)

            penjualan_app.tambah_transaksi(transaksi)
            print("Transaksi berhasil disimpan.")
        elif pilihan == '5':
            penjualan_app.tampilkan_transaksi()
        elif pilihan == '6':
            no_transaksi = input("Masukkan nomor transaksi yang ingin dicetak: ")
            transaksi_ditemukan = next((t for t in penjualan_app.transaksi_list if t.no_transaksi == no_transaksi), None)

            if transaksi_ditemukan:
                struk = Struk(transaksi_ditemukan)
                struk.cetak_struk()
            else:
                print("Transaksi tidak ditemukan.")
        elif pilihan == '7':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
