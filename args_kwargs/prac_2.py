def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args) + sum(kwargs.values())
print(super_func(1,2,3,4,5, num1=3, num2=7)) # dictionary






'''
Output : 
(1, 2, 3, 4, 5)
{'num1': 3, 'num2': 7}
25
'''