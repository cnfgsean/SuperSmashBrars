import random

class Fight(object):
    turn = 1
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
    def run(self):
        coinflip = random.randint(0,1)
        while True:
            print("TURN {}".format(self.turn))
            print("Player 1 ({}) HP: {}".format(self.p1.name, self.p1.hp))
            print("Player 2 ({}) HP: {}".format(self.p2.name, self.p2.hp))
            
            p1move = input("Select Player 1 Move (a, {}d)".format("s, " if self.p1.resource >= self.p1.srec else ""))
            p2move = input("Select Player 2 Move (a, {}d)".format("s, " if self.p2.resource >= self.p2.srec else ""))
            
            if coinflip == 0:
                self.p1.passive()
                if self.p1.hp <= 0:
                    lose = self.p1
                    break
                self.p2.passive()
                if self.p2.hp <= 0:
                    lose = self.p2
                    break
            else:
                self.p2.passive()
                if self.p2.hp <= 0:
                    lose = self.p2
                    break
                self.p1.passive()
                if self.p1.hp <= 0:
                    lose = self.p1
                    break
                
            
            
            """
            if p1move == 'd':
                p1oldd = self.p1.defense
                p1olda = self.p1.attack
                self.p1.defense *= 3
                self.p1.attack = 0
                
                
            if p2move == 'd':
                p2oldd = self.p2.defense
                p2olda = self.p2.attack
                self.p2.defense *= 3
                self.p2.attack = 0
            """
            
            lose = None
            
            # p2 attack p1 #
            if coinflip == 0:
                print("Player 2 ({}) Attacks first!".format(self.p2.name))
                d = 0 if random.uniform(1, 100) < self.p1.dodge else 1
                if d == 0:
                    print("Player 1 ({}): Dodged Player 2's ({}) Attack!".format(self.p1.name, self.p2.name))  
                c = 2 if random.uniform(1, 100) < self.p2.crit else 1
                if c == 2 and d == 1:
                    print("Player 2 ({}): Critical Hit!".format(self.p2.name))
                
                damage = d*(max(0, c*self.p2.attack - self.p1.defense))
                print("Player 2 dealt {} damage!".format(damage))
                self.p1.hp -=  damage
                if self.p1.hp <= 0:
                    lose = self.p1
                    break
                        
                d = 0 if random.uniform(1, 100) < self.p2.dodge else 1
                if d == 0:
                    print("Player 2 ({}): Dodged Player 1's ({}) Attack!".format(self.p2.name, self.p1.name))               
                c = 2 if random.uniform(1, 100) < self.p1.crit else 1
                if c == 2 and d == 1:
                    print("Player 1 ({}): Critical Hit!".format(self.p1.name))   

                damage = d*(max(0, c*self.p1.attack - self.p2.defense))
                print("Player 1 dealt {} damage!".format(damage))                
                self.p2.hp -= damage
                if self.p2.hp <= 0:
                    lose = self.p2
                    break
            else:
                print("Player 1 ({}) Attacks first!".format(self.p1.name))
                d = 0 if random.uniform(1, 100) < self.p2.dodge else 1
                if d == 0:
                    print("Player 2 ({}): Dodged Player 1's ({}) Attack!".format(self.p2.name, self.p1.name))           
                c = 2 if random.uniform(1, 100) < self.p1.crit else 1
                if c == 2 and d == 1:
                    print("Player 1 ({}): Critical Hit!".format(self.p1.name))               
                
                damage = d*(max(0, c*self.p1.attack - self.p2.defense))
                print("Player 1 dealt {} damage!".format(damage))                
                self.p2.hp -= damage
                if self.p2.hp <= 0:
                    lose = self.p2
                    break         
                    
                d = 0 if random.uniform(1, 100) < self.p1.dodge else 1
                if d == 0:
                    print("Player 1 ({}): Dodged Player 2's ({}) Attack!".format(self.p1.name, self.p2.name))                          
                c = 2 if random.uniform(1, 100) < self.p2.crit else 1
                if c == 2 and d == 1:
                    print("Player 2 ({}): Critical Hit!".format(self.p2.name))
                
                damage = d*(max(0, c*self.p2.attack - self.p1.defense))
                print("Player 2 dealt {} damage!".format(damage))
                self.p1.hp -=  damage
                if self.p1.hp <= 0:
                    lose = self.p1
                    break
                            
            """
            if p1move == 'd':
                self.p1.defense = p1oldd
                self.p1.attack = p1olda
                
                
            if p2move == 'd':
                self.p2.defense = p2oldd
                self.p2.attack = p2olda
            """
            self.p1.passiveend()
            self.p2.passiveend()
            
            self.p1.endround()
            self.p2.endround()
            
            
            self.turn += 1
            print("\n\n")
           
        print("{} loses!".format(lose.name))
            

class Character(object):   
    #self.properties = {name : None, hp : None, attack : None, dodge : None, crit : None, defense : None, gender : None}
    def __init__(self, name, title, hp, attack, dodge, crit, defense, gender):
        self.name = name
        self.title = title
        self.hp = hp
        self.attack = attack
        self.dodge = dodge
        self.crit = crit
        self.defense = defense
        self.gender = gender.lower()
        self.resource = 0
        
        #self.modifiers = {hp : 1, attack : 1, dodge : 1, crit : 1, defense : 1}
    
    def passive(self):
        pass
        
    def passiveend(self):
        pass
     
    def special(self):
        pass
        
    def onSwap(self):
        pass
        
    def a(self):
        pass
        
    def d(self):
        pass
        
    def endround(self):
        self.resource += 1

class Sean(Character): 
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=30, crit=30, defense=20, gender="male")
        self.srec = 2
    
    def passive(self):
        self.crit += 0.03*30
        self.dodge += 0.03*30
      
    def special(self):
        olddodge = self.dodge
        oldcrit = self.crit
        
        self.dodge = 100
        self.crit = 100
    
        self.dodge = olddodge
        self.crit = oldcrit
        
      
    
class Arvin(Character): 
    def __init__(self):
        super().__init__("Arvin", title="The Vegetarian", hp=2100, attack=170, dodge=10, crit=20, defense=20, gender="male")
        self.srec = 2
        
    def passive(self):
        self.hp = min(2100, self.hp+random.randint(40, 60))
        
    def special(self):
        self.attack += (20)*self.resource
        self.resource = 0
  
  
class Jay(Character): 
    selfhit = 12
    hitself = False
    
    def __init__(self):
        super().__init__("Jay", title="GayJay47", hp=3800, attack=280, dodge=0, crit=10, defense=50, gender="male")
        self.srec = 8
        
    def passive(self):
        if random.uniform(1,100) < self.selfhit:
            self.hitself = True
            self.hp -= (self.attack - self.defense)
            
            c = 2 if random.uniform(1, 100) < self.crit else 1
            print("Jay dealt {} damage to himself!".format(c*self.attack - self.defense))
            
            self.attack = 0
        
    def passiveend(self):
        self.attack = 280
        #self.selfhit = 12
        
    def special(self):
        pass
        
    def endround(self):
        super().endround()
        self.selfhit += 3
        
        if self.hitself:
            self.passiveend()
            self.hitself = False
        
    
             
    
    
game = Fight(Jay(), Arvin())
game.run()






        