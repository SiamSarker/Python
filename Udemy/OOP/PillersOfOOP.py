# inheritance

class User():
    def sign_in(self):
        print('logged in')
    def attack(self):
        print('do nothing')

class Wizerd(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'{self.num_arrows} remaining')

    def attack(self):
        print(f'Attacking with arrows {self.num_arrows}')

    def run(self):
        print('ran really fast')

class HybridBorg(Wizerd, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizerd.__init__(self, name, power)


hb1 = HybridBorg('Borgie', 50, 100)

print(hb1.check_arrows())
print(hb1.attack())


# wizerd1 = Wizerd('Siam', 50)
# archer1 = Archer('Robin', 100)
#
# print(dir(wizerd1))

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
