numbers=[1,14,17,34,35,68]
kelimeler=['r','a','b','i','a']
val=min(numbers)
print(val)
val=max(numbers)
print(val)

numbers[4]=40
numbers.append(48)
numbers.append(71)
numbers.insert(0,15)
print(numbers)

siralama=numbers.sort()
print(siralama)