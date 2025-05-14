is_friend = True
is_user = False

if is_friend or is_user:
    print("best friend forever")
print("condition false")



if is_friend and is_user:
    print("best friend forever") #not print cz we have a false, this is called short circuiting..
print("condition false")







'''
output :
best friend forever
condition false
condition false
'''