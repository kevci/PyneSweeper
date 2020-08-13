from enum import Enum 

class Action(Enum):
    UNCOVER = 1
    FLAG = 2

DEFAULT_BOARD_HEIGHT = 10
DEFAULT_BOARD_WIDTH = 10
DEFAULT_MINE_COUNT = 30

mine_locations = []
board = [[]]

def initBoard():
    #assume random mine placement for now
    #generate mine placements
    pass

def displayStartInfo():
    pass

def render():
    print(board)

# @return (pos_x, pos_y, action)
def handleInput():
    user_input_raw = input('Make your move...')
    user_input = user_input_raw.split(' ')
    return user_input

# @input (pos_x, pos_y, action)
def updateBoard(user_input):
    board[pos_x][pos_y] = 

def gameLoop():
    initBoard()
    displayStartInfo()
    while True:
        input = handleInput()
        updateBoard(input)
        render()

if __name__ == '__main__':
    gameLoop()