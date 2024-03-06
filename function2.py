def sayi_atama(sayi):
    iki_basamakli_sayi = 0

    if sayi < 10 or sayi > 99:
        print("2 basamaklı sayı giriniz.")
    elif sayi >= 10 and sayi <= 99:
        iki_basamakli_sayi = sayi

        return sayi_okunusu(iki_basamakli_sayi)

def sayi_okunusu(sayi):
    birler = ["Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
    onlar = ["On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

    birinci = sayi % 10
    ikinci = sayi // 10

    return onlar[ikinci - 1] + " " + birler[birinci - 1]

sayi = int(input("2 basamaklı sayı giriniz:"))

print(sayi_atama(sayi))