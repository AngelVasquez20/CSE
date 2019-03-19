class Room(object):
    def __init__(self, name, description, north=None, west=None, east=None, south=None, up=None, down=None):
        self.name = name
        self.description = description
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.strength = 100
        self.inventory = []
        self.current_location = starting_location

    def move(self, new_location):
        """This method moves a player to a new location

        :param new_location: The room object that we move to
        :return:
        """
        self.current_location = new_location

    def find_room(self, direction):
        """This method takes a direction, and finds the variable of the room.

        :param direction: A String (all lowercase), with a cardinal direction
        :return: A rom object if it exist, None if it does not
        """
        return getattr(self.current_location, direction)


Your_office = Room("Your office", "This is your work office", None, "Weight_Room", "Clue_Room", "Co_Worker_office",
                   None, None)
Co_Worker_office = Room("Co-worker's office", "This is your co-worker's office", "Your_office", "Break_Room2",
                        "Break_Room", "Clue_Room2", None, None)
Clue_Room = Room("Clue room", "This a clue room (The clue is to go south 2 times.)", None, "Your_office", None,
                 "Break_Room", None, None)
Weight_Room = Room("Weight room", "This is where the workers workout", None, None, "Your_office", "Break_Room", None,
                   None)
Break_Room = Room("Break Room", "This is where the workers take breaks", "Clue_Room", "Co_Worker_Office", None,
                  "Training_Room", None, None)
Training_Room = Room("training room", "This is where workers do their training", None, "Clue_Room2", None, None, None,
                     None)
Clue_Room2 = Room("Another clue room", "This is where another clue is at (Go West)", "Co_Worker_office", "Clue_Room3",
                  "Training_Room", "Main_Office", None, None)
Clue_Room3 = Room("third clue room", "This is where the third clue is at (Go South)", "Break_Room2", None, "Clue_Room2",
                  "Clue_Room4", None, None)
Break_Room2 = Room("Another break room", "This is another room where the workers take brake", "Weight_Room", None,
                   "Co_Worker_office", None, None, None)
Clue_Room4 = Room("Clue room", "Where a clue is at (Go South then go East)", "Clue_Room3", None, "Main_Office",
                  "Office",
                  None, None)
Office = Room("A Office", "This is a random office", "Clue_Room4", None, "Main_Office", None, None, None)
Back_office = Room("Back office", "This is the back of the main office", None, "Main_Office", None, "Parking_Lot",
                   None, None)
Main_Office = Room("Main office", "This is the main office", "Clue_Room2", "Office", "Back_office", "Front_Door",
                   None, None)
Front_Door = Room("Front door", "This is the front door either for the entrance or the exit", "Main_Office", None,
                  "Parking_Lot", None, None, None)
Parking_Lot = Room("Parking lot", "This is where all the worker's cars are parked at", "Back_office", "Front_Door",
                   None, None, None, None)

Your_office.south = Co_Worker_office
Your_office.east = Clue_Room
Your_office.west = Weight_Room
Co_Worker_office.east = Break_Room
Co_Worker_office.south = Clue_Room2
Co_Worker_office.north = Your_office
Co_Worker_office.west = Break_Room2
Clue_Room.west = Your_office
Clue_Room.south = Break_Room
Weight_Room.east = Your_office
Weight_Room.south = Break_Room
Break_Room.south = Training_Room
Break_Room.west = Co_Worker_office
Break_Room.north = Clue_Room
Training_Room.west = Clue_Room2
Clue_Room2.south = Main_Office
Clue_Room2.east = Training_Room
Clue_Room2.west = Clue_Room3
Clue_Room2.north = Co_Worker_office
Clue_Room3.east = Clue_Room2
Clue_Room3.north = Break_Room2
Clue_Room3.south = Clue_Room4
Break_Room2.east = Co_Worker_office
Break_Room2.north = Weight_Room
Clue_Room4.south = Office
Clue_Room4.north = Clue_Room3
Clue_Room4.east = Main_Office
Office.north = Clue_Room4
Office.east = Main_Office
Back_office.south = Parking_Lot
Back_office.west = Main_Office
Main_Office.north = Clue_Room2
Main_Office.west = Office
Main_Office.south = Front_Door
Main_Office.east = Back_office
Front_Door.north = Main_Office
Front_Door.east = Parking_Lot
Parking_Lot.north = Back_office
Parking_Lot.west = Front_Door


