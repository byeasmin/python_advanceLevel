# 2. Enclosing Scope (E)

def outer():
    x = 'enclosing'
    def inner():
        print(x)  # Looks for x in the enclosing function
    inner()

outer()
