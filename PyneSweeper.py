from enum import Enum 
from random import randrange

DEFAULT_BOARD_HEIGHT = 5
DEFAULT_BOARD_WIDTH = 5

mine_locations = []
internalBoard = [[None for i in range(DEFAULT_BOARD_WIDTH)] for i in range(DEFAULT_BOARD_HEIGHT)]
displayBoard = [[None for i in range(DEFAULT_BOARD_WIDTH)] for i in range(DEFAULT_BOARD_HEIGHT)]

def genMinePositions(width, height):
    for x in range(width):
        for y in range(height):
            if randrange(10) < 3:
                internalBoard[x][y] = 'X'
            else:
                internalBoard[x][y] = '_'

def genMineCounters(width = DEFAULT_BOARD_WIDTH, height = DEFAULT_BOARD_HEIGHT):
    # iterate through internalBoard
    # count cells around curCell to determine counter value at curCell
    for x in range(width):
        for y in range(height):
            # determine which case curCell is in: top edge, left side, right side, bottom, or middle
            if internalBoard[x][y] == '_':
                # check for adjacent mines
                count = 0
                if x - 1 >= 0 and internalBoard[x - 1][y] == 'X':
                    count += 1
                if x + 1 < width and internalBoard[x + 1][y] == 'X':
                    count += 1
                if y - 1 >= 0 and internalBoard[x][y - 1] == 'X':
                    count += 1
                if y + 1 < height and internalBoard[x][y + 1] == 'X':
                    count += 1
                if x - 1 >= 0 and y - 1 >= 0 and internalBoard[x - 1][y - 1] == 'X':
                    count += 1
                if x - 1 >= 0 and y + 1 < height and internalBoard[x - 1][y + 1] == 'X':
                    count += 1
                if x + 1 < width and y - 1 >= 0 and internalBoard[x + 1][y - 1] == 'X':
                    count += 1
                if x + 1 < width and y + 1 < height and internalBoard[x + 1][y + 1] == 'X':
                    count += 1

                internalBoard[x][y] = count

def initInternalBoard(width = DEFAULT_BOARD_WIDTH, height = DEFAULT_BOARD_HEIGHT):
    # assume random mine placement for now
    # generate mine placements on internalBoard
    # generate mine counters on internalBoard
    # 
    genMinePositions(width, height)
    genMineCounters(width, height)

def initDisplayBoard(width = DEFAULT_BOARD_WIDTH, height = DEFAULT_BOARD_HEIGHT):
    for x in range(width):
        for y in range(height):
            displayBoard[x][y] = '_'

def renderInternalBoard(): #for testing
    print()
    for row in internalBoard:
        print(row)
    print()

def displayStartInfo():
    print('Enter position in (x, y) format with u for uncover or f for flag, as in: 2 3 u or: 3 9 f')

def renderDisplayBoard():
    print() #to keep space above board
    for row in displayBoard:
        print(row)
    print() #to leave space below board

# @return (pos_x, pos_y, action)
# NEED to validate input here
def handleInput():
    user_input = input('Make your move...').split(' ')
    return (int(user_input[0]), int(user_input[1]), user_input[2])

# @input (pos_x, pos_y, action)
# once validation is implemented we can assume input is valid when this is called
def updateDisplayBoard(user_input):
    pos_x = user_input[0]
    pos_y = user_input[1]
    action = user_input[2]
    if action == 'u':
        displayBoard[pos_y][pos_x] = internalBoard[pos_y][pos_x]
    else:
        displayBoard[pos_y][pos_x] = 'F'

def checkForLoss():
    for x in range(DEFAULT_BOARD_WIDTH):
        for y in range(DEFAULT_BOARD_HEIGHT):
            if displayBoard[x][y] == 'X':
                return True
    return False

def checkForWin(): #need to revise this to account for case where player puts 'F' everywhere, which should not win
    for x in range(DEFAULT_BOARD_WIDTH):
        for y in range(DEFAULT_BOARD_HEIGHT):
            if internalBoard[x][y] == 'X' and displayBoard[x][y] != 'F':
                return False
    return True

def runGame():
    initInternalBoard()
    initDisplayBoard()
    renderDisplayBoard()
    displayStartInfo()
    while True:
        input = handleInput()
        updateDisplayBoard(input)
        if checkForLoss():
            renderDisplayBoard()
            print('You Lost :(')
            break
        if checkForWin():
            renderDisplayBoard()
            print('You win!  :D')
            break
        renderDisplayBoard()

if __name__ == '__main__':
    runGame()