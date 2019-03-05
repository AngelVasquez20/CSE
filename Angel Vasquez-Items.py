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


class Iron(Sword):
    def __init__(self):
        super(Iron, self).__init__("Iron")


class Shield(Item):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.health_left = 100
