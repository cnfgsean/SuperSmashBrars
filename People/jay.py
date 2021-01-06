import random
from character import Character

class Jay(Character):
    selfhit = 12
    hitself = False

    def __init__(self):
        super().__init__("Jay", title="GayJay47", hp=3800, attack=280, dodge=0, crit=10, defense=50, gender="male")
        self.srec = 11

    def passive(self):
        if random.uniform(1, 100) < self.selfhit:
            self.hitself = True
            self.hp -= (self.attack - self.defense)

            c = 2 if random.uniform(1, 100) < self.crit else 1
            print("Jay dealt {} damage to himself!".format(c * self.attack - self.defense))

            self.attack = 0

    def passiveend(self):
        self.attack = 280
        # self.selfhit = 12

    def special(self):
        self.attack *= 2
        self.crit = 100
        self.defense -= 100
        self.resource -= 10
        return "undodgeable"

    def specialend(self):
        self.attack = 280
        self.crit = 10
        

    def endround(self):
        super().endround()
        self.selfhit += 3

        if self.hitself:
            self.passiveend()
            self.hitself = False
