class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Siam', 20)
player2 = PlayerCharacter('Tom', 18)

print(player1.run())
print(player2.name)
