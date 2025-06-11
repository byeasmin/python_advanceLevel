# A local variable is one that is defined inside
# a function and can only be used inside that function.

def my_function():
    x = 10     # local variable
    print(x)
my_function()
print(x)       # ❌ Error: x is not defined outside



'''
Output :
10
'''
# x is defined inside my_function(), so it only exists there.





