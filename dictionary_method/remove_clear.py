users ={
    'basket':[1,2,3,4],
    'greet':'hellow',
    'age': 20
}



# print(users.clear())
# users.clear()
print(users)

user1=users.copy()
print(users)
print(user1)

print(users.pop('age'))
print(users)


print(users.popitem())
print(users)


print(users.update({'basket':[1,2,3,4,5]}))
print(users)










'''
output : 
{'basket': [1, 2, 3, 4], 'greet': 'hellow', 'age': 20}
{'basket': [1, 2, 3, 4], 'greet': 'hellow', 'age': 20}
{'basket': [1, 2, 3, 4], 'greet': 'hellow', 'age': 20}
20
{'basket': [1, 2, 3, 4], 'greet': 'hellow'}
('greet', 'hellow')
{'basket': [1, 2, 3, 4]}

'''