users ={
    'basket':[1,2,3,4],
    'greet':'hellow',
    'age': 20
}

print('basket' in 'users')
print('basket' in users)
print('size' in 'users')


# check kys and values..
print('basket' in users.keys())
print('hellow' in users.values())
print(users.items())  # it returns actually a tuple..





'''
output : 
False
True
False
True
True
dict_items([('basket', [1, 2, 3, 4]), ('greet', 'hellow'), ('age', 20)])

'''