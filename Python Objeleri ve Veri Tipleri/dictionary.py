#key- value
# plakalar = { 'pendik' : 34, 'çanakkale': 17 }
#key = pendik value= 34 key= çanakkale value= 17
users = {
    'omertahaoztop': {
        'age': 22,        
        'roles': ['kullanici'],
        'email': 'omertahaoztop@gmail.com',
        'address': 'pendik',
        'phone': '1231321'
    },
    'enessafa': {
        'age': 2,
        'roles': ['admin','user'],
        'email': 'enessafa@gmail.com',
        'address': 'pendik',
        'phone': '1231321'
    }
}

print(users['enessafa']['roles'][0])
