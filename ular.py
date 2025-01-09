from animal import Animal

class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_kulit, Family):
        super().__init__(nama, makanan, hidup, berkembang_biak,)
        self.warna_kulit = warna_kulit
        self.ordo = Family
        
        
    def info_ular(self):
        super().info_animal(),
        print("sirip \t\t\t : ", self.warna_kulit,
              "\nordo \t\t : ", self.Family)
        
Ular_python = ular("Python","Daging","tanah","Bertelur","coklat","Pythonidae")
Ular_python.info_ular()
print("=================================================")
ular_kobra = ular("kobra","daging","tanah","bertelur","hitam","elapidae")
ular_kobra.info_ular()
print("=================================================")
