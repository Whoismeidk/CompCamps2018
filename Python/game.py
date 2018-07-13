import location, player, item, enemy
import random
from datetime import datetime
seed = input("I request a seed from you: ")

tile = location.Location(seed + "0,0")

user = player.Player(input("What is your name?: "))

x = 0
y = 0
tiles = {}
searched_tiles = []

def move(direction):
    global x, y
    if direction == "n":
        y += 1
    elif direction == "e":
        x += 1
    elif direction == "w":
        x -= 1
    elif direction == "s":
        y -= 1
    key = "{}, {}".format(x, y)
    if key in tiles:
        return tiles[key]
    else:
        newtile = location.Location(seed + key)
        tiles[key] = newtile
        return newtile

running = True
while running and user.isAlive():
    print("You are in the {}".format(tile.name))
    if tile.enemy and tile.enemy.isAlive():
        print("You've been attacked! Your pursuer has {} health.".format(tile.enemy.health))
    command = input("> ")
    if command == "items":
        if user.inventory:
            print("You have: {}".format(user.getItems()))
        else:
            print("You're broke LUL")
    elif command == "move":
        direction = input("N/E/S/W > ")[0].lower()
        if direction == "n":
            print("You went North")
            tile = move("n")
        elif direction == "e":
            print("You went East")
            tile = move("e")
        elif direction == "s":
            print("You went South")
            tile = move("s")
        elif direction == "w":
            print("You went West")
            tile = move("w")
        else:
            print("No movement, I don't understand")
    elif command == "search":
        if tile.seed in searched_tiles:
            print("greedy scum")
        random.seed(seed + str(x) + str(y))
        if random.randint(1, 5) == 1:
            user.addItem(item.getRandomItem())
            print("Ayy, there's something on the ground.")
        else:
            print("Nope")
        searched_tiles.append(tile.seed)
    elif command == "fight":
        random.seed(datetime.now())
        while tile.enemy.isAlive() and user.isAlive():
            print("You have {} health!".format(user.health))
            command = input("Combat > ")
            if command == "attack":
                if random.randint(1,5) < 5:
                    print("You gottem! You hit for 3 damage.")
                    tile.enemy.health -= 3
                else:
                    print("You missed! How could you miss!? That's like missing the broad side of ten barns!")
            elif command == "spell":
                if random.randint(1,5) == 1:
                    print ("What an awesome kill! You did 10 damage.")
                    tile.enemy.health -= 10
                else:
                    print ("You don't know how to spell.")

            elif command.startswith("weapon"):
                _, item = command.split(" ", 1)
                if user.hasItem(item):
                    print("You have attacked the enemy with the {}.".format(item))
                    user.weapon(item)
                    tile.enemy.health -= item.damage(item)
                else:
                    print("You don't have that LUL")
                    continue

            if tile.enemy.health > 0:
                user.health -= tile.enemy.damage
    elif command.startswith("use"):
        _, item = command.split(" ", 1)
        if user.hasItem(item):
            print("You have eaten the {}".format(item))
            user.use(item)
            user.removeItem(item)
        else:
            print("You don't have {}s".format(item))
