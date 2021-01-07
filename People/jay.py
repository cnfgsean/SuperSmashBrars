import random
from character import Character

class Jay(Character):
    selfhit = 12
    hitself = False

    def __init__(self):
        super().__init__("Jay", title="GayJay47", hp=3800, attack=280, dodge=0, crit=10, defense=50, gender=0)
        self.srec = 11

    def passive(self):
        #print(self.selfhit)
        if random.uniform(1, 100) < self.selfhit:
            #print("hsbfjsdfbfhsbfhjfbhjsfs")
            self.hitself = True
            c = 2 if random.uniform(1, 100) < self.getActualCRIT() else 1
            self.hp -= c * (self.getActualATK() - self.getActualDEF())
            print("Jay dealt {} damage to himself!".format(c * self.attack - self.defense))

            self.attack = 0

    def passiveend(self):
        self.attack = 280
        #self.selfhit = 12

    def special(self):
        self.modifiers['attack']['selfmult'] += 1
        self.modifiers['crit']['selfadd'] += 1000
        self.modifiers['defense']['selfadd'] += -100
        
        self.enemy.modifiers['dodge']['othermult'] += -1
        
        
       
       
        self.resource -= self.srec
        return "undodgeable"
        

    def endround(self):
        
        self.selfhit += 3

        if self.hitself:
            self.passiveend()
            self.hitself = False
            
        if self.isSpecial:
            self.modifiers['attack']['selfmult'] -= 1
            self.modifiers['crit']['selfadd'] -= 1000
            self.modifiers['defense']['selfadd'] -= -100
            self.enemy.modifiers['dodge']['othermult'] -= -1
            
        super().endround()
            
            
