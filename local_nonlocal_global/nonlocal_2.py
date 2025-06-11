def outer():
    x = "I am from outer"

    def inner():
        nonlocal x
        x = "Changed by inner"
        print("Inside inner:", x)

    inner()
    print("Inside outer:", x)

outer()




# 🧾 What Happens Step-by-Step:
# The function outer() is called.
# It creates a variable x = "I am from outer".
# Then inside outer(), we define another function inner().
# Inside inner():
# We say nonlocal x, meaning: "I want to use the x from outer(), not make a new one."
# We change x to "Changed by inner".
# It prints: "Inside inner: Changed by inner"
# After calling inner(), outer() prints: "Inside outer: Changed by inner"



'''
output : 
Inside inner: Changed by inner
Inside outer: Changed by inner

'''
