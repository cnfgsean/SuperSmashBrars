import random
from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean
from People.jiyang import Jiyang
from People.sara import Sara
from People.peter import Peter


class Fight(object):
    turn = 1
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        
        self.p2.enemy = self.p1
        self.p1.enemy = self.p2

    #### make universally probably
    def damage(self, attacker, victim):
        damage = None
        victim.testdodged()
        
        actualattack = attacker.getActualATK()
        actualdodge = victim.getActualDODGE()
        actualcrit = attacker.getActualCRIT()
        actualdefense = victim.getActualDEF()
        
        #print("Atk = {}\nDodge = {}\nCrit = {}\nDef = {}\n".format(actualattack, actualdodge, actualcrit, actualdefense))
        attacker.doescrit = 2 if random.uniform(1, 100) < actualcrit else 1
        
        
        if actualdefense > 0:
            damage = victim.doesdodge * (max(0, attacker.doescrit * actualattack - actualdefense))
        else:
            damage = victim.doesdodge * (max(0, attacker.doescrit * actualattack - (2 * actualdefense)))

        if victim.doesdodge == 0:
            #print("The attack was dodged")
            pass
        else:
            if attacker.doescrit > 1:  # its greater than 1 because some characters will have a 3 crit multiplier
                pass
                #print("Was dealt a critical hit")
            #print("({}) took {} damage".format(victim.name, damage))
        victim.hp -= damage
        
    def run(self):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            self.p1, self.p2 = self.p2, self.p1


        lose = None

        while True:
            #print("TURN {}".format(self.turn))
            #print("{}'s Resource count: {}".format(self.p1.name, self.p1.resource))
            #print("{}'s Resource count: {}".format(self.p2.name, self.p2.resource))
            #print("Player 1 ({}) HP: {}".format(self.p1.name, self.p1.hp))
            #print("Player 2 ({}) HP: {}".format(self.p2.name, self.p2.hp))

           
            if self.p2.hp < 0:
                lose = self.p2
                break

            if self.p1.hp < 0:
                lose = self.p1
                break



            #p1c = input("{}: Select your move ({})".format(self.p1.name, "a, s" if self.p1.resource >= self.p1.srec else "a"))
            #p2c = input("{}: Select your move ({})".format(self.p2.name, "a, s" if self.p2.resource >= self.p2.srec else "a"))
            
            
            #for simulation
            p1c = 's'
            p2c = 's'
            
            #start passives

            self.p1.passive()
            self.p2.passive()



            if p1c.lower() == "s":
                if self.p1.resource >= self.p1.srec:
                    self.p1.isSpecial = True
                    self.p1.special()
                
            if p2c.lower() == "s":
                if self.p2.resource >= self.p2.srec:
                    self.p2.isSpecial = True
                    self.p2.special()
            #p1 attacks p2
            """
            print("({}) attacks ({})".format(self.p1.name, self.p2.name))

            p1.doescrit = 2 if random.uniform(1, 100) < self.p1.crit else 1
            self.p2.damage(self.p1.attack, doescrit)

            #p2 attacks p1
            print("({}) attacks ({})".format(self.p2.name, self.p1.name))

            p2.doescrit = 2 if random.uniform(1, 100) < self.p2.crit else 1
            self.p1.damage(self.p2.attack, doescrit)
            """
            #print("({}) attacks ({})".format(self.p1.name, self.p2.name))
            self.damage(self.p1, self.p2)

            #p2 attacks p1
            #print("({}) attacks ({})".format(self.p2.name, self.p1.name))
            self.damage(self.p2, self.p1)
            
            
            #print("MODIFIERS")
            #print(self.p1.modifiers)
            #print(self.p2.modifiers)
            #print("-----------------------------------")
            
            #death checks


            if self.p2.hp < 0:
                lose = self.p2
                break
                
            if self.p1.hp < 0:
                lose = self.p1
                break

            

            # end passives

            #self.p1.passiveend()
            #self.p2.passiveend()

            #This function should be removed
            #self.p1.specialend()
            #self.p2.specialend()
  
            self.p1.endround()
            self.p2.endround()
            
            
            self.turn += 1
            #print("\n\n")
           
        #print("{} loses!".format(lose.name))
        #print("{} : {}\n{} : {}".format(self.p1.name, self.p1.hp, self.p2.name, self.p2.hp))
        return lose.name
    
#####    


#for simulation
d = {"Sara" : 0, "Arvin" : 0}
for _ in range(100000):
    game = Fight(Sara(), Arvin())
    d[game.run()] += 1

print(d)
