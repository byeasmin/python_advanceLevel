# tuple is faster than list..


tuple=(1,2,3,4,5,6,7,8)

print(tuple[1])
print(5 in tuple)

users ={
    'basket':[1,2,3,4],
    'greet':'hellow',
    'age': 20
}

print(users.items())

# a key of a dictionary can be a tuple..

users1={
    (1,2):[34,35,36],
    'number':9
}
print(users1[(1,2)])





'''
output : 
2
True
dict_items([('basket', [1, 2, 3, 4]), ('greet', 'hellow'), ('age', 20)])
[34, 35, 36]

'''