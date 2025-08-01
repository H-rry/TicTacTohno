import os

playing = True
turn = True



def print_board(board):

    os.system('cls')

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


def make_move(move: str, board, turn):
    if board[int(move[0])-1 + 3*(int(move[1])-1)] == 0:
        if turn == True:
            board[int(move[0])-1 + 3*(int(move[1])-1)] = 1
        elif turn == False:
            board[int(move[0])-1 + 3*(int(move[1])-1)] = 2
        turn = not turn
    return board, turn

def winner(board):
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

def minimax(board, maximizing_player):
    value = winner(board)
    if value != 0:
        if value == 2: return (-100, None)
        if value == 1: return (100, None)
        if value == 3: return (0, None)

    if maximizing_player:
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
def reset_game(board, turn):
    board = [0,0,0,0,0,0,0,0,0]
    turn = not turn
    return board, turn
while playing:
    
    print_board(board)
    
    win = winner(board)
    if win != 0:
        if win == 1:
            print("x wins!")
        if win == 2:
            print("o wins!")
        if win == 3:
            print("draw!")
        play_again = input("play again: y,n")
        if play_again == 'y':
            board, turn = reset_game(board, turn)
        elif play_again == 'n':
            playing = False
            break

    if turn == True:
        print("what's your next move? in form xy")
        board, turn = make_move(input(), board, turn)
    else:
        move = minimax(board, turn)[1]
        board[move] = 2
        turn = not turn

