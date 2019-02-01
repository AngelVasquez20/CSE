world_map = {
    'Sheriff dept': {
        'NAME': "sheriff's office (Safe House)",
        'DESCRIPTION': "This is the classroom that you are in right "
                       "now. It has two exits to the north side.",
        'PATHS': {
            'SOUTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The Sheriff dept's Parking Lot",
        'DESCRIPTION': "There are cars parked here. To "
                       "the north is the Sheriff's office",
        'PATHS': {
            'NORTH': "Sheriff dept"
        }
    }
}


# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['Sheriff dept']   # this is your current location
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
