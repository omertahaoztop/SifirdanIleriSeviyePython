website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
result='Hello World'.strip()
result='Hello World'.lstrip()
result='Hello World'.rstrip()


# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
result='www.sadikturan.com'.strip('w.moc')
# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
result=course.lower()
result=course.upper()
result=course.title()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result=website.count('a')
result=website.count('www')

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result=website.startswith('www')
result=website.endswith('com')
# 6-  'website' içinde '.com' ifadesi var mı?
result=website.find('com')

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

result=course.isalpha()
result=course.isdigit()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result='Contents'.center(100,'*')
result='Contents'.ljust(100,'*')
result='Contents'.rjust(100,'*')
# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result=course.replace('','-')
# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result='Hello World'.replace('World','There')
# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
result=course.split(' ')

print(result)