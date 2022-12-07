# Oshard Henry

# instructions
def instructions():
    print('Navigate the game and collect items')
    print('To Move Input: go Up, go Down, go Right, go Left')
    print('To Get Item Input: get <item>')


# status update
def status(currentlocat, inventory, itemsavail):
    print('You are at:', currentlocat)
    print(inventory)
    print(itemsavail)


# moving through locations
def room_mov(cur_location, user):
    """uses dictionary to change location"""
    new_loc = lands[cur_location][user]
    return new_loc


def validate(user, new_loc):
    """validates user input"""
    incre = 0
    while True:
        if 'exit' in user:
            print('You have exited the game')
            break
        if (len(user) > 1) and ((user[1]) in directions):
            user = user[1]
            return user
        elif (len(user) == 0) and ((user[0]) in directions):
            print('Invalid Input, Try Again')
            user = input_loop(user, new_loc)
            incre += 1
        elif (user[0] or user[1]) not in directions:
            print('Invalid Input, Try Again')
            user = input_loop(user, new_loc)
            incre += 1


# directions
directions = ['Up', 'Down', 'Right', 'Left']


# room navigation with dictionaries
def main():
    lands = {
        'Grass Lands': {'Left': 'Swamp Lands'},
        'Swamp Lands': {'down': 'Jungle Lands', 'right': 'Grass Lands', 'item': 'Spade'},
        'Jungle Lands': {'up': 'Swamp Lands', 'left': 'The Abyss', 'right': ' Mountain Lands', 'down': 'Check Point',
                         'item': 'Heart'},
        'The Abyss': {'right': 'Jungle Lands'},
        'Mountain Lands': {'left': 'Jungle Lands', 'up': 'Desert Lands', 'item': 'Diamond'},
        'Desert Lands': {'down': 'Mountain Lands', 'item': 'Clubs'},
        'Check Point': {'up': 'Jungle Lands', 'right': 'Stone Lands'},  # create weapon here
        'Stone Lands': {'right': 'Check Point'}  # villain
    }

    # starting point
    current_location = 'Grass Lands'
    inventory = []

    # gameplay loop
    while True:
        
        user_input = input('Enter Directions\n').split()
        user_input = validate(user_input, current_location)

        if user_input == 'exit':
            print('You have exited the game')
            break

        elif current_location == 'Grass Lands':
            if user_input not in directions:
                print('Try Again')
            elif (user_input in directions) and (user_input != 'Left'):
                print('Wrong Turn')
            else:
                current_location = lands[current_location][user_input]
                print(current_location)
                instructions()

        # elif current_location == 'Swamp Lands':
        #     if (user_input == 'North') or (user_input == 'East'):
        #         current_location = room_mov(current_location, user_input)
        #         instruct(current_location)
        #     elif (user_input in directions) and (user_input != 'North' or 'East'):
        #         print('Wrong Turn')
        #         instruct(current_location)
        #     elif user_input not in directions:
        #         print('Try again')
        #
        # elif current_location == 'Cellar':
        #     if user_input not in directions:
        #         print('Try again')
        #     elif user_input in directions and user_input != 'West':
        #         print('Wrong Turn')
        #         instruct(current_location)
        #     else:
        #         current_location = room_mov(current_location, user_input)
        #         instruct(current_location)


main()
