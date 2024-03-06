tam_bolunenler = []
def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    for temp in range(min_sayi, max_sayi + 1):
        if(temp % bolen_sayi == 0):
            tam_bolunenler.append(temp)

    return tam_bolunenler

print(bolunen_sayi_bulma(1,6,2))