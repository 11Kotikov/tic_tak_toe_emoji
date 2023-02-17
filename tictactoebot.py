import emoji

def field_creating(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[i*3], "|", board[i*3+1], "|", board[i*3+2], "|")
    print ("-" * 13)

def player_moves(player_xo):
    flag = False
    while not flag:
        player_xo_move = input(f'put your {player_xo}  on empty cell: ')
        try:
            player_xo_move = int(player_xo_move)
        except:
            print (f'please try numbers from 1-9 to put your {player_xo}')
            continue
        if player_xo_move >= 1 and player_xo_move <= 9:
            if (str(field[player_xo_move-1]) not in "XO"):
                field[player_xo_move-1] = player_xo
                flag = True
            else:
                print ('This cell has already taken')
        else:
            print ('Your input incorrect, please try again:')

def win_checking(field):
    win_positions = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_positions:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False

print(emoji.emojize("First Player who will be :cross_mark: , put your name here: ")) 
first_player = input() + emoji.emojize(":cross_mark:") 
print()
print(emoji.emojize("First Player who will be :hollow_red_circle: , put your name here:")) 
second_player = input() + emoji.emojize(":hollow_red_circle:")

counter = 0
win = False
field = list(range(1,10))
while not win:
    field_creating(field)
    if counter % 2 == 0:
        print (first_player+', now it\'s your turn,')
        player_moves(emoji.emojize(":cross_mark_button:"))
    else:
        print (second_player+', now it\'s your turn,')
        player_moves(emoji.emojize(":O_button_(blood_type):"))
    counter += 1
    if counter > 4:
        current_player = win_checking(field)
        if current_player=='X':
            print (first_player, "has Won!")
            win = True
            break
        if current_player=='O':
            print (first_player, "has Won!")
            win = True
            break
    if counter == 9:
        print ("It's a tie!")
        break
field_creating(field)