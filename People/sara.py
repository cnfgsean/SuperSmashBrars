from character import Character

class Sara(Character):
    def __init__(self):
        super().__init__("Sara", title="Saraline Hooey", hp=1600, attack=150, dodge=20, crit=15, defense=10,
                         gender=1)
        self.srec = 3
        self.sccount = 0

    def passive(self):      
        self.modifiers['crit']['selfadd'] += 5
                 
    
    def special(self):
        self.enemy.modifiers['defense']['otheradd'] += -110
        self.resource -= self.srec
    
    
    """
    def onswap(self):
        self.modifiers['crit']['selfadd'] = 0
        self.crit = int(self.crit/2)
    
    """
    def endround(self):
        
        if self.isSpecial:
            self.sccount = 4
        
        if self.sccount > 0:
        
            self.enemy.modifiers['defense']['otheradd'] -= -20
            self.sccount -= 1
            
            if self.sccount == 1:
                self.enemy.modifiers['defense']['otheradd'] -= -40
                self.sccount = 0
                
                
        
        """
        if self.isSpecial:
            self.enemy.modifiers['defense']['otheradd'] -= -100
        """
        super().endround()
        
       
       
