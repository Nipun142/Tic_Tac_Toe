  
def display(board):
    print('|_'+board[1]+'_|_'+board[2]+'_|_'+board[3]+'_|')
    print('|_'+board[4]+'_|_'+board[5]+'_|_'+board[6]+'_|')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')

def user_name():
    p1=input('Player1 Enter your Name: ')
    p2=input('Player2 Enter your Name: ')
    return p1,p2
 #Gives player1 and player2 name   

    
def marker_selection(p1name):
    marker=''
    while marker!='X' and marker!='O':
        marker=input(f'{p1name} select your marker (X/O): ').upper()
        if marker not in ['X','O']:
            print('Please choose between X and O')
    player1=marker
    if player1 =='X':
        player2='O'
    elif player1=='O':
        player2='X'
    return player1,player2


import random
def choose_first(p1name,p2name):
    flip=random.randint(0,1)
    if flip==1:
        return p1name
    else:
        return p2name
    
def place_marker(board,position,marker):
    board[position]=marker  
    
    
    
def win_check(board,marker):
    return((board[1]==board[2]==board[3]== marker) or
           (board[4]==board[5]==board[6]== marker) or
           (board[7]==board[8]==board[9]== marker) or
           (board[1]==board[4]==board[7]== marker) or
           (board[2]==board[5]==board[8]== marker) or
           (board[3]==board[6]==board[9]== marker) or
           (board[1]==board[5]==board[9]== marker) or
           (board[3]==board[5]==board[7]== marker))

def space_check(board,position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    #Board is full if True
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position=int(input('Choose a position (1-9): '))
    return position

def replay():
    choice=input('Play again? Y/N: ').upper()
    return choice=='Y'

print('Welcome to TIC TAC TOE')
while True:
    board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    p1name,p2name=user_name()
    player1,player2=marker_selection(p1name)
    turn=choose_first(p1name,p2name)
    print(turn +' goes first')
    play_game=input('Ready to play? y/n: ').lower()
    if play_game=='y':
        game_on=True
    else:
        game_on=False
    while game_on==True:
        if turn==p1name:
            display(board)
            position=player_choice(board)
            place_marker(board,position,player1)
            if win_check(board,player1):
                display(board)
                print(f'{p1name} won!')
                game_on=False
            else:
                if full_board_check(board):
                    print('Game is Tied!')
                    game_on=False
                else:
                    turn=p2name
        else:
            display(board)
            position=player_choice(board)
            place_marker(board,position,player2)
            if win_check(board,player2):
                display(board)
                print(f'{p2name} won!')
                game_on=False
            else:
                if full_board_check(board):
                    print('Game is Tied')
                    game_on=False
                else:
                    turn=p1name                 
    if not replay():
        break
