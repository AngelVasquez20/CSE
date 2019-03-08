class Item(object):
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.protection = 100
        self.health = 100

    def swinging(self):
        self.health -= 1
        print("You are swinging the door the sword")


class Shield(Item):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.health_left = 100


class Taser(Item):
    def __init__(self, name):
        super(Taser, self).__init__(name)
        self.damage = 100
        self.usage_left = 100


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.usage_left = 100
        self.protection = 20


class Knife(Item):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.damage = 100
        self.usage_left = 100


class Laptop(Item):
    def __init__(self, name):
        super(Laptop, self).__init__(name)
        self.battery_life = 100


class Armour(Item):
    def __init__(self, name):
        super(Armour, self).__init__(name)
        self.usage_left = 100
        self.protection = 60


class Gun(Item):
    def __init__(self, name):
        super(Gun, self).__init__(name)
        self.damage = 100
        self.range = 100
        self.usage_left = 100


class Clothes(Item):
    def __init__(self, name):
        super(Clothes, self).__init__(name)
        self.protection = 1


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.protection = 50
        self.damage = 50
        self.usage_left = 100


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)
        self.food_left = 100
        self.damage = 100


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)
        self.protection = 20
        self.usage_left = 100


class Pills(Item):
    def __init__(self, name):
        super(Pills, self).__init__(name)
        self.damage = 50
        self.life = 20


class Axe(Item):
    def __init__(self, name):
        super(Axe, self).__init__(name)
        self.damage = 80
        self.usage_left = 100


class Backpack(Item):
    def __init__(self, name):
        super(Backpack, self).__init__(name)
        self.space = 100
