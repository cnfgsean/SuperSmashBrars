import random
from character import Character

class Arvin(Character):
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2100, attack=170, dodge=10, crit=20, defense=20,
                         gender=0)
        self.srec = 2

    def passive(self):
        o = self.hp
        self.hp = min(2100, self.hp + random.randint(40, 60))
        
        print("({}) heals {} health".format(self.name, self.hp - o))

    def special(self):
        self.attack += (40) 
        self.resource -= self.srec