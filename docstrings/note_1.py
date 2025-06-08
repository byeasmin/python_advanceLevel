#Docstrings are special strings used to document code — especially functions, classes, and modules.

def greet(name):
    """
    This function takes a name as input
    and returns a greeting message.
    """
    return f"Hello, {name}!"
help(greet)





'''
Summary:
Use triple quotes (""" """ / ''' ''') right after defining a function or class.

It explains what the function/class/module does.
It’s different from regular comments (#) — docstrings are stored in memory and visible via tools like help().
'''






'''
Output : 
Help on function greet in module __main__:

greet(name)
    This function takes a name as input
    and returns a greeting message.
'''