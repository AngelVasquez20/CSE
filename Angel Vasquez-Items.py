class Item(object):
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.protection = 100
        self.usage = 100

    def swinging(self):
        self.usage -= 1
        print("You are swinging the door the sword")


class Wood(Sword):
    def __init__(self):
        super(Wood, self).__init__("Wood Sword")


class Iron(Sword):
    def __init__(self):
        super(Iron, self).__init__("Iron Sword")


class Steel(Sword):
    def __init__(self):
        super(Steel, self).__init__("Steel Sword")


class Shield(Item):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.health_left = 100


class Big(Shield):
    def __init__(self):
        super(Big, self).__init__("Big Shield")


class Small(Shield):
    def __init__(self):
        super(Small, self).__init__("Small Shield")


class Taser(Item):
    def __init__(self, name):
        super(Taser, self).__init__(name)
        self.damage = 100
        self.usage_left = 100


class Tasergun(Taser):
    def __init__(self):
        super(Tasergun, self).__init__("Taser Gun")


class Black(Taser):
    def __init__(self):
        super(Black, self).__init__("Black Taser")


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.usage_left = 100
        self.protection = 20


class SteelH(Helmet):
    def __init__(self):
        super(SteelH, self).__init__("Steel Helmet")


class IronH(Shield):
    def __init__(self):
        super(IronH, self).__init__("Iron Helmet")


class Knife(Item):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.damage = 100
        self.usage_left = 100


class SharpK(Knife):
    def __init__(self):
        super(SharpK, self).__init__("Sharp Knife")


class Thin(Knife):
    def __init__(self):
        super(Thin, self).__init__("Thin Knife")


class Laptop(Item):
    def __init__(self, name):
        super(Laptop, self).__init__(name)
        self.battery_life = 100


class AppleLaptop(Laptop):
    def __init__(self):
        super(AppleLaptop, self).__init__("Apple Laptop")


class Asus(Laptop):
    def __init__(self):
        super(Asus, self).__init__("Asus Laptop")


class ChestArmour(Item):
    def __init__(self, name):
        super(ChestArmour, self).__init__(name)
        self.usage_left = 100
        self.protection = 60


class SteelA(ChestArmour):
    def __init__(self):
        super(SteelA, self).__init__("Steel Armour")


class IronA(ChestArmour):
    def __init__(self):
        super(IronA, self).__init__("Iron Armour")


class Gun(Item):
    def __init__(self, name):
        super(Gun, self).__init__(name)
        self.damage = 100
        self.range = 100
        self.bullets_left = 100


class Ak47(Gun):
    def __init__(self):
        super(Ak47, self).__init__("Ak47")


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol")


class Sniper(Gun):
    def __init__(self):
        super(Sniper, self).__init__("Sniper")


class Clothes(Item):
    def __init__(self, name):
        super(Clothes, self).__init__(name)
        self.protection = 1


class Pants(Clothes):
    def __init__(self):
        super(Pants, self).__init__("Pants")


class Shirt(Clothes):
    def __init__(self):
        super(Shirt, self).__init__("Shirt")


class Sweater(Clothes):
    def __init__(self):
        super(Sweater, self).__init__("Sweater")


class Socks(Clothes):
    def __init__(self):
        super(Socks, self).__init__("Socks")


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.protection = 50
        self.damage = 50
        self.usage_left = 100


class LifeP(Potion):
    def __init__(self):
        super(LifeP, self).__init__("Life Potion")


class HarmfulP(Potion):
    def __init__(self):
        super(HarmfulP, self).__init__("Harmful Potion")


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)
        self.food_left = 100
        self.damage = 100


class Chicken(Food):
    def __init__(self):
        super(Chicken, self).__init__("Chicken")

class


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


class Water(Item):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.space = 100
