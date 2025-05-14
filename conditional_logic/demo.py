is_old=True
is_licenced=True
if is_old:
    print("you're old enough") #if true then print this..
print("check")





is_old=False
if is_old:
    print("you're old enough") #if true then print this..
else:
    print("not old")







is_old=False
is_licenced=True
if is_old:
    print("you're old enough") #if true then print this..
elif is_licenced:
    print("licenced")
else:
    print("not old")
print("check")








is_old=False
is_licenced=True
if is_old and is_licenced:
    print("you're old enough") #if true then print this..
else:
    print("not old")
print("check")






'''
output : 
you're old enough
check
not old
licenced
check
not old
check

'''