# Items
class Item(object):
    def __init__(self, name):
        self.name = name


class Sword(Item):
    def __init__(self, name):
        super(Sword, self).__init__(name)
        self.protection = 40
        self.usage_left = 100

    def swinging(self):
        self.usage_left -= 1
        print("You are swinging the sword")

    def block(self):
        self.protection -= 1
        print("Used the sword as a protection")


class Iron(Sword):
    def __init__(self):
        super(Iron, self).__init__("Iron Sword")


class Steel(Sword):
    def __init__(self):
        super(Steel, self).__init__("Steel Sword")


class Shield(Item):
    def __init__(self, name):
        super(Shield, self).__init__(name)
        self.usage_left = 100
        self.protection = 100

    def use_shield(self):
        self.usage_left -= 1
        print("You use the Shield")


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
        self.bullets = 20

    def shoot(self):
        self.damage = 100
        print("You press the button the taser turns on")


class Tasergun(Taser):
    def __init__(self):
        super(Tasergun, self).__init__("Taser Gun")

    def shoot(self):
        self.bullets -= 1
        print("You push the trigger and the taser shoots you have %s bullets left" % self.bullets)


class Helmet(Item):
    def __init__(self, name):
        super(Helmet, self).__init__(name)
        self.usage_left = 100
        self.protection = 20

    def defend(self):
        self.protection -= 5
        self.usage_left -= 10
        print("You have been it but the helmet helped you you have %s protection left")


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

    def info(self):
        self.damage = 1000
        print("The knife can do 100 damage against an opponent")

    def attack(self):
        self.damage = 100
        print("This knife can do 100 damage against an opponent")
        self.usage_left -= 10
        print("You attacked with the knife you have %s usage left" % self.usage_left)


class SharpK(Knife):
    def __init__(self):
        super(SharpK, self).__init__("Sharp Knife")
        self.damage = 1000
        self.usage_left = 1000

    def info(self):
        self.damage = 1000
        print("The sharp knife can do 1000 damage against an opponent")

    def attack(self):
        self.usage_left -= 10
        print("You attacked with the sharp knife you have %s usage left" % self.usage_left)


class Thin(Knife):
    def __init__(self):
        super(Thin, self).__init__("Thin Knife")
        self.damage = 50
        self.usage_left = 10

    def info(self):
        self.damage = 1000
        print("The sharp knife can do 50 damage against an opponent")

    def attack(self):
        self.usage_left -= 5
        print("You attacked with the tin knife you have %s usage left" % self.usage_left)


class Laptop(Item):
    def __init__(self, name):
        super(Laptop, self).__init__(name)
        self.battery_life = 100

    def use(self):
        self.battery_life -= 10
        print("You have used the laptop your laptop has %s battery left" % self.battery_life)


class AppleLaptop(Laptop):
    def __init__(self):
        super(AppleLaptop, self).__init__("Apple Laptop")

    def use(self):
        self.battery_life -= 10
        print("You have used the laptop your Apple laptop has %s battery left" % self.battery_life)


class Asus(Laptop):
    def __init__(self):
        super(Asus, self).__init__("Asus Laptop")

    def use(self):
        self.battery_life -= 10
        print("You have used the laptop your Asus laptop has %s battery left" % self.battery_life)


class ChestArmor(Item):
    def __init__(self, name):
        super(ChestArmor, self).__init__(name)
        self.usage_left = 100
        self.protection = 60

    def defend(self):
        self.usage_left -= 10
        print("You have used your armor to protect yourself")


class SteelA(ChestArmor):
    def __init__(self):
        super(SteelA, self).__init__("Steel Armour")
        self.protection = 100

    def defend(self):
        self.usage_left -= 10
        print("You have used your steel armor to protect yourself you have %s usage left" % self.usage_left)


class IronA(ChestArmor):
    def __init__(self):
        super(IronA, self).__init__("Iron Armour")
        self.protection = 80

    def defend(self):
        self.usage_left -= 10
        print("You have used your Iron armor to protect yourself you have %s usage left" % self.usage_left)


