#Austin Wilson

def show_instructions():
    items = [] # Initilization of list for items collected during game playthrough
    current_room = 'Your Mothers Basement'  # Starting room
    print('Moves: North, East, South, West, Search')  # Game directions
    print('Type exit at any point to leave the game')
    return current_room, items

def update_status(current_room, items):
    print('You are in', current_room)  # Tells player what room they are in
    print("You have acquired these items:") # Tells player what items they have acquired
    for i in range(0, len(items)):
        print(items[i] + ',' , '', end='')
    print('')

def move_and_acquire_items(rooms, current_room, items):
    move = input('What is your move?')  # Reads in player move
    if move == 'exit':  # Sets current_room to 'exit' so the loop will end if move is equal to 'exit'
        current_room = 'exit'
    elif move in rooms[current_room]:  # Checks if the move is in the nested dictionary
        if move == 'Search' and not rooms[current_room][move] in items: # If the move is search and the item being searched is not currently in the items list it is added to the list
            items.append(rooms[current_room][move])
            print('Found', rooms[current_room][move] + '!')
        elif move == 'North' or move == 'East' or move == 'South' or move == 'West': # If the move is any of the cardinal directions the room changes to its appropriate neighboring room
            current_room = rooms[current_room][move]
            print('You went to', current_room)
        else: # If the move is somehow part of the nested dictionary but does not meet the previous if statement qualifications its declared an invalid move
            print('Invalid move')
    else:
        if move == 'North' or move == 'East' or move == 'South' or move == 'West':  # If you try to go the wrong direction it tells you that you cant go that way
            print('You cant go that direction')
        else:
            print('Invalid move')  # Any other invalid moves are stated as such
    return current_room, items

def game_over(current_room, items):
    if len(items) == 10: # Win condition, if you collect all items
        print('You have gathered all ingredients necessary to make the ultimate sandwich')
        print('Your sandwich has become deified and vaporized PETA with a mere thought')
        print('You Win!')
    elif current_room == 'PETA Headquarters': # Lose condition, if you enter PETAs Headquarters before collecting all items
        print('Oh no! PETA has caught you!')
        print('They are going to put you down and make you into a stylist leather coat and hat')
        print('You lost')
    exit()  # Ends the game

rooms = { #Room dictionary
    'Cow Pasture': {
        'South': 'Neighborhood Walmarket',
        'Search': 'Ribeye Steak'
    },
    'PETA Headquarters': {
        'South': 'Mega Walmarket'
    },
    'Maxi Walmarket': {
        'South': 'Your Mothers Basement',
        'Search': 'Mustard'
    },
    'Neighborhood Walmarket': {
        'North': 'Cow Pasture',
        'East': 'Butcher Shop',
        'South': 'Super Walmarket',
        'Search': 'Swiss Cheese'
    },
    'Butcher Shop': {
        'West': 'Neighborhood Walmarket',
        'Search': 'Salami'
    },
    'Mega Walmarket': {
        'North': 'PETA Headquarters',
        'East': 'Your Mothers Basement',
        'Search': 'Gouda Cheese'
    },
    'Your Mothers Basement': {
        'North': 'Maxi Walmarket',
        'East': 'Super Walmarket',
        'South': 'Lamb Pasture',
        'West': 'Mega Walmarket'
    },
    'Super Walmarket': {
        'North': 'Neighborhood Walmarket',
        'West': 'Your Mothers Basement',
        'Search': 'Provolone Cheese'
    },
    'Pig Pen': {
        'East': 'Lamb Pasture',
        'Search': 'Bacon'
    },
    'Lamb Pasture': {
        'North': 'Your Mothers Basement',
        'South': 'Local Walmarket Competitor',
        'West': 'Pig Pen',
        'Search': 'Sliced Lamb Leg'
    },
    'Local Walmarket Competitor': {
        'North': 'Lamb Pasture',
        'East': 'Baby Cow Pen',
        'Search': 'Pickles'
    },
    'Baby Cow Pen': {
        'West': 'Local Walmarket Competitor',
        'Search': 'Veal Cutlets'
    }
}

current_room, items = show_instructions() #Shows initial game instructions

while (current_room != 'exit') and (len(items) != 10) and (current_room != 'PETA Headquarters'): #Loops continuously as long as player does not type exit, collect all items, or enter PETAs Headquarters
    update_status(current_room, items) # Updates the players status, ie what room they are in and what items they have collected
    current_room, items = move_and_acquire_items(rooms, current_room, items) # Changes the room the player is in and what items they have collected

game_over(current_room, items) # End game situations