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


# room navigation with dictionaries
def main():
    lands = {
        'Grass Lands': {'right': 'Swamp Lands'},
        'Swamp Lands': {'down': 'Jungle Lands', 'right': 'Grass Lands', 'item': 'King of Spades'},
        'Jungle Lands': {'up': 'Swamp Lands', 'left': 'The Abyss', 'right': ' Mountain Lands', 'down': 'Check Point'},
        'The Abyss': {'right': 'Jungle Lands'},
        'Mountain Lands': {'left': 'Jungle Lands', 'up': 'Desert Lands'},
        'Desert Lands': {'down': 'Mountain Lands'},
        'Check Point': {'up': 'Jungle Lands', 'right': 'Stone Lands'},
        'Stone Lands': {'right': 'Check Point'}
    }


# directions
directions = ['Up', 'Down', 'Right', 'Left']

# starting point
current_location = 'Grass Lands'
inventory = []

# gameplay loop
while True:
    user_input = input('Enter Directions\n').split()
    user_input = validate(user_input, current_location)