class Gun(Item):
    def __init__(self, name):
        super(Gun, self).__init__(name)
        self.damage = 100
        self.range = 100
        self.bullets_left = 100

    def info(self):
        self.damage = 100
        self.range = 100
        self.bullets_left = 100
        print("Your gun does 100 damage, 100 range, and 100 bullets")

    def shoot(self):
        self.bullets_left -= 10
        print("You shoot the gun you have %s bullets left" % self.bullets_left)


class Ak47(Gun):
    def __init__(self):
        super(Ak47, self).__init__("Ak47")
        self.range = 1000
        self.damage = 100
        self.bullets_left = 100

    def info(self):
        self.damage = 100
        self.range = 1000
        self.bullets_left = 100
        print("The AK47 does 100 damage, has 1000 range, and has 100 bullets")

    def shoot(self):
        self.bullets_left -= 10
        print("You shoot the AK47, you have %s bullets left" % self.bullets_left)


class Pistol(Gun):
    def __init__(self):
        super(Pistol, self).__init__("Pistol")
        self.range = 100
        self.damage = 50

    def info(self):
        self.damage = 50
        self.range = 100
        self.bullets_left = 100
        print("The Pistol does 50 damage, has 100 range, and has 100 bullets")

    def shoot(self):
        self.bullets_left -= 10
        print("You shoot the Pistol, you have %s bullets left" % self.bullets_left)


class Sniper(Gun):
    def __init__(self):
        super(Sniper, self).__init__("Sniper")
        self.range = 10000
        self.damage = 1000

    def info(self):
        self.damage = 1000
        self.range = 10000
        self.bullets_left = 100
        print("The Sniper does 1000 damage, has 10000 range, and has 100 bullets")

    def shoot(self):
        self.bullets_left -= 10
        print("You shoot the Sniper, you have %s bullets left" % self.bullets_left)


class Clothes(Item):
    def __init__(self, name):
        super(Clothes, self).__init__(name)
        self.protection = 3

    def info(self):
        self.protection = 3
        print("Your clothes has 1 protection")


class Pants(Clothes):
    def __init__(self):
        super(Pants, self).__init__("Pants")

    def info(self):
        print("Pants has 3 protection")


class Shirt(Clothes):
    def __init__(self):
        super(Shirt, self).__init__("Shirt")

    def info(self):
        print("Pants has 3 protection")


class Sweater(Clothes):
    def __init__(self):
        super(Sweater, self).__init__("Sweater")

    def info(self):
        print("Pants has 3 protection")


class Socks(Clothes):
    def __init__(self):
        super(Socks, self).__init__("Socks")

    def info(self):
        print("Pants has 3 protection")


class Potion(Item):
    def __init__(self, name):
        super(Potion, self).__init__(name)
        self.protection = 50
        self.damage = 50
        self.usage_left = 100
        self.life = 50
        self.power = 50

    def drink(self):
        self.usage_left -= 1
        self.life += 1
        print("You take the potion and you have %s life now and %d is how much is left" % (self.life,
                                                                                           self.usage_left))


class LifeP(Potion):
    def __init__(self):
        super(LifeP, self).__init__("Life Potion")

    def drink(self):
        self.usage_left -= 1
        self.life += 1
        print("You take the life potion and you have %s life now and %d is how much is left" % (self.life,
                                                                                                self.usage_left))


class Power(Potion):
    def __init__(self):
        super(Power, self).__init__("Power Potion")

    def drink(self):
        self.usage_left -= 1
        self.power += 1
        print("You take the power potion and you have %s life now and %d is how much is left" % (self.power,
                                                                                                 self.usage_left))


class Food(Item):
    def __init__(self, name):
        super(Food, self).__init__(name)
        self.food_left = 100
        self.damage = 100
        self.life = 100

    def eat(self):
        self.food_left -= 10
        self.life += 1
        print("You eat and have %s life now and has %d food left" % (self.food_left, self.life))


class Chicken(Food):
    def __init__(self):
        super(Chicken, self).__init__("Chicken")

    def eat(self):
        self.food_left -= 10
        self.life += 1
        print("You eat Chicken and have %s life now and has %d food left" % (self.food_left, self.life))


class Pork(Food):
    def __init__(self):
        super(Pork, self).__init__("Pork")

    def eat(self):
        self.food_left -= 10
        self.life += 1
        print("You eat Pork and have %s life now and has %d food left" % (self.food_left, self.life))


