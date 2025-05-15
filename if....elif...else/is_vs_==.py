# equality operator..

print(True==1)
print(''==1)
print(10==10.0)
print([]==1)
print([]==[])


#print('now let\'s check whether is and == are same or not')

print("now let's check whether is and == are same or not")



# is(identity operator)
print(True is 1)
print('' is 1)
print(10 is 10.0)
print([] is 1)
print([] is [])

# everything will be false..




# ex - 1:

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True, because their contents are the same


# ex - 2:
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, because a and b are two different objects in memory



# ex - 3:

x = 5
y = 5

print(x == y)  # True, values are the same
print(x is y)  # True, because small integers (-5 to 256) are cached by Python



# ex - 4:
x = [1, 2]
y = [1, 2]

print(x == y)  # True, values are equal
print(x is y)  # False, different objects in memory



print(10 is 10) # True because Python caches small integers.










'''
output : 
True
False
True
False
True
now let's check whether is and == are same or not
False
False
False
False
False
True
False
True
True
True
False
True

'''


























































