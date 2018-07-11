import random

class Item:
    def __init__(self, name, damage, healing):
        self.name = name
        self.damage = damage
        self.healing = healing

items = [
    Item("Potion", 0, 10),
    Item("Knife", 10, 0),
    Item("Crowbar", 4, 0),
    Item("Lamp", 0, 5),
    Item("Flashlight", 0, 2)
]

def getRandomItem():
    return random.choice(items)
