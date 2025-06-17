class playerCharacter:
    def __init__(self, name, age):
        self.name=name   #attricutes / properties
        self.age=age

    def run(self):
        print('run')

player1=playerCharacter("benin", 22)
player2=playerCharacter("yeasmin", 23)

print(player1)
print(player2)
print(player1.name)
print(player2.name)
print(player1.age)
print(player2.age)










'''
Output :
<__main__.playerCharacter object at 0x00000142477D9370>
<__main__.playerCharacter object at 0x00000142477D93A0>
benin
yeasmin
22
23

'''

