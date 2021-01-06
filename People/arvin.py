import random
from character import Character

class Arvin(Character):
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2100, attack=170, dodge=10, crit=20, defense=20,
                         gender="male")
        self.srec = 1

    def passive(self):
        self.hp = min(2100, self.hp + random.randint(40, 60))

    def special(self):
        self.attack += (20) * self.resource
        self.resource = 0