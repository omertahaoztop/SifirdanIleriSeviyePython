x=5
hak=0
devam='E'
sonuc=5<x<10
# and
# True, True => True
# True, False => False
sonuc = (x > 5) and (x < 10)  
sonuc = (hak > 0) and (devam == 'e')
# or

sonuc = (x > 0) or (x % 2 == 0)

# True, False => True
# True, True => True
# False, False => False

# not

sonuc = not(x > 0)

# x, 5-10 arasında olan bir çift sayı mı?

sonuc = ((x>5) and (x<10)) and (x%2==0)

print(sonuc)