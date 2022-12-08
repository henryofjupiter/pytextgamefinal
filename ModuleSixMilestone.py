# instructions
def instructions():
    print('Navigate the game and collect items')
    print('To Move Input: go Up, go Down, go Right, go Left')
    print("To Get Item Input: get 'item'")
    print('--------------------------')


# status update
def status(currentlocat, inventory, itemsavail):
    print('You are at:', currentlocat)
    print('You see a', itemsavail)
    print('Inventory:', inventory)


# moving through locations
# def room_mov(cur_location, user):
#     """uses dictionary to change location"""
#     new_loc = lands[cur_location][user]
#     return new_loc


def input_loop(user):
    """nested in validate function to continuously
    ask for input from user"""
    while (user != 'go') or (user == directions):
        users = input(">Enter Command\n").split()
        return users


def validate(user):
    """validates user input"""
    incre = 0
    while True:
        if 'exit' in user:
            print('You have exited the game')
            break
        if len(user) > 1:
            if (user[0]) == 'go' and (user[1]) in directions:
                users = user[1]
                return users
            if (user[0]) == 'get' and (user[1]) in itemsGame:
                users = user[1]
                return users
        elif (len(user) == 0) and ((user[0]) in directions):
            print('Invalid Input, Try Again')
            user = input_loop(user)
            incre += 1
        elif (user[0] or user[1]) not in directions:
            print('Invalid Input, Try Again')
            user = input_loop(user)
            incre += 1
        else:
            print('Invalid Input, Try Again')
            user = input_loop(user)


# directions
directions = ['Up', 'Down', 'Right', 'Left']
itemsGame = ['Spade', 'Heart', 'Diamond', 'Clubs']


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

    instructions()

    # starting point
    current_location = 'Grass Lands'
    inventory = []

    # gameplay loop
    while True:
        user_input = input('>Enter Command\n').split(' ')
        user_input = validate(user_input)

        if current_location == 'Grass Lands':
            if user_input == 'Left':
                current_location = lands[current_location][user_input]
                itemsavail = lands[current_location]['item']
                status(current_location, inventory, itemsavail)
                print('----------------------')
            else:
                print('Wrong turn, Try again')

        # work on feature to pick up items

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
