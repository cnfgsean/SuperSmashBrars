from character import Character

class Phillip(Character):
    def __init__(self):
        super().__init__("Phillip", title="Erik Rygh", hp=1000, attack=200, dodge=50, crit=10, defense=10,
                         gender=0)
        self.srec = 4

    def passive(self):
        #print(self.team)
        if 1 in [p.gender for p in self.team]:
            self.modifiers['attack']['selfadd'] = 50
            self.modifiers['defense']['selfadd'] = 30
        else:
            self.modifiers['attack']['selfadd'] = 0
            self.modifiers['defense']['selfadd'] = 0
        
        if self.enemy.gender == 1:
            self.modifiers['dodge']['selfmult'] = 0.8
        else:
            self.modifiers['dodge']['selfmult'] = 1
        
        
        
    
    
    def special(self):
        self.resource -= self.srec
    
    def endround(self):
        if self.isSpecial:
            pass
            
        super().endround()
        
        
