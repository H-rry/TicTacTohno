import os

playing = True
turn = True
first_player = True
def print_board(board): # A function that takes in the board (a single dimensional array of length 9) and prints it in the pretty format you can see

    os.system('clear') # change to 'cls' if you're using a windows based terminal

    for i in range(9):
        if board[i] == 1:
            print(' x ', end='')
        elif board[i] == 2:
            print(' o ', end='')
        else:
            print("   ", end='')
        if (i % 3 != 2):
            print('|', end='')
        elif i != 8:
            print("\n-----------")
    print("\n")


def make_move(move: str, board, turn): # this code converts a users input in the form xy e.g. 11 to the one dimensional board array
    if board[int(move[0])-1 + 3*(int(move[1])-1)] == 0:
        if turn == True:
            board[int(move[0])-1 + 3*(int(move[1])-1)] = 1
        elif turn == False:
            board[int(move[0])-1 + 3*(int(move[1])-1)] = 2
        turn = not turn
    return board, turn

def winner(board): # checks all 8 possibilities of a winner
    winner = 0
    if board[0] == board[3] == board[6] != 0:
        winner = board[0]
    if board[1] == board[4] == board[7] != 0:
        winner = board[1]
    if board[2] == board[5] == board[8] != 0:
        winner = board[2]
    if board[0] == board[1] == board[2] != 0:
        winner = board[0]
    if board[3] == board[4] == board[5] != 0:
        winner = board[3]
    if board[6] == board[7] == board[8] != 0:
        winner = board[6]
    if board[0] == board[4] == board[8] != 0:
        winner = board[0]
    if board[2] == board[4] == board[6] != 0:
        winner = board[2]

    if 0 not in board: 
        return 3

    return winner

def minimax(board, maximizing_player): # minimax algorithm always finds the minimising path to victory
    value = winner(board)
    if value != 0: # i.e. if the game is over then return who won or if it's a draw
        if value == 2: return (-100, None)
        if value == 1: return (100, None)
        if value == 3: return (0, None)

    if maximizing_player: # then recursively finds the path to that player winning
        best_score = -100
        best_move = None
        for i in range(9):
            if board[i] == 0:
                state = board.copy()
                state[i] = 1
                value = minimax(state, not maximizing_player)[0]
                if value > best_score:
                    best_move = i
                    best_score = value
    else:
        best_score = 100
        best_move = None
        for i in range(9):
            if board[i] == 0:
                state = board.copy()
                state[i] = 2
                value = minimax(state, not maximizing_player)[0]
                if value < best_score:
                    best_move = i
                    best_score = value
    return best_score, best_move

board = [0,0,0,0,0,0,0,0,0]

def reset_game(board):
    board = [0,0,0,0,0,0,0,0,0]
    return board

while playing: # game loop
    if board == [0,0,0,0,0,0,0,0,0]: # keeps track of who goes first
        turn == first_player
        first_player != first_player

    print_board(board)
    
    win = winner(board)
    if win != 0: # checks for winner
        if win == 1:
            print("x wins!")
        if win == 2:
            print("o wins!")
        if win == 3:
            print("draw!")
        
        
        play_again = input("play again: y,n")# if game over then chicks if they want to play again
        if play_again == 'y':
            board2 = reset_game(board)
        elif play_again == 'n':
            playing = False
            break

    if turn == True: # player turn and computer turn
        print("what's your next move? in form xy")
        board, turn = make_move(input(), board, turn)
    else:
        move = minimax(board, turn)[1]
        board[move] = 2
        turn = not turn

