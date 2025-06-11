total=0
def count():
    total+=1
    return total
print(count())


# error, because total is not local variable..