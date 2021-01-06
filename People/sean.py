from character import Character

class Sean(Character):
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=30, crit=30, defense=20,
                         gender="male")
        self.srec = 2

    def passive(self):
        
        self.crit += 3
        self.dodge += 3
        
        global ocrit 
        ocrit = self.crit
        
        global ododge 
        ododge = self.dodge
    
    def specialend(self):
        
        self.dodge = ododge
        self.crit = ocrit
    
    def special(self):

        self.dodge = 100
        self.crit = 100
        self.resource -= 2
  
        
