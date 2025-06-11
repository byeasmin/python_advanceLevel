# A nonlocal variable is used inside a nested function,
# and it refers to a variable in the enclosing (outer) function, not the global scope.

def outer():
    x = "local"
    def inner():
        nonlocal x  # refers to x from outer()
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)

outer()



'''
Output : 

inner: nonlocal
outer: nonlocal
'''






