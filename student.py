import names
import random
'''
ogrenci uygulamasi
ders olsun(matematik)
dersin sinavlari olsun
sinavlari uygulayalim
dersin ogrencileri olsun
ogrenci classi personel classini inherit etsin
dersin ogretmeni de personel classindan inherit etsin
ogrenci ilk okul orta okul ogrencisi olsun
'''
tum_ogrenciler = []
basarili_ogrenciler = {}
class Personel:
    def __init__(self, name, yas):
        self.name = name
        self.yas = yas
class Ogrenci(Personel):
    '''
    sinifi, ilk veya orta olarak girin
    '''
    def __init__(self,name,sinif,yas=8):
        if sinif != 'ilk':
            yas = 12
        super().__init__(name, yas)
        self.sinif = sinif
        self.matematik_sinav = None
        tum_ogrenciler.append(self)
    def __str__(self):
        return f'{self.name} {self.yas} yasinda bir ogrenci'

class Matematik:
    def __init__(self):
        self.name = 'Matematik'
        self.ogrenciler = []
    def kayit_yap(self, ogrenci):
        self.ogrenciler.append(ogrenci)
    def sinav_yap(self):
        if self.ogrenciler:
            for ogrenci in self.ogrenciler:
                sonuc = random.randint(1,100)
                ogrenci.matematik_sinav = sonuc 
        else:
            print('Bu sinifa ait kayitli ogrenci bulunmamaktadir.')
    

# **********kod baslangici***********
# ogrenci1 = Ogrenci(names.get_first_name(),'ilk',9)
# ogrenci2 = Ogrenci(names.get_first_name(),'orta')
matematik = Matematik()
for i in range(30):
    Ogrenci(names.get_first_name(),'ilk')    
for i in range(30):
    temp = Ogrenci(names.get_first_name(),'orta')
    matematik.kayit_yap(temp)
matematik.sinav_yap()
for ogrenci in tum_ogrenciler:
    if ogrenci.matematik_sinav and ogrenci.matematik_sinav>90:
        basarili_ogrenciler[ogrenci.name] = ogrenci.matematik_sinav
        print(ogrenci)
