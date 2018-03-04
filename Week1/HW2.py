while True:
	sayi1 = 1
	sayi2 = 1
	deger = (input("Fibonacci dizisinin kaçıncı değere kadar yazdırılacağını giriniz veya Çıkmak için 'exit' yazabilirsiniz: "))
	if deger == "exit":
		print("Çıkış yapılıyor.")
		break
	else:
		while True:
			try:
				deger = int(deger)
				if int(deger):
					i = 2
					while i<=deger+1:
						sayi1_eski = sayi1
						sayi2_eski = sayi2
						sayi1 = sayi2_eski
						sayi2 = sayi1_eski + sayi2_eski
						print (sayi2)
						i += 1
				break
			except:
				print("\nGirdiğiniz değer geçersiz.\n")
				break
	
