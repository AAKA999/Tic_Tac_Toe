import random

def display_board(current_board):
    print(current_board[0]+'|'+current_board[1]+'|'+current_board[2])
    print(current_board[3]+'|'+current_board[4]+'|'+current_board[5])
    print(current_board[6]+'|'+current_board[7]+'|'+current_board[8])

def player_input():
    selection=input('Player choose your marker, X or O:  ')
    if (selection.upper()=='X'):
        return ('X','O')
    elif (selection.upper()=='O'):
        return ('O','X')

def place_marker(the_board,position,marker):
    if position in range (0,9):
        the_board[position] = marker

def choose_first():
    switch=random.randint(0,1)
    if (switch==1):
        return 'Player'
    else:
        return 'Computer'

def win_check(the_board,turn):
    if (the_board[0]==the_board[1]==the_board[2] or
        the_board[3]==the_board[4]==the_board[5] or
        the_board[6]==the_board[7]==the_board[8] or
        the_board[0]==the_board[3]==the_board[6] or
        the_board[1]==the_board[4]==the_board[7] or
        the_board[2]==the_board[5]==the_board[8] or
        the_board[0]==the_board[4]==the_board[8] or
        the_board[2]==the_board[4]==the_board[6] ):
        return True

def board_full_check(the_board):
    board_full = True
    for i in range(0,9):
        if the_board[i].isdigit():
            board_full = False
    return board_full

def replay():
    choice=input('Play again? Yes or No:').upper()
    return choice=='YES'


while(True):
    print('WELCOME TO TIC TAC TOE !!!')
    the_board=['0','1','2','3','4','5','6','7','8']
    display_board(the_board)

    p1,p2=player_input()
    print(f'Player marker is {p1}\nComputer marker is {p2}')

    turn=choose_first()
    print(turn+ ' will go first')

    game_status= True
    while(game_status):
        if turn=='Player':
            position= int(input(f'{turn}, select a position to make your move: '))
            if position in range(0,9):
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
                print('Player won!!')
                game_status=False
            else:
                if board_full_check(the_board):
                    display_board(the_board)
                    print('TIE Game!!')
                    game_status=False
                    break
                else:
                    turn='Computer'

        else:
            print(f'{turn} will select a position to make its move now')
            if the_board[4]=='4' and (the_board[1]==the_board[7] or the_board[3]==the_board[5] or the_board[0]==the_board[8] 
            or the_board[2]==the_board[6]):
                position=4
            elif the_board[0]=='0' and (the_board[1]==the_board[2] or the_board[3]==the_board[6] or the_board[4]==the_board[8]):
                position=0
            elif the_board[2]=='2' and (the_board[1]==the_board[0] or the_board[5]==the_board[8] or the_board[4]==the_board[6]):
                position=2
            elif the_board[6]=='6' and (the_board[0]==the_board[3] or the_board[7]==the_board[8] or the_board[2]==the_board[4]):
                position=6
            elif the_board[8]=='8' and (the_board[2]==the_board[5] or the_board[6]==the_board[7] or the_board[0]==the_board[4]):
                position=8
            elif the_board[1]=='1' and (the_board[0]==the_board[2] or the_board[4]==the_board[7]):
                position=1
            elif the_board[3]=='3' and (the_board[0]==the_board[6] or the_board[4]==the_board[5]):
                position=3
            elif the_board[5]=='5' and (the_board[2]==the_board[8] or the_board[3]==the_board[4]):
                position=5
            elif the_board[7]=='7' and (the_board[1]==the_board[4] or the_board[6]==the_board[8]):
                position=7
            else:
                position=random.randint(0,8)
            print(f'{turn} will place {p2} at position {position}')
            if the_board[position]!='X' and the_board[position]!='O':
                place_marker(the_board,position,p2)
                display_board(the_board)
            else:
                continue
            if win_check(the_board,turn):
                display_board(the_board)
                print('Computer won!!')
                game_status=False
            else:
                if board_full_check(the_board):
                    display_board(the_board)
                    print('TIE Game!!')
                    game_status=False
                    break
                else:
                    turn='Player'
    if not replay():
        break