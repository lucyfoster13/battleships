# Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot

from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}

"""
Create a board of 8 rows and 8 columns
"""
def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        #%d for decimal, %s for string
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row] [ship_column] == 'X':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'X'    


#Bug that accepts blank field and crashes
def get_ship_location():
    row = input('Choose a row between 1 and 8 for your ship.')
    #if input is not a number between 1 and 8
    while row not in '12345678':
        print('Please enter a valid row between 1 and 8.')
        #display input message again
        row = input('Choose a row between 1 and 8 for your ship.')
    column = input('Choose a column between A and H for your ship.').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column between A and H.')
        column = input('Choose a column between A and H for your ship.').upper()
    return int(row) -1, letters_to_numbers[column]


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count            

create_ships(HIDDEN_BOARD)
turns = 10
while turns > 0:
    print('Welcome to Battleships!')
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You've already guessed that! Try again.")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Congratulations! You've hit a battleship!")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry, you missed :(')
        GUESS_BOARD[row][column] = '-'
        turns-=1
if count_hit_ships(GUESS_BOARD == 5):
    print("Congratulations! You've sunk all the battleships!")
    break
print("You have " + str(turns) + " remaining turns.")
if turns == 0:
    print("Game Over!")
    break
