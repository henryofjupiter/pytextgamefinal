# Oshard Henry

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
    elif itemsavail not in itemsGame:
        print('You are at:', currentlocat)
        print(itemsavail)
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


def fuse_items(inventory):
    if (len(inventory)) == 4:
        print('press "F" to fuse items')
        incre = 0
        while True:
            user = input('>>ENTER COMMAND<<\n')
            incre += 1
            if user == 'F':
                user = 'x------>'
                return user
            elif user != 'F':
                continue


def validate(user):
    """validates user input"""
    incre = 0
    while True:
        if 'exit' in user:
            print('You have exited the game')
            return user
        elif len(user) > 1:
            if (user[0]) == 'go' and (user[1]) in directions:
                users = user[1]
                return users
            if (user[0]) == 'get' and (user[1]) in itemsGame:
                users = user[1]
                return users
            if (user[0]) != 'go':
                print('Invalid Input, Try Again')
                user = input_loop(user)
            else:
                print('Invalid Input, Try Again')
                user = input_loop(user)
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
        'Jungle Lands': {'Up': 'Swamp Lands', 'Left': 'The Abyss', 'Right': 'Mountain Lands', 'Down': 'Check Point',
                         'item': 'Heart'},
        'The Abyss': {'Right': 'Jungle Lands'},
        'Mountain Lands': {'Left': 'Jungle Lands', 'Up': 'Desert Lands', 'item': 'Diamond'},
        'Desert Lands': {'Down': 'Mountain Lands', 'item': 'Clubs'},
        'Check Point': {'Up': 'Jungle Lands', 'Right': 'Stone Lands'},  # create weapon here
        'Stone Lands': {'Left': 'Check Point'}  # villain
    }

    instructions()

    # starting point
    current_location = 'Grass Lands'
    inventory = []
    weapon = ''

    # gameplay loop
    while True:
        user_input = input('>>ENTER COMMAND<<\n').split()
        # print(user_input)
        user_input = validate(user_input)
        print('---------------------')

        if 'exit' in user_input:
            break

        if current_location == 'Grass Lands':
            if user_input == 'Left':
                current_location = lands[current_location][user_input]
                itemsavail = lands[current_location]['item']
                status(current_location, inventory, itemsavail)
                print('----------------------')
            else:
                print('Wrong turn, Try again')

        elif current_location == 'Swamp Lands':
            if user_input in directions:
                if (user_input == 'Down') or (user_input == 'Right'):
                    if user_input == 'Down':
                        # jungle lands
                        current_location = lands[current_location][user_input]
                        itemsavail = lands[current_location]['item']
                        status(current_location, inventory, itemsavail)
                        print('----------------------')
                    elif user_input == 'Right':
                        # grass lands
                        current_location = lands[current_location][user_input]
                        status(current_location, inventory, itemsavail=0)
                        print('----------------------')
                else:
                    print('Wrong Turn')
            elif user_input == itemsavail:
                inventory.append(itemsavail)
                lands[current_location]['item'] = 'no item here'
                status(current_location, inventory, itemsavail=0)
                print('----------------------')

        elif current_location == 'Jungle Lands':
            if user_input in directions:
                if (user_input == 'Up') or (user_input == 'Right'):
                    current_location = lands[current_location][user_input]
                    itemsavail = lands[current_location]['item']
                    status(current_location, inventory, itemsavail)
                    print('----------------------')
                if (user_input == 'Left') or (user_input == 'Down'):
                    if user_input == 'Left':
                        current_location = lands[current_location][user_input]
                        status(current_location, inventory, itemsavail=0)
                        print('You have entered', current_location)
                        print('>>>GAME OVER<<<')
                        break
                    elif user_input == 'Down':
                        current_location = lands[current_location][user_input]
                        status(current_location, inventory, itemsavail=0)
                        if len(inventory) < 4:
                            print('!WARNING! !WARNING!')
                            print('If you dont have all four')
                            print('items collect them first')
                            print('before proceeding')
                            print('----------------------')
                        elif len(inventory) == 4:
                            weapon = fuse_items(inventory)
                            print('Items Fused Into Weapon')

            elif user_input == itemsavail:
                inventory.append(itemsavail)
                lands[current_location]['item'] = 'no item here'
                status(current_location, inventory, itemsavail=0)
                print('----------------------')

        elif current_location == 'Mountain Lands':
            if user_input in directions:
                if (user_input == 'Up') or (user_input == 'Left'):
                    if user_input == 'Up':
                        current_location = lands[current_location][user_input]
                        itemsavail = lands[current_location]['item']
                        status(current_location, inventory, itemsavail)
                        print('----------------------')
                    elif user_input == 'Left':
                        current_location = lands[current_location][user_input]
                        itemsavail = lands[current_location]['item']
                        status(current_location, inventory, itemsavail)
                        print('----------------------')
                else:
                    print('Wrong turn, Try again')

            if user_input == itemsavail:
                inventory.append(itemsavail)
                lands[current_location]['item'] = 'no item here'
                status(current_location, inventory, itemsavail=0)

        elif current_location == 'Desert Lands':
            if user_input in directions:
                if user_input == 'Down':
                    current_location = lands[current_location][user_input]
                    itemsavail = lands[current_location]['item']
                    status(current_location, inventory, itemsavail)
                    print('----------------------')
                else:
                    print('Wrong turn, Try again')

            if user_input == itemsavail:
                inventory.append(itemsavail)
                lands[current_location]['item'] = 'no item here'
                status(current_location, inventory, itemsavail=0)

        elif current_location == 'Check Point':
            if user_input in directions:
                if (user_input == 'Right') or (user_input == 'Up'):
                    if user_input == 'Right':
                        current_location = lands[current_location][user_input]
                        status(current_location, inventory=0, itemsavail=0)
                        print('Weapon:', weapon)

                        if len(weapon) < 8:
                            print('He kills you')
                            print('GAME OVER')
                            break
                        if len(weapon) == 8:
                            print('You see Hisoka and defeated him')
                            print()
                            print('YOU WON')
                            print('Thanks For Playing')
                            break

                    elif user_input == 'Up':
                        current_location = lands[current_location][user_input]
                        itemsavail = lands[current_location]['item']
                        status(current_location, inventory, itemsavail)
                        print('----------------------')
                else:
                    print('Wrong turn, Try again')


main()
