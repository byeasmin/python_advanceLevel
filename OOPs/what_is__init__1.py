class playerCharacter:
    membership=True
    def __init__(self, name='anonymous', age=0):
        if (age>18):
            self.name=name   #attricutes / properties
            self.age=age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self, hello):
        print(f'my name is {self.name}')

player1=playerCharacter('tom', 19)   # age defaults to 0 → age > 18 condition fails
player2=playerCharacter()

print(player2.shout())
