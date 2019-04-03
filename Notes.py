class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done because some FABULOUS armor!")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attack %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


# Items
sword = Weapon("Sword", 10)
canoe = Weapon("Canoe", 84)
wiebe_armour = Armor("Armour of the gods", 100000000000000000)

# Character
orc = Character("Orc", 100, sword, Armor("Generic Armour", 2))
wiebe = Character("Wiebe", 10000000000, canoe, wiebe_armour)


orc.attack(wiebe)
wiebe.attack(orc)
wiebe.attack(orc)

elif "drop" in command:
item_name = command[0:]
drop_item = None
for item in player.inventory:
    if item_name == item_name:
        drop_item = player.current_location.items

if drop_item is None:
    print("You don't an item in your inventory")