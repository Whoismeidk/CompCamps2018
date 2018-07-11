import random

def get():
    if random.randint(1,10) == 1:
        return Enemy()

    else:
        return None
class Enemy:
    def __init__(self):
        self.health = random.randint(1, 5)
        self.damage = random.randint(1, 5)

    def isAlive(self):
        return self.health > 0
