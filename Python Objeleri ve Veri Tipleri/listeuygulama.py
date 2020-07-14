# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=['BMW','Mercedes','Opel','Mazda']
# 2-  Liste Kaç elemanlıdır ?
sonuc=len(arabalar)
print(sonuc)
# 3-  Listenin ilk ve son elemanı nedir ?
sonuc=arabalar[0]
print(sonuc)
sonuncu=arabalar[3]
print(sonuncu)
# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1]='Toyota'
print(arabalar)
# 5-  Mercedes listenin bir elemanı mıdır ?
sonuc='Mercedes' in arabalar
print(sonuc)
# 6-  Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])
# 7-  Listenin ilk 3 elemanını alın.
sonuc=arabalar[0:3]
print(sonuc)
# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
sonuc=arabalar+['Audi','Nissan']
print(sonuc)
# 10- Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)
# 11- Liste elemanlarını tersten yazdırınız.
sonuc = arabalar[::-1]
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]
