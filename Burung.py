from animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, paruh, warna_bulu):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.paruh = paruh
        self.warna_bulu = warna_bulu
        
        
    def info_burung(self):
        super().info_animal(),
        print("paruh \t\t\t : ", self.paruh,
              "\nwarna bulu \t\t : ", self.warna_bulu)
        
Burung_beo = Burung("beo","jagung","darat","bertelur","melengkung","warna warni")
Burung_beo.info_burung()
print("=================================================")
Burung_merpati = Burung("merpati","beras","darat","bertelur","lurus","putih")
Burung_merpati.info_burung()
print("=================================================")
