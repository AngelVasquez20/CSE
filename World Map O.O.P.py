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


Your_office = Room("Your office", "This is your work office", None, "Weight_Room", "Clue_Room", "Co_Worker_office")
Co_Worker_office = Room("Co-worker's office", "This is your co-worker's office", "Your_office", "Break_Room2",
                        "Break_Room", "Clue_Room2", None, None)
Clue_Room = Room("Clue room", "This a clue room", None, "Your_office", None, "Break_Room", None, None)
Weight_Room = Room("Weight room", "This is where the workers workout", None, None, "Your_office", "Break_Room", None,
                   None)
Break_Room = Room("Break Room", "This is where the workers take breaks", "Clue_Room", "Co_Worker_Office", None,
                  "Training_Room", None, None)
Training_Room = Room("training room", "This is where workers do their training", None, "Clue_Room2", None, None, None,
                     None)
Clue_Room2 = Room("Another clue room", "This is where another clue is at", "Co_Worker_office", "Clue_Room3",
                  "Training_Room", "Main_Office", None, None)
Clue_Room3 = Room("third clue room", "This is where the third clue is at", "Break_Room2", None, "Clue_Room2",
                  "Clue_Room4", None, None)
Break_Room2 = Room("Another break room", "This is another room where the workers take brake", "Weight_Room", None,
                   "Co_Worker_office", None, None, None)
Clue_Room4 = Room("4th clue room", "This is where the 4th clue is at", "Clue_Room3", None, "Main_Office", "Office",
                  None, None)
Office = Room("A Office", "This is a random office", "Clue_Room4", None, "Main_Office", None, None, None)
Back_office = Room("Back office", "This is the back of the main office", None, )
Main_Office = Room("Main office", "This is the main office", "Clue_Room2", "Office", "Back_office", "Front_Door")
Front_Door = Room("Front door", "This is the front door either for the entrance or the exit", "Main_Office", None,
                  "Parking_Lot", None)
Parking_Lot = Room("Parking lot", "This is where all the worker's cars are parked at", "Back_office", "Front_Door",
                   None, None)

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

player = Player(Your_office)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
playing = True

# Controller
while playing:
    print(player.current_location.name)
    command = input(">_ ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            next_room = player.find_room(command)
            player.move(next_room)
        except KeyError:
            print("I can't go that way")

    else:
        print("Command not recognized")

