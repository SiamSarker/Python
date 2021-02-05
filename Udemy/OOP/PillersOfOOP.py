# inheritance

class User():
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')

class Wizerd(User):
    def __init__(self, name, power):
        super().__init__(self)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        super().__init__(self)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows {self.num_arrows}')


wizerd1 = Wizerd('Siam', 50)
archer1 = Archer('Robin', 100)

print(dir(wizerd1))

# wizerd1.attack()
# archer1.attack()



# wizard1 = Wizerd('Siam', 20)
#
# print(isinstance(wizard1, object))
#

# Polymorphism

# def player_attack(char):
#     char.attack()
#
# player_attack(wizerd1)
# player_attack(archer1)
#
# for char in [wizerd1, archer1]:
#     char.attack()
