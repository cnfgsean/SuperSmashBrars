from character import Character

class Romir(Character):
    def __init__(self):
        super().__init__("Romir", title="Prophet, Pimp, Maverick", hp=1200, attack=150, dodge=15, crit=15, defense=20,
                         gender=0)
        self.srec = 0
        self.canRespawn = True
   
    
    def special(self):
        pass
      
    def onDeath(self):
        super().onDeath()
        if self.canRespawn:
            self.hp = 1200
            
            print("THE PIMP RETURNS! {} respawned".format(self.name))
            self.canRespawn = False
            
        
          
    def endround(self):            
        super().endround()
        
        
