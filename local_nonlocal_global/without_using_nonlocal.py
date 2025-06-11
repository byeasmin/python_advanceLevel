def outer():
    x = "I am from outer"

    def inner():
        x = "Changed by inner"  # this creates a NEW local x
        print("Inside inner:",x)

    inner()
    print("Inside outer:",x)

outer()


# Without nonlocal,
# the x inside inner() is a new variable,
# separate from the one in outer() — so the outer value never changes.




'''
Output : 
Inside inner: Changed by inner
Inside outer: I am from outer

'''