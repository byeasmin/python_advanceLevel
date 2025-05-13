#dictionary is a unorders key-value pair..

dictionary={
    'a':1,
    'b':2
}
print(dictionary['a'])



my_dictionary={
    'a':'benin',
    'b':[1,2,3,4,5],
    'c':True
}

print(my_dictionary['b'])
print(my_dictionary['b'][1]) # the value of 1 no index is 2.



my_list = [{'a':[1,2,3], 'b':'hellow', 'c': True}, {'a':[4,5,6], 'b':'hello', 'c': True}]

print(my_list[0])
print(my_list[1])

print(my_list[0]['a'][2])



'''
output : 
1
[1, 2, 3, 4, 5]
2
{'a': [1, 2, 3], 'b': 'hellow', 'c': True}
{'a': [4, 5, 6], 'b': 'hello', 'c': True}
3

'''













