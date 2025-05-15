# dictionary..

users = {
    'name':"benin",
    'age':23,
    'can_swim':False

}

for item in users:
    print(item)




# dictionary method..
for item in users.items():
    print(item)
for item in users.values():
    print(item)
for item in users.keys():
    print(item)




for keys,values in users.items():
    print(keys,values)












'''
output :
name
age
can_swim
('name', 'benin')
('age', 23)
('can_swim', False)
benin
23
False
name
age
can_swim
name benin
age 23
can_swim False
'''