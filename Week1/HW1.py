# -*- coding: utf-8 -*-
while True:
    islem = (input("\nİşlem Seçiniz (+, -, *, / veya Çıkmak için 'exit' yazabilirsiniz):"))
    if islem == "+" or islem == "-" or islem == "*" or islem == "/" or islem == "exit":
        if islem == "exit":
            print("Çıkış Yapılıyor.")
            break
        while True:
            try:
                sayi1 = int(input("\nİlk Sayıyı Giriniz: "))
                sayi2 = int(input("İkinci Sayıyı Giriniz: "))
                break                
            except:
                print("\nGirdiğiniz değer sayı değil.")
                continue
               
        if islem == "+":
            print("Sonuç: {}".format(sayi1+sayi2))

        elif islem == "-":
            print("Sonuç: {}".format(sayi1-sayi2))

        elif islem == "*":
            print("Sonuç: {}".format(sayi1*sayi2))

        elif islem == "/":
            if sayi1 == 0 or sayi2 == 0:
                print("Bölen '0' olamaz.")
            else:
                print("Sonuç: {}".format(sayi1/sayi2))
    else:
        print("\nGirdiğiniz değer geçersiz.")