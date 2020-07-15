# 1- Girilen 2 sayıdan hangisi büyüktür ?
a=int(input("1.sayi"))
b=int(input("2.sayi"))
sonuc=(a>b)
print(f'a: {a} b: {b} den büyüktür: {sonuc}')
#2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
vize1=float(input("1.vize:"))
vize2=float(input("2.vize:"))
final=float(input("Final:"))
ortalama=((vize1+vize2)/2)*0.6+(final*0.4)
print(ortalama)
# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
sayi=int(input("Sayı:"))
tekcift=(sayi%2==0)
print(f'girilen sayı çift olma durumu: {tekcift}')