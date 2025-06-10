# *args and **kwargs..

# *args
def super_func(*args):
    print(args)
    return sum(args)
print(super_func(1,2,3,4,5)) # tuple


# **kwargs

def super_func(*args, **kwargs):
    print(kwargs)
    return sum(args)
print(super_func(1,2,3,4,5, num1=3, num2=7)) # dictionary





'''
Output : 
(1, 2, 3, 4, 5)
15
{'num1': 3, 'num2': 7}
15
'''

