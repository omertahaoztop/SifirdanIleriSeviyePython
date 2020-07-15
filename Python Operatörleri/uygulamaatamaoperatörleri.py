x,y,z=2,5,10
# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a=int(input('1.sayi : '))
b=int(input('2.sayi: '))
sonuc=(a*b)-(x+y+z)
# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
sonuc=y//x
# 3- (x,y,z) toplamının mod 3' ü nedir ?
toplam=x+y+z
sonuc=toplam%3
# 4- y' nin x. kuvvetini hesaplayınız.
sonuc=y**x
# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers=1,5,7,10,6
x,*y,z=numbers
sonuc=z**3
# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
numbers=1,5,10,6
x,*y,z=numbers
sonuc=y[0]+y[1]+y[2]
