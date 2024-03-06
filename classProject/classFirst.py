class Ogrenci(object):
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif

class Soru(Ogrenci):
    def net_sayisi(self, dogru, yanlis):
        self.net = dogru - (yanlis / 4)

        self.hesapla(self.net)
    def hesapla(self, ogrenci_net):
        return print('Öğrenci Adı: ' + self.ogrenci_adi, 'Soyadı: ' + self.ogrenci_soyadi,
                     'Sınıfı: ' + self.ogrenci_sinif, 'Puanı: ' + str(ogrenci_net * 2))

soru = Soru('Gülşan', 'Celep', '12-C')
soru.net_sayisi(46,4)