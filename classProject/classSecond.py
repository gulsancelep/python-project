class Insan(object):
    def __init__(self):
        self.ad = 'Gülşan'
        self.soyad = 'Celep'
        self.yas = 26
        self.ulke = 'Türkiye'
        self.sehir = 'Bolu'
        self.yetenekler = []

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)
    def kisi_bilgileri(self):
        return print('Adı: ' + self.ad, 'Soyadı: ' + self.soyad, 'Yaşı: ' + str(self.yas), 'Ülke: ' + self.ulke,
                     'Şehir: ' + self.sehir, 'Yetenekler: ' + self.yetenekler[0])

insan = Insan()
insan.yetenek_ekle('Bisiklete binmek, Python')
insan.kisi_bilgileri()