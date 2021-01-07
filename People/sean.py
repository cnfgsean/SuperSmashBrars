from character import Character

class Sean(Character):
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=30, crit=30, defense=20,
                         gender=0)
        self.srec = 2

    def passive(self):
        
        self.modifiers['crit']['selfadd'] += 3
        self.modifiers['dodge']['selfadd'] += 3
        
    
    
    def special(self):

        self.modifiers['dodge']['selfmult'] = 100000
        self.modifiers['crit']['selfmult'] = 100000
        self.resource -= self.srec
    
    def endround(self):
        if self.isSpecial:
            self.modifiers['dodge']['selfmult'] = 1
            self.modifiers['crit']['selfmult'] = 1
            
        super().endround()
        
        
