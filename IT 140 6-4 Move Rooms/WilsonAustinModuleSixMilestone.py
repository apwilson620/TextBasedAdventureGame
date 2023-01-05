#Austin Wilson

rooms = { #Room dictionary
    'Cow Pasture': {
        'South': 'Neighborhood Walmarket'
    },
    'PETA Headquarters': {
        'South': 'Mega Walmarket'
    },
    'Maxi Walmarket': {
        'South': 'Your Mothers Basement'
    },
    'Neighborhood Walmarket': {
        'North': 'Cow Pasture',
        'East': 'Butcher Shop',
        'South': 'Super Walmarket'
    },
    'Butcher Shop': {
        'West': 'Neighborhood Walmarket'
    },
    'Mega Walmarket': {
        'North': 'PETA Headquarters',
        'East': 'Your Mothers Basement'
    },
    'Your Mothers Basement': {
        'North': 'Maxi Walmarket',
        'East': 'Super Walmarket',
        'South': 'Lamb Pasture',
        'West': 'Mega Walmarket'
    },
    'Super Walmarket': {
        'North': 'Neighborhood Walmarket',
        'West': 'Your Mothers Basement'
    },
    'Pig Pen': {
        'East': 'Lamb Pasture'
    },
    'Lamb Pasture': {
        'North': 'Your Mothers Basement',
        'South': 'Local Walmarket Competitor',
        'West': 'Pig Pen'
    },
    'Local Walmarket Competitor': {
        'North': 'Lamb Pasture',
        'East': 'Baby Cow Pen'
    },
    'Baby Cow Pen': {
        'West': 'Local Walmarket Competitor'
    }
}

current_room = 'Your Mothers Basement' #Starting room
print('Moves: North, East, South, West') #Game directions
print('Type exit at any point to leave the game')

while current_room != 'exit': #Loops continuously as long as player does not type exit
    print('You are in', current_room) #Tells player what room they are in
    move = input('What is your move?') #Reads in player move
    if move == 'exit': #Sets current_room to 'exit' so the loop will end if move is equal to 'exit'
        current_room = 'exit'
    elif move in rooms[current_room]: #Checks if the move is in the nested dictionary, if it is it assigns current_room as the nested dictionary key
        current_room = rooms[current_room][move]
        print('You went to', current_room)
    else:
        if move == 'North' or move == 'East' or move == 'South' or move == 'West': #If you try to go the wrong direction it tells you that you cant go that way
            print('You cant go that direction')
        else:
            print('Invalid move') #Any other invalid moves are stated as such

exit() #Ends the game