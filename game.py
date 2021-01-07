import random
from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean
from People.jiyang import Jiyang

class Fight(object):
    turn = 1
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def run(self):
        coinflip = random.randint(0,1)
        if coinflip == 0:
            self.p1, self.p2 = self.p2,self.p1

        lose = None

        while True:
            print("TURN {}".format(self.turn))
            print("{}'s Resource count: {}".format(self.p1.name, self.p1.resource))
            print("{}'s Resource count: {}".format(self.p2.name, self.p2.resource))
            print("Player 1 ({}) HP: {}".format(self.p1.name, self.p1.hp))
            print("Player 2 ({}) HP: {}".format(self.p2.name, self.p2.hp))

            if self.p1.hp < 0:
                lose = self.p1
                break

            if self.p2.hp < 0:
                lose = self.p2
                break

            #start passives

            self.p1.passive()
            self.p2.passive()

            #p1 attacks p2
            print("({}) attacks ({})".format(self.p1.name, self.p2.name))

            doescrit = 2 if random.uniform(1, 100) < self.p1.crit else 1
            self.p2.damage(self.p1.attack, doescrit)

            #p2 attacks p1
            print("({}) attacks ({})".format(self.p2.name, self.p1.name))

            doescrit = 2 if random.uniform(1, 100) < self.p2.crit else 1
            self.p1.damage(self.p2.attack, doescrit)

            #death checks

            if self.p1.hp < 0:
                lose = self.p1
                break

            if self.p2.hp < 0:
                lose = self.p2
                break

            # end passives

            self.p1.passiveend()
            self.p2.passiveend()

            #This function should be removed
            #self.p1.specialend()
            #self.p2.specialend()
  
            self.p1.endround()
            self.p2.endround()
            
            
            self.turn += 1
            print("\n\n")
           
        print("{} loses!".format(lose.name))
    
    
game = Fight(Arvin(), Sean())
game.run()




