# instructions
def instructions():
    print('Navigate the game and collect items')
    print('To Move Input: go Up, go Down, go Right, go Left')
    print("To Get Item Input: get 'item'")
    print('--------------------------')


# status update
def status(currentlocat, inventory, itemsavail):
    if itemsavail == 0:
        print('You are at:', currentlocat)
        print('Inventory:', inventory)
    else:
        print('You are at:', currentlocat)
        print('You see a', itemsavail)
        print('Inventory:', inventory)


def input_loop(user):
    """nested in validate function to continuously
    ask for input from user"""
    while (user != 'go') or (user == directions):
        users = input(">>ENTER COMMAND<<\n").split()
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
        'Swamp Lands': {'Down': 'Jungle Lands', 'Right': 'Grass Lands', 'item': 'Spade'},
        'Jungle Lands': {'Up': 'Swamp Lands', 'Left': 'The Abyss', 'right': ' Mountain Lands', 'Down': 'Check Point',
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
        user_input = input('>>ENTER COMMAND<<\n').split(' ')
        user_input = validate(user_input)
        print('---------------------')

        if current_location == 'Grass Lands':
            if user_input == 'Left':
                current_location = lands[current_location][user_input]
                itemsavail = lands[current_location]['item']
                status(current_location, inventory, itemsavail)
                print('----------------------')
            else:
                print('Wrong turn, Try again')

        # work on feature to pick up items

        elif current_location == 'Swamp Lands':
            if user_input == 'Down':
                current_location = lands[current_location][user_input]
                itemsavail = lands[current_location]['item']
                status(current_location, inventory, itemsavail)
                print('----------------------')
            if user_input == 'Spade':
                inventory.append(itemsavail)
                status(current_location, inventory, itemsavail=0)
                print('----------------------')

            elif user_input == 'Right':
                current_location = lands[current_location][user_input]
                status(current_location, inventory, itemsavail=0)
                print('----------------------')

        elif current_location == 'Jungle Lands':
            if user_input == 'Up' or user_input == 'Right':
                current_location = lands[current_location][user_input]
                itemsavail = lands[current_location]['item']
                status(current_location, inventory, itemsavail)
                print('----------------------')

            if user_input == 'Heart':
                inventory.append(itemsavail)
                status(current_location, inventory, itemsavail=0)
                print('----------------------')

            elif user_input == 'Left':
                status(current_location, inventory, itemsavail=0)
                print('GAME OVER')
                break
            elif user_input == 'Down':
                current_location = lands[current_location][user_input]
                status(current_location, inventory, itemsavail=0)
                if len(inventory) < 4:
                    print('!WARNING! WARNING!')
                    print('If you dont have all four')
                    print('items collect them first')
                    print('before proceeding')
                    print('----------------------')
                else:
                    continue

        # PICK UP ITEMS


main()
