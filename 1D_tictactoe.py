from random import randrange

board = "--------------------"

def move(board, mark, position):
    # Returns the game board with the given mark in the given position.
    return board[:position] + mark + board[position+1:]


def player_move():
    # Returns a game board with the player's move.
    global board
    mark = "x"
    while True:
        try:
            position = int(input("In which position do you want to play? "))
        except ValueError:
            print("Position needs to be an integer between 0 and 19. Try again!")
            continue
        if position < 0:
            print ("Position needs to be between 0 and 19. Try again!")
        elif position > 19:
            print ("Position needs to be between 0 and 19. Try again!")
        elif board[position] == "x":
            print ("That position is already taken. Try againg!")
        elif board[position] == "o":
            print ("That position is already taken. Try againg!")
        else:
            board = move(board, mark, position)
            print ("Player move:  ", board)
            break

def pc_strategy(pattern):
    # Places the pc move before or after (if position already taken) a certain pattern is found.
    global board
    mark = "o"
    while True:
        position = board.rfind(pattern)
        try:
            if board[position + len(pattern)] == "-" :
                board = move(board, mark, position + len(pattern))
                print ("Computer move:", board)
                break
        except IndexError:     # exception used in case string index out of range e.g. position + len(pattern) > 19
            position = position

        if board[abs(position - 1)] == "-" :        # abs used to avoid getting negative position numbers 
            board = move(board, mark, position - 1)
            print ("Computer move:", board)
            break        
        else:
                position = randrange(0,19)
                if board[position] == "-" :
                    board = move(board, mark, position)
                    print ("Computer move:", board)
                    break

def pc_move():
    # Returns a game board with the computer's move.
    mark = "o"
    global board
    while True:
        if "xx" in board:
            pc_strategy("xx")
            break
        elif "oo" in board:    
            pc_strategy("oo")
            break
        elif "o" in board:
            pc_strategy("o")
            break
        elif "x" in board:
            pc_strategy("x")
            break
        else:
            position = randrange(0,19)
            if board[position] == "-" :
                board = move(board, mark, position)
                print ("Computer move:", board)
                break
            else:
                continue

# lauching the game
while True:
    player_move()
    if "xxx" in board:
        print ("Player wins!")
        break
    elif "-" not in board:
        print ("Draw")
        break
    else:
        pc_move()
        if "ooo" in board:
            print ("Computer wins!")
            break
        elif "-" not in board:
            print ("Draw")
            break
        else:
            continue
       