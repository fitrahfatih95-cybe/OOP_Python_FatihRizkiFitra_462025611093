class Mobil:
    name = ""
    merek = ""
    
    @staticmethod
    def kabin():
        print(f"mobil ini memiliki kabin yang luas")
    def mesin(self):
        print(f"mesin {self.name} menggunakan mesin dari {self.merek}")
    def dari (self, asal):
        print(f"mobil {self.merek} merupakan buatan dari {asal}")
    
mobil1 = Mobil()
mobil1.name = "Inova"
mobil1.merek = "Toyota"

mobil1.kabin()
mobil1.mesin()
mobil1.dari('jepang')