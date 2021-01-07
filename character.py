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

    def dodged(self):
        return 1 if random.uniform(1, 100) > self.dodge else 0

    def damage(self, opponentattack, critmult):
        damage = None
        dodgemult = self.dodged()
        if self.defense > 0:
            damage = dodgemult * (max(0, critmult * opponentattack - self.defense))
        else:
            damage -= dodgemult * (max(0, critmult * opponentattack - (2 * self.defense)))

        if critmult > 1:  # its greater than 1 because some characters will have a 3 crit multiplier
            print("Was dealt a critical hit")

        if dodgemult == 0:
            print("The attack was dodged")
        else:
            print("({}) took {} damage".format(self.name, damage))
        self.hp -= damage

    def endround(self):
        self.resource += 1
