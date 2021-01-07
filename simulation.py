import random
from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean
from People.jiyang import Jiyang
from People.sara import Sara
from People.peter import Peter

from game import Fight # this triggers a fight from the last two lines of game.py

# for simulation
d = {"Sara" : 0, "Arvin" : 0}
for _ in range(10000):
    game = Fight(Sara(), Arvin(), False)
    d[game.run()] += 1

print(d)
