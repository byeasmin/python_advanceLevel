# Rules : params, *args, default parameters, **kwargs


def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total+=items
    return sum(args) + total
print(super_func('benin',1,2,3,4,5, num1=3, num2=7))








'''
Output : 
25
'''