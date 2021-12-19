class PlayerCharacter:
    # class Object Attribute
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')
        return 'done'

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Anas', num1 + num2)

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter('Siam', 20)
player2 = PlayerCharacter('Tom', 18)

print(player1.shout())
print(player1.adding_things2(5, 6))

player3 = PlayerCharacter.adding_things(8, 9)
print(player3.age)
