from animal import Animal

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, sirip, Ordo):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.sirip = sirip
        self.ordo = Ordo
        
        
    def info_Ikan(self):
        super().info_animal(),
        print("sirip \t\t\t : ", self.sirip,
              "\nordo \t\t : ", self.Ordo)
        
Ikan_paus = Ikan("Paus","Rumput laut","Air","Beranak","sirip punggung","Artiodactyla")
Ikan_paus.info_Ikan()
print("=================================================")
Ikan_paus = Ikan("Paus","Rumput laut","Air","Beranak","sirip punggung","Artiodactyla")
Ikan_paus.info_Ikan()
print("=================================================")



