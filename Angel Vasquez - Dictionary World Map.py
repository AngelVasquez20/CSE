world_map = {
    'R19A': {
        'NAME': "Wiebe's Classroom",
        'DESCRIPTION': "This is the classroom that you are in right "
                       "now. It has two exits to the north side.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The Edison Parking Lot",
        'DESCRIPTION': "There are cars parked here. To "
                       "the south is Mr. Wiebe's room",
        'PATHS': {
            'SOUTH': "R19A"
        }
    }
}

# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['R19A']   # this is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")

    else:
        print("Command not recognized")