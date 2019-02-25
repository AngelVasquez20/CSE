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


# Other Variables
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map['YOUR_OFFICE']   # this is your current location
playing = True

# Controller
while playing:
    print(current_node['NAME'])
    command = input(">_ ")
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
