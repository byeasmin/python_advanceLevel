class playerCharacter:
    membership=True
    def __init__(self, name, age):
            self.name=name   #attricutes / properties
            self.age=age

    def shout(self):
        print(f'my name is {self.name}')


# @classmethod
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('meem', num1 + num2)



# staticmethod
    @staticmethod
    def adding_things(num1, num2):
        return num1 + num2



# player1=playerCharacter("benin", 22)
player3 = playerCharacter.adding_things(12,11)
print(player3.age)













