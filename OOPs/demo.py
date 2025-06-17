print(type(None))
print(type(True))
print(type(5))
print(type(5.5))
print(type('hi'))
print(type([]))
print(type(()))
print(type({}))



class BigObject:
    pass
    # code
obj1=BigObject() # instanciate
obj2=BigObject() # instanciate
obj3=BigObject() # instanciate

print(type(BigObject))
print(type(obj1))
print(type(obj2))
print(type(obj3))









'''
Output : 
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'dict'>
<class 'type'>
<class '__main__.BigObject'>
<class '__main__.BigObject'>
<class '__main__.BigObject'>
'''