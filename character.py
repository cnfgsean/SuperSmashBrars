import random
class Character(object):
    # self.properties = {name : None, hp : None, attack : None, dodge : None, crit : None, defense : None, gender : None}
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

        # self.modifiers = {hp : 1, attack : 1, dodge : 1, crit : 1, defense : 1}

    def passive(self):
        pass

    def passiveend(self):
        pass

    def special(self):
        pass

    def onSwap(self):
        pass

    def critical(self):
        return 2 if random.uniform(1, 100) < self.crit else 1

    def damage(self, dodgemultiplier):
        if self.defense > 0:
            self.hp -= dodgemultiplier *(max(0, self.critical() *self.attack - self.defense))
        else:
            self.hp -= dodgemultiplier *(max(0, self.critical() *self.attack - (2*self.defense)))



    def endround(self):
        self.resource += 1