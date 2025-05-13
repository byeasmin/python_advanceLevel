# password checker..

username=input("what's your name ? ")
password=input("what's your password ? ")

password_length=len(password)
hidden_password="*" * password_length

print(f"{username}, your password, {hidden_password}, is {password_length} letters long.")




'''
output : 
what's your name ? yeasmin
what's your password ? 123456
yeasmin, your password, ******, is 6 letters long.
'''