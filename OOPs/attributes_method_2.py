class playerCharacter:
    membership=True
    def __init__(self, name, age):
        if (playerCharacter.membership):
            self.name=name   #attricutes / properties
            self.age=age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

player1=playerCharacter("benin", 22)
player2=playerCharacter("yeasmin", 23)
player2.attack=50


print(player1.run('hello'))
print(player2.shout())












'''
Output : 
my name is benin
None
my name is yeasmin
None
'''