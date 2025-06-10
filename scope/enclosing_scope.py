def outer():
    x = 'outer'

    def inner():
        nonlocal x
        x = 'changed'

    inner()
    print(x)  # 'changed'

outer()
