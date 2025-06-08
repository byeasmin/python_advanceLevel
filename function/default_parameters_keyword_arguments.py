# parameters..
# def say_hellow(name, emoji):
#     print(f'hello {name} {emoji}')


#default parameters..
def say_hellow(name='umme', emoji='🥸'):
    print(f'hello {name} {emoji}')

#arguments..
say_hellow('benin', '😊')
say_hellow('yeasmin', '😊')


#keyword arguments..
# say_hellow(emoji='😒', name='benin')
say_hellow(name='meem', emoji='😒')
say_hellow()
say_hellow('benin')
say_hellow('❤️')  # default parameters..






'''
Output : 
hello benin 😊
hello yeasmin 😊
hello meem 😒
hello umme 🥸
hello benin 🥸
hello ❤️ 🥸
'''



