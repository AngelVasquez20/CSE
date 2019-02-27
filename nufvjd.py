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


class Boss(object):
    def __init__(self):
        self.health = 100
        self.strength = 100

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
