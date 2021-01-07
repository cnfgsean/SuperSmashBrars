from character import Character
import random

class Peter(Character):
    def __init__(self):
        super().__init__("Peter", title="Thicc Booty", hp=2500, attack=180, dodge=15, crit=15, defense=5,
                         gender=0)
        self.srec = 0

    def passive(self):
        pass
        
    
    
    def special(self):
        self.enemy.modifiers['attack']['othermult'] += -self.resource * 0.01
        self.enemy.modifiers['dodge']['othermult'] += -self.resource * 0.01
        self.enemy.modifiers['crit']['othermult'] += -self.resource * 0.01
        self.enemy.modifiers['defense']['othermult'] += -self.resource * 0.01
        
        print("{}'s stats dropped {}%!".format(self.enemy.name, self.resource))
        self.resource = 0
    
    def endround(self):
        if random.uniform(1, 100) <= 40: 
            self.resource += 2
            
        if self.doescrit != 1:
            self.resource += 3
        
        if self.doesdodge != 1:
            self.resource += 3
            
            
            
        super().endround()
        
        
