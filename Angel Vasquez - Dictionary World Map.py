world_map = {
    'YOUR_OFFICE': {
        'NAME': "Your Office",
        'DESCRIPTION': "This is the classroom that you are in right "
                       "now. It has two exits to the north side.",
        'PATHS': {
            'SOUTH': "RANDOM_OFFICE",
            'EAST': "CLUE_ROOM"
        }
    },
    'RANDOM_OFFICE': {
        'NAME': "The Sheriff dept's Parking Lot",
        'DESCRIPTION': "There are cars parked here. To "
                       "the north is the Sheriff's office",
        'PATHS': {
            'EAST': "",
            'NORTH': "Sheriff dept"
        }
    },
    'CLUE_ROOM': {
        'NAME': "Great You found a clue. The clue that will be given is to go South 2 times.",
        'DESCRIPTION': "This room is where the clue is hidden.",

        'PATHS': {
            'WEST': "Sheriff dept",
            'SOUTH': ""

        }
    },
    'WEIGHT_ROOM': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }

    },
    'BREAK_ROOM': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'TRAINING_ROOM': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'CLUE_ROOM2': {
        'NAME': "",
        'DESCRIPTION': "",

        "PATHS": {

        }
    },
    'CLUE_ROOM3': {
        'NAME': "",
        'DESCRIPTION': "",

        "PATHS": {

        }
    },
    'BREAK_ROOM2': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'CLUE_ROOM4': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'OFFICE': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'MAIN_OFFICE': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'FRONT_DOOR': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'BACK_DOOR': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'PARKING_LOT': {
        'NAME': "",
        'DESCRIPTION': "",

        'PATHS': {

        }
    },
    'BACK_OFFICE_DOOR':
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
