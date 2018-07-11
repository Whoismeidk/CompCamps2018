import random, enemy

descriptions = ["Angry", "Screaming", "Busy", "Deadly"]
location_types = ["Mountain", "Volcano", "Town", "sky"]


class Location:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)
        self.name = "{} {}".format(
                random.choice(descriptions),
                random.choice(location_types)
            )
        self.enemy = enemy.get()
