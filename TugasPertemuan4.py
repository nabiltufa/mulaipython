#SuperClass Tempat Makan

class Tempatmakan():

    def __init__ (self, lokasi, menu, harga, rating):
        self.lokasi = lokasi
        self.menu = menu
        self.harga = harga
        self.rating = rating

    def printname (self):
        print("Lokasi: ", self.lokasi)
        print("Menu: ", self.menu)
        print("Harga: ", self.harga)
        print("Rating: ", self.rating)

#SubClass Tempat Makan Warteg dan Restoran

        class warteg(Tempatmakan):
            pass
        
        class restoran(Tempatmakan):
            pass

 #Output
        a = warteg("Sepang","Nasi Goreng","Rp10.000",3.9)
        a.printname

        b = restoran("Ujung Kulon", "Ramen Konoha", "Rp60.000",4)
        b.printname
