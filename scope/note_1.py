# In Python, scope refers to the region of a program where a variable is recognized and can be used.
# Scopes help prevent naming conflicts and control variable visibility.




# 1. Local Scope (L)
def my_func():
    x = 10  # Local variable
    print(x)

my_func()
# print(x)  # Error: x is not defined outside the function
