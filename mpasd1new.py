from prettytable import PrettyTable

class Kendaraan:
    def __init__(self, id, merk, model, tahun, harga):
        self.id = id
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.harga = harga

class Dealer:
    def __init__(self):
        self.kendaraan_dict = {}

    def tambah_kendaraan(self, kendaraan):
        self.kendaraan_dict[kendaraan.id] = kendaraan

    def hapus_kendaraan(self, id):
        if id in self.kendaraan_dict:
            del self.kendaraan_dict[id]
            print("Kendaraan dengan ID {} telah dihapus.".format(id))
        else:
            print("Kendaraan dengan ID {} tidak ditemukan.".format(id))

    def tampilkan_katalog(self):
        if self.kendaraan_dict:
            table = PrettyTable(["ID", "Merk", "Model", "Tahun", "Harga"])
            for id, kendaraan in self.kendaraan_dict.items():
                table.add_row([id, kendaraan.merk, kendaraan.model, kendaraan.tahun, kendaraan.harga])
            print(table)
        else:
            print("Katalog kendaraan kosong.")

    def cari_kendaraan(self, id):
        if id in self.kendaraan_dict:
            kendaraan = self.kendaraan_dict[id]
            print("Kendaraan ditemukan:")
            print("ID: {}, Merk: {}, Model: {}, Tahun: {}, Harga: {}".format(
                id, kendaraan.merk, kendaraan.model, kendaraan.tahun, kendaraan.harga))
        else:
            print("Kendaraan dengan ID {} tidak ditemukan.".format(id))

    def update_kendaraan(self, id, kendaraan_baru):
        if id in self.kendaraan_dict:
            self.kendaraan_dict[id] = kendaraan_baru
            print("Kendaraan dengan ID {} telah diperbarui.".format(id))
        else:
            print("Kendaraan dengan ID {} tidak ditemukan.".format(id))

    def create_kendaraan(self, id, merk, model, tahun, harga):
        kendaraan_baru = Kendaraan(id, merk, model, tahun, harga)
        self.tambah_kendaraan(kendaraan_baru)
        print("Kendaraan baru telah ditambahkan.")

    def read_katalog(self):
        self.tampilkan_katalog() 

    def update_kendaraan_by_id(self, id, merk, model, tahun, harga):
        kendaraan_baru = Kendaraan(id, merk, model, tahun, harga)
        self.update_kendaraan(id, kendaraan_baru)

    def delete_kendaraan(self, id):
        self.hapus_kendaraan(id)

if __name__ == "__main__":
    dealer = Dealer()

    while True:
        print("\n=== MENU ===")
        print("1. Tampilkan Katalog")
        print("2. Tambah Kendaraan")
        print("3. Cari Kendaraan")
        print("4. Hapus Kendaraan")
        print("5. Update Kendaraan")
        print("6. Keluar")

        choice = input("Pilih operasi yang ingin Anda lakukan: ")

        if choice == "1":
            dealer.read_katalog()
        elif choice == "2":
            id = input("Masukkan ID kendaraan: ")
            merk = input("Masukkan merk kendaraan: ")
            model = input("Masukkan model kendaraan: ")
            tahun = int(input("Masukkan tahun kendaraan: "))
            harga = int(input("Masukkan harga kendaraan: "))
            dealer.create_kendaraan(id, merk, model, tahun, harga)
        elif choice == "3":
            id = input("Masukkan ID kendaraan yang ingin dicari: ")
            dealer.cari_kendaraan(id)
        elif choice == "4":
            id = input("Masukkan ID kendaraan yang ingin dihapus: ")
            dealer.delete_kendaraan(id)
        elif choice == "5":
            id = input("Masukkan ID kendaraan yang ingin diperbarui: ")
            merk = input("Masukkan merk kendaraan baru: ")
            model = input("Masukkan model kendaraan baru: ")
            tahun = int(input("Masukkan tahun kendaraan baru: "))
            harga = int(input("Masukkan harga kendaraan baru: "))
            dealer.update_kendaraan_by_id(id, merk, model, tahun, harga)
        elif choice == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")
