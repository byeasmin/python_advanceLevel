#Global Variables

# A global variable is defined outside all functions
# and is accessible inside functions
# (only for reading unless you use global keyword).


x = 5  # global variable
def print_x():
    print(x)  # accessing global variable
print_x()




'''
Output : 
5
'''





# Modifying Global Variable inside a Function


x = 5
def change_x():
    global x      # Declare x as global so we can modify it
    x = 10
change_x()
print(x)



'''
Output :
10
'''

# Without global, this would raise an error when trying to assign.

























