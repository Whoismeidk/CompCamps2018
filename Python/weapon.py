import random

class Item:
    def __init__(self, name, damage, healing):
        self.name = name
        self.damage = damage
        self.healing = healing

items = [
    Item("Knife", 10, 0),
    Item("Crowbar", 4, 0),
]

def getRandomItem():
    return random.choice(items)
