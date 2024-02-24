# miniproasd1

from  prettytable import PrettyTable
 
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


class Dealer:

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

    dealer.create_kendaraan("001", "Toyota", "Avanza", 2020, 150000000)
    dealer.create_kendaraan("002", "Honda", "Civic", 2019, 200000000)

  
    dealer.read_katalog()


    dealer.cari_kendaraan("001")

    dealer.delete_kendaraan("002")

  
    dealer.read_katalog()

   
    dealer.update_kendaraan_by_id("001", "Toyota", "Innova", 2021, 250000000)

    
    dealer.read_katalog()
