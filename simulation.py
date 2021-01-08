import random
from People.arvin import Arvin
from People.jay import Jay
from People.sean import Sean
from People.jiyang import Jiyang
from People.sara import Sara
from People.peter import Peter
from People.phillip import Phillip
from People.romir import Romir

from game import Fight # this triggers a fight from the last line of game.py, unrelated to the simulation

# for simulation
d = {"Romir" : 0, "Arvin" : 0}
for _ in range(10000):
    game = Fight(Romir(), Arvin(), False)
    d[game.run()] += 1

print(d)
