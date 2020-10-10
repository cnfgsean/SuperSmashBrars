from character import Character

class Sean(Character):
    def __init__(self):
        super().__init__("Sean", title="Long Dong Sean Fong", hp=1200, attack=160, dodge=30, crit=30, defense=20,
                         gender="male")
        self.srec = 2

    def passive(self):
        self.crit += 0.03 * 30
        self.dodge += 0.03 * 30

    def special(self):
        olddodge = self.dodge
        oldcrit = self.crit

        self.dodge = 100
        self.crit = 100

        self.dodge = olddodge
        self.crit = oldcrit