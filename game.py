import random

from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean

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
            
            specialstatus1 = True if self.p1.resource >= self.p1.srec else False
            specialstatus2 = True if self.p2.resource >= self.p2.srec else False
            
            p1move = input("Select Player 1 Move (a, {}d)".format("s, " if specialstatus1 else ""))
            p2move = input("Select Player 2 Move (a, {}d)".format("s, " if specialstatus2 else ""))
            
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
                 
                 
                if specialstatus2 and p2move == 's':
                    self.p2.special()

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
##############################################                

                if specialstatus1 and p1move == 's':
                    self.p1.special()
                    
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
                
                if specialstatus2 and p2move == 's':
                    self.p2.special()
                    
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
################################################## 
                if specialstatus2 and p2move == 's':
                    self.p2.special()
                    
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
            
            #self.p1.specialend()
            #self.p2.specialend()
            
            
            self.p1.passiveend()
            self.p2.passiveend()
            
  
            self.p1.endround()
            self.p2.endround()
            
            
            self.turn += 1
            print("\n\n")
           
        print("{} loses!".format(lose.name))
    
    
game = Fight(Sean(), Arvin())
game.run()






        