meyveler={'elma','karpuz','kiraz'} #set küme tanımlaması
# print(meyveler[0]) indekslenemez.

for meyve in meyveler:
    print(meyve)

meyveler.add('Vişne') #sonuna vişne ekliyor
meyveler.update(['mango','üzüm','kavun']) #meyveler set kümesini düzenliyor
meyveler.remove('mango') #set kümesinden mango çıkarılıyor
meyveler.discard('elma') #remove ile aynı kullanım
meyveler.pop() #sondaki eleman siliniyor
meyveler.clear() #set kümesinin içi temizleniyor
print(meyveler)