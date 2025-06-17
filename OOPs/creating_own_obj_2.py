class playerCharacter:
    def __init__(self, name, age):
        self.name=name   #attricutes / properties
        self.age=age

    def run(self):
        print('run')
        return 'done'

player1=playerCharacter("benin", 22)
player2=playerCharacter("yeasmin", 23)
player2.attack=50

print(player1.run())
print(player2.run())
print(player2.attack)












'''
Output : 
run
done
run
done
50
'''



