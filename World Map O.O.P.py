class Room(object):
    def __init__(self, name, north=None, west=None, east=None, south=None, up=None, down=None):
        self.name = name
        self.north = north
        self.west = west
        self.east = east
        self.south = south
        self.up = up
        self.down = down


Your_office = Room("Your office", "This is your work office")
Co_Worker_office = Room("Co-worker's office", "This is your co-worker's office")
Clue_Room = Room("Clue room", "This a clue room")
Weight_Room = Room("Weight room", "This is where the workers workout")
Break_Room = Room("Break Room", "This is where the workers take breaks")
Training_Room = Room("training room", "This is where workers do their training")
Clue_Room2 = Room("Another clue room", "This is where another clue is at")
Clue_Room3 = Room("third clue room", "This is where the third clue is at")
Break_Room2 = Room("Another break room", "This is another room where the workers take brakes")
Clue_Room4 = Room("4th clue room", "This is where the 4th clue is at")
Office = Room("A Office", "This is a random office")
Back_office = Room("Back office", "This is the back of the main office")
Main_Office = Room("Main office", "This is the main office")
Front_Door = Room("Front door", "This is the front door either for the entrance or the exit")
Parking_Lot = Room("Parking lot", "This is where all the worker's cars are parked at")

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
Break_Room.south = 
Break_Room.west =
Break_Room.north =
Training_Room.west =
Clue_Room2.south =
Clue_Room2.east =
Clue_Room2.west =
Clue_Room2.north =
Clue_Room3.east
Clue_Room3.north
Clue_Room3.south







