# # help(list)
#
#
# class playerCharacter:
#     def __init__(self, name, age):
#         self.name=name   #attricutes / properties
#         self.age=age
#
#     def run(self):
#         print('run')
#         return 'done'
#
# player1=playerCharacter("benin", 22)
# player2=playerCharacter("yeasmin", 23)
# player2.attack=50
#
#
# help(player1)

# print(player1.run())
# print(player2.run())
# print(player2.attack)



class playerCharacter:
    membership=True
    def __init__(self, name, age):
        # if (self.membership):
        if (playerCharacter.membership):
            self.name=name   #attricutes / properties
            self.age=age

    def run(self):
        print('run')
        return 'done'

player1=playerCharacter("benin", 22)
player2=playerCharacter("yeasmin", 23)
player2.attack=50

print(player1.name)
print(player2.membership)
print(player1.membership)










'''
Output :
benin
True
True
'''









