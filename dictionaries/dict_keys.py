# a key cannot be changed

dictionary = {
    'a':'benin',
    'b':[1,2,3],
    'c':True
}


dictionary1={
    123:'benin',
    True:[1,2,3],
    'c':True,
    # [100]:True #error occurs, cz a key cannot be a list
}

print(dictionary1[True])
# print(dictionary1[100])






'''
output :
[1, 2, 3]
'''