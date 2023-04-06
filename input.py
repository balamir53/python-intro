# print('DUKKANIMA HOSGELDINIZ!')
# print('*'*30)

# item = input('Satin aldiginiz urun nedir: ')
# price = float(input(f"{item}(n)in fiyati nedir: "))
# quantity = float(input(f"Kac tane {item} aldiniz: "))

# print(f"Sepete {quantity} tane {item} eklendi")
# print(f"Toplam: $ {round((quantity*price),2)}")
# input()

# tweet = input('Tweetinizi giriniz: ')
# uzunluk = len(tweet)

# if uzunluk < 140:
#     print(f'{uzunluk} karakterli tweet atabilirsiniz.')
# else:
#     print(f'{uzunluk-140} karakter fazla girdiniz!')

# from random import randint

# zar_sayisi = int(input('Kac zar atilacak: '))
# while zar_sayisi<1 or zar_sayisi>20:
#     zar_sayisi = int(input('Lutfen 1 ile 20 arasinda bir sayi girin: '))
# kenar_sayisi = int(input('Kac kenarli olacaklar: '))
# while kenar_sayisi<1 or kenar_sayisi>20:
#     kenar_sayisi = int(input('Lutfen 1 ile 20 arasinda bir sayi girin: '))

# while True:
#     sonuc = '|'
#     for zar in range(zar_sayisi):
#         rand = randint(1, kenar_sayisi)
#         sonuc+=f'{rand}|'
#     print(sonuc)
#     cevap = input('Tekrar zar atilsin mi? (Cikmak icin "q"ya basin)')
#     if cevap == 'q':
#         break

print('Kurdan oyununa hosgeldiniz!')
print('*'*30)

kalan_kurdan = 13
birinci_oyuncu = input('Birinci oyuncunun adi: ')
ikinci_oyuncu = input('Ikinci oyuncunun adi: ')

while True:
    print('| '*kalan_kurdan)
    print(f'Toplam {kalan_kurdan} kurdan kaldi')
    # birinci oyuncunun secimi
    p1_secim = int(input(f'{birinci_oyuncu}, kac kurdan seciyorsun?: '))
    while p1_secim < 1 or p1_secim > 3:
        p1_secim = int(input(f'Sadece 1,2 veya 3 kurdan secebilirsin: '))
    # kurdan azalt
    kalan_kurdan -= p1_secim
    if kalan_kurdan <=0:
        print(f'{birinci_oyuncu} kazandi')
        break

    print('| '*kalan_kurdan)
    print(f'Toplam {kalan_kurdan} kurdan kaldi')
    # inci oyuncunun secimi
    p2_secim = int(input(f'{ikinci_oyuncu}, kac kurdan seciyorsun?: '))
    while p2_secim < 1 or p2_secim > 3:
        p2_secim = int(input(f'Sadece 1,2 veya 3 kurdan secebilirsin: '))
    # kurdan azalt
    kalan_kurdan -= p2_secim
    if kalan_kurdan <=0:
        print(f'{ikinci_oyuncu} kazandi')
        break
print('OYUN BITTI')
