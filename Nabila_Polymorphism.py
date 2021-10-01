class serang:
    def intro(self):
        print("Serang adalah Ibu Kota Provinsi Banten")

    def kecamatan(self):
        print("Kota Serang memiliki 6 kecamatan")

class Serang(serang):
    def kecamatan(self):
        print("Kecamatan Serang terdiri dari 10 kelurahan.")

class Kasemen(serang):
    def kecamatan(self):
        print("Kecamatan Kasemen terdiri dari 10 kelurahan.")

class CipocokJaya(serang):
    def kecamatan(self):
        print("Kecamatan Cipocok Jaya terdiri dari 8 kelurahan")

class Curug(serang):
    def kecamatan(self):
        print("Kecamatan Curug terdiri dari 10 kelurahan")

class Taktakan(serang):
    def kecamatan(self):
        print("Kecamatan Taktakan terdiri dari 13 kelurahan")

class Walantaka(serang):
    def kecamatan(self):
        print("Kecamatan Walantaka terdiri dari 14 kelurahan")

obj_Serang = Serang ()
obj_serang = serang ()
obj_Kasemen = Kasemen()
obj_CipocokJaya = CipocokJaya()
obj_Curug = Curug ()
obj_Taktakan =  Taktakan ()
obj_Walantaka = Walantaka()

obj_serang.intro()
obj_serang.kecamatan()

print("\n")

obj_Kasemen.intro()
obj_Kasemen.kecamatan()

print("\n")

obj_CipocokJaya.intro()
obj_CipocokJaya.kecamatan()

print("\n")

obj_Curug.intro()
obj_Curug.kecamatan()

print("\n")

obj_Taktakan.intro()
obj_Taktakan.kecamatan()

print("\n")

obj_Walantaka.intro()
obj_Walantaka.kecamatan()