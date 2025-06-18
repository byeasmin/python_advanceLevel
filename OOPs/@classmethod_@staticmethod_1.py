class playerCharacter:
    membership=True
    def __init__(self, name, age):
            self.name=name   #attricutes / properties
            self.age=age

    def shout(self):
        print(f'my name is {self.name}')


# @classmethod

    @classmethod
    # def adding_things(num1, num2):         # getting error..
    def adding_things(cls, num1, num2):
        return num1 + num2



player1=playerCharacter("benin", 22)
print(player1.adding_things(2,3))
print(playerCharacter.adding_things(4, 5))









'''
Output : 
5
9

'''

