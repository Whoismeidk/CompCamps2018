import item as items

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 15

    def addItem(self, item):
            self.inventory.append(item)

    def hasItem(self, name):
        for item in self.inventory:
            if item.name == name:
                return True
        return False

    def getItems(self):
        items = []
        for item in self.inventory:
            items.append(item.name)
        return items

    def isAlive(self):
        return self.health > 0

    def removeItem(self, name):
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if item.name == name:
                self.inventory.pop(i)
                return

    def use(self, name):
        if self.hasItem(name):
            for item in items.items:
                if item.name == name:
                    self.health += item.healing

    def weapon(self,name):
        if self.hasItem(name):
            for item in items.items:
                if item.name == name:
                    return items.damage(items)
