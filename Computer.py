from random import randint
from Player import *

class Computer(Player):
    def __init__(self,name="CPU"):
        super().__init__(name)

    def newPick(self):
        self.lastInput = randint(0,3)