'''
Clean code is code that is:

Easy to read

Easy to understand

Easy to maintain

Free of unnecessary complexity
'''



def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False
print(is_even(51))
# this code is right but not a clean code...


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
print(is_even(52))




def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(57))




# this is a clean code..
def is_even(num):
    return num % 2 == 0
print(is_even(60))
print(is_even(61))








'''
Output : 
False
True
False
True
False
'''