class Eggs(Food):
    def __init__(self):
        super(Eggs, self).__init__("Eggs")

    def eat(self):
        self.food_left -= 10
        self.life += 1
        print("You eat Eggs and have %s life now and has %d food left" % (self.food_left, self.life))


class Boots(Item):
    def __init__(self, name):
        super(Boots, self).__init__(name)
        self.protection = 50
        self.usage_left = 100

    def walk(self):
        self.usage_left -= 1
        print("You walk and have %s usage left on your boots" % self.usage_left)


class LeatherB(Boots):
    def __init__(self):
        super(LeatherB, self).__init__("Leather Boots")
        self.protection = 100
        self.usage_left = 1000

    def walk(self):
        self.usage_left -= 1
        print("You walk and have %s usage left on your leather boots" % self.usage_left)


class Pills(Item):
    def __init__(self, name):
        super(Pills, self).__init__(name)
        self.damage = 50
        self.life = 20
        self.usage_left = 10

    def take(self):
        self.life += 1
        self.usage_left -= 1
        print("You tak the pil and have %s life added to you and have %d pills left" % (self.life, self.usage_left))


class Energy(Pills):
    def __init__(self):
        super(Energy, self).__init__("Energy Pills")
        self.energy = 100
        self.usage_left = 5

    def take(self):
        self.energy += 1
        self.usage_left -= 1
        print("You tak the power pill and have %s power added to you and have %d pills left" %
              (self.energy, self.usage_left))


class Strength(Pills):
    def __init__(self):
        super(Strength, self).__init__("Strength Pills")
        self.strength = 100
        self.usage_left = 5

    def take(self):
        self.strength += 1
        self.usage_left -= 1
        print("You tak the strength pill and have %s power added to you and have %d pills left" %
              (self.strength, self.usage_left))


class Axe(Item):
    def __init__(self, name):
        super(Axe, self).__init__(name)
        self.damage = 80
        self.usage_left = 100

    def attack(self):
        self.usage_left -= 10
        print("You attacked with the axe and have %s usage left" % self.usage_left)


class Ironaxe(Axe):
    def __init__(self):
        super(Ironaxe, self).__init__("Steel Axe")
        self.damage = 90
        self.usage_left = 1000

    def attack(self):
        self.usage_left -= 10
        print("You attacked with the iron axe and have %s usage left" % self.usage_left)


class Steelaxe(Axe):
    def __init__(self):
        super(Steelaxe, self).__init__("Steel Axe")
        self.damage = 100
        self.usage_left = 10000

    def attack(self):
        self.usage_left -= 10
        print("You attacked with the steel axe and have %s usage left" % self.usage_left)


class Water(Item):
    def __init__(self, name):
        super(Water, self).__init__(name)
        self.health = 10
        self.strength = 10
        self.water_left = 100

    def drink(self):
        self.health += 5
        self.strength += 5
        self.water_left -= 10
        print("You have drink the water you have %s health added, %s strength added and you have %s water left" %
              (self.health, self.strength, self.water_left))


class Cold(Water):
    def __init__(self):
        super(Cold, self).__init__("Cold Water")
        self.health = 10
        self.strength = 10
        self.water_left = 100

    def drink(self):
        self.health += 10
        self.strength += 10
        self.water_left -= 10
        print("You have drink the water you have %s health added, %s strength added and you have %s water left" %
              (self.health, self.strength, self.water_left))


class Hot(Water):
    def __init__(self):
        super(Hot, self).__init__("Hot Water")
        self.health = 10
        self.strength = 10
        self.usage_left = 100

    def drink(self):
        self.health += 4
        self.strength += 4
        self.water_left -= 10
        print("You have drink the water you have %s health added, %s strength added and you have %s water left" %
              (self.health, self.strength, self.water_left))


