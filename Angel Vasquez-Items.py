class Item(object):
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.damage = 100
        self.health = 100

    def swinging(self):
        self.health -= 1
        print("You are swinging the door the sword")


class Shield(Item):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.health_left = 100


class Tazer(Item):
    def __init__(self, name):
        super(Tazer, self).__init__(name)
        self.damage = 100
        self.health_left = 100


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.use_left = 100


class Knife(Item):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.damage = 100
        self.use_left = 100


class Laptop(Item):
    def __init__(self, name):
        super(Laptop, self).__init__(name)
        self.battery_life = 100
