vize1 = float(input("1. vize notunu giriniz: "))
vize2 = float(input("2. vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))

if 0 <= vize1 <= 100 and 0 <= vize2 <= 100 and 0 <= final <= 100:
    ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

    if ortalama >= 90:
        harf = 'AA'
    elif ortalama >= 85:
        harf = 'BA'
    elif ortalama >= 80:
        harf = 'BB'
    elif ortalama >= 75:
        harf = 'CB'
    elif ortalama >= 70:
        harf = 'CC'
    elif ortalama >= 65:
        harf = 'DC'
    elif ortalama >= 60:
        harf = 'DD'
    elif ortalama >= 55:
        harf = 'FD'
    else:
        harf = 'FF'

    print("Ortalamanız: ", ortalama)
    print("Harf notunuz: ", harf)
else:
    print("Geçerli bir sınav notu giriniz.")