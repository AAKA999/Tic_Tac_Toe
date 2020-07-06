import random

def display_board(current_board):
    print(current_board[1]+'|'+current_board[2]+'|'+current_board[3])
    print(current_board[4]+'|'+current_board[5]+'|'+current_board[6])
    print(current_board[7]+'|'+current_board[8]+'|'+current_board[9])

def player_input():
    selection=input('Player 1 choose your marker, X or O:  ')
    if (selection.upper()=='X'):
        return ('X','O')
    elif (selection.upper()=='O'):
        return ('O','X')

def place_marker(the_board,position,marker):
    if position in range (1,10):
        the_board[position] = marker

def choose_first():
    switch=random.randint(0,1)
    if (switch==1):
        return 'Player 1'
    else:
        return 'Player 2'

def win_check(the_board,turn):
    if (the_board[1]==the_board[2]==the_board[3] or
        the_board[4]==the_board[5]==the_board[6] or
        the_board[7]==the_board[8]==the_board[9] or
        the_board[1]==the_board[4]==the_board[7] or
        the_board[2]==the_board[5]==the_board[8] or
        the_board[3]==the_board[6]==the_board[9] or
        the_board[1]==the_board[5]==the_board[9] or
        the_board[3]==the_board[5]==the_board[7] ):
        return True

def board_full_check(the_board):
    board_full = True
    for i in range(1,10):
        if the_board[i].isdigit():
            board_full = False
    return board_full

def replay():
    choice=input('Play again? Yes or No:').upper()
    return choice=='YES'


while(True):
    print('WELCOME TO TIC TAC TOE !!!')
    the_board=['#','1','2','3','4','5','6','7','8','9']
    display_board(the_board)

    p1,p2=player_input()
    print(f'Player 1 marker is {p1}\nPlayer 2 marker is {p2}')

    turn=choose_first()
    print(turn+ ' will go first')

    game_status= True
    while(game_status):
        if turn=='Player 1':
            #display_board(the_board)
            position= int(input(f'{turn}, select a position to make your move: '))
            if position in range(1,10):
                if the_board[position]!='X' and the_board[position]!='O':
                    place_marker(the_board,position,p1)
                    display_board(the_board)
                else:
                    print('Choose correct position!')
                    continue
            else:
                print('Choose correct position!')
            if win_check(the_board,turn):
                display_board(the_board)
                print('Player 1 won!!')
                game_status=False
            else:
                if board_full_check(the_board):
                    display_board(the_board)
                    print('TIE Game!!')
                    game_status=False
                    break
                else:
                    turn='Player 2'

        else:
            #display_board(the_board)
            position= int(input(f'{turn}, select a position to make your move: '))
            if position in range(1,10):
                if the_board[position]!='X' and the_board[position]!='O':
                    place_marker(the_board,position,p2)
                    display_board(the_board)
                else:
                    print('Choose correct position!')
                    continue
            else:
                print('Choose correct position!')
            if win_check(the_board,turn):
                display_board(the_board)
                print('Player 2 won!!')
                game_status=False
            else:
                if board_full_check(the_board):
                    display_board(the_board)
                    print('TIE Game!!')
                    game_status=False
                    break
                else:
                    turn='Player 1'

    if not replay():
        break