# Rooms
world_map = {
    'YOUR_OFFICE': {
        'NAME': "Your Office",
        'DESCRIPTION': "This is Your work office",
        'PATHS': {
            'SOUTH': "CO_WORKER_OFFICE",
            'EAST': "CLUE_ROOM",
            'WEST': "WEIGHT_ROOM",
        }
    },
    'CO_WORKER_OFFICE': {
        'NAME': "co-worker's office",
        'DESCRIPTION': "This is your co-worker's office",
        'PATHS': {
            'EAST': "BREAK_ROOM",
            'NORTH': "YOUR_OFFICE",
            'WEST': "BREAK_ROOM2",
            'SOUTH': "CLUE_ROOM2"
        }
    },
    'CLUE_ROOM': {
        'NAME': "Great You found a clue. The clue that will be given is to go South 2 times,"
                "and then you choose where to go.",
        'DESCRIPTION': "This room is where the clue is hidden.",

        'PATHS': {
            'WEST': "YOUR_OFFICE",
            'SOUTH': "BREAK_ROOM"

        }
    },
    'WEIGHT_ROOM': {
        'NAME': "Weight room",
        'DESCRIPTION': "This is thw eight room where the sheriff's cary weights.",

        'PATHS': {
            'EAST': "YOUR_OFFICE",
            'SOUTH': "BREAK_ROOM"
        }

    },
    'BREAK_ROOM': {
        'NAME': "Break room",
        'DESCRIPTION': "This is where you and your co-workers take breaks.",

        'PATHS': {
            'SOUTH': "TRAINING_ROOM",
            'WEST': "CO_WORKER_OFFICE",
            'NORTH': "CLUE_ROOM"
        }
    },
    'TRAINING_ROOM': {
        'NAME': "Training room",
        'DESCRIPTION': "This is where you or other sheriff's train",

        'PATHS': {
            'WEST': "CLUE_ROOM2"
        }
    },
    'CLUE_ROOM2': {
        'NAME': "Great you found a clue, you can go west and you will find another clue.",
        'DESCRIPTION': "",

        "PATHS": {
            'SOUTH': "MAIN_OFFICE",
            'NORTH': "CO_WORKER_OFFICE",
            'WEST': "CLUE_ROOM3",
            'EAST': "TRAINING_ROOM"
        }
    },
    'CLUE_ROOM3': {
        'NAME': "Another clue is to go South then you will find another clue",
        'DESCRIPTION': "This is clue 3 do south and you will find another clue",

        "PATHS": {
            'EAST': "CLUE_ROOM2",
            'NORTH': "BREAK_ROOM2",
            'SOUTH': "CLUE_ROOM4"
        }
    },
    'BREAK_ROOM2': {
        'NAME': "Second Break room",
        'DESCRIPTION': "This is the second brake room",

        'PATHS': {
            'EAST': "CO_WORKER_OFFICE",
            'NORTH': "WEIGHT_ROOM"
        }
    },
    'CLUE_ROOM4': {
        'NAME': "You found the clue, now you will go South then go East.",
        'DESCRIPTION': "",

        'PATHS': {
            'SOUTH': "OFFICE",
            'NORTH': "CLUE_ROOM3",
            'EAST': "MAIN_OFFICE"
        }
    },
    'OFFICE': {
        'NAME': "An office",
        'DESCRIPTION': "This is a random office",

        'PATHS': {
            'NORTH': "CLUE_ROOM4",
            'EAST': "MAIN_OFFICE"
        }
    },
    'BACK_OFFICE': {
        'NAME': "Back Office",
        'DESCRIPTION': "",

        'PATHS': {
            'SOUTH': "PARKING_LOT",
            'WEST': "MAIN_OFFICE"
        }
    },
    'MAIN_OFFICE': {
        'NAME': "Main office",
        'DESCRIPTION': "",

        'PATHS': {
            'NORTH': "CLUE_ROOM2",
            'WEST': "OFFICE",
            'SOUTH': "FRONT_DOOR",
            'EAST': "BACK_OFFICE"
        }
    },
    'FRONT_DOOR': {
        'NAME': "Front door",
        'DESCRIPTION': "",

        'PATHS': {
            'NORTH': "MAIN_OFFICE",
            'EAST': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "You found the parking lot",
        'DESCRIPTION': "",

        'PATHS': {
            'NORTH': "BACK_OFFICE",
            'WEST': "FRONT_DOOR"
        }
    }
}


# Characters
class Boss(object):
    def __init__(self):
        self.health = 100
        self.strength = 1000


player = Player(Your_office)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_ ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            if next_room is None:
                raise KeyError
            player.move(next_room)
        except KeyError:
            print("I can't go that way")

    else:
        print("Command not recognized")
