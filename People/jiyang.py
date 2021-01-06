from character import Character
import random
class Jiyang(Character):
    def __init__(self):
        super().__init__("Jiyang", title="African American Paragon", hp=700, attack=210, dodge=70, crit=50, defense=3,
                         gender="male")
        self.srec = 1

    def passive(self):
        if random.uniform(1, 100) <= 30:
            print("Jiyang's attack missed")
            self.attack = 0

    def passiveend(self):
        self.attack = 210
    
    
    def specialend(self):
        pass
    
    def special(self):
        self.resource -= self.srec
        self.srec += 3 
        if random.randint(1, 6) == 1:
            print("We may be equal, but some are more equal than others")
            return "communism"
            
  
        
