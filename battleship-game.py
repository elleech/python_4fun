import random

def print_board(board):
    for row in board:
        print(' '.join(row))

def rand_place():
    x = random.randrange(len(board))
    y = random.randrange(len(board))
    d = random.choice(['+x', '+y'])
    return(x, y, d)

def ship_type():
    # {'Shipname': [quantity, size]}
    ships = {'Aircarrier': [1, 5], 'Battleship': [1, 4], 'Cruiser': [1, 3],
             'Destroyer': [2, 2], 'Submarine': [2, 1]}
    return(ships)

def ship_space(ships):
    spaces = {}
    for name, [qty, size] in ships.items():
        spaces[name] = qty * size
    return(spaces)

def ship_place(board):
    ships = ship_type()
    for name, [qty, size] in ships.items():
        for num in range(qty):
            finish = False
            while not finish:
                (x, y, d) = rand_place()
                # print(name[0], '#', (num+1), 'size:', size, '@', x, y, d)
                if d == '+x':
                    if x < len(board)-size:
                        if board[y][x:x+size] == ['~']*size:
                            board[y][x:x+size] = [name[0]]*size
                            finish = True
                        else:
                            finish = False
                    else:
                        finish = False
                else:
                    if y < len(board)-size:
                        check = []
                        for i in range(size):
                            check.append(board[y+i][x])
                        if check == ['~']*size:
                            for j in range(size):
                                board[y+j][x] = name[0]
                            finish = True
                        else:
                            finish = False
                    else:
                        finish = False
    return(board)

def play(board, hidden_board, spaces):
    place = []
    chances = 2
    for name, space in spaces.items():
        chances += space
    for chance in range(chances):
        play = input("Bomb where? (col row) ")
        x = int(play.split()[0]) - 1
        y = int(play.split()[1]) - 1
        if [x, y] not in place:
            place.append([x, y])
            if board[y][x] != '~':
                for name, space in spaces.items():
                    if board[y][x] == name[0]:
                        if space > 0:
                            space -= 1
                            spaces[name] = space
                            hidden_board[y][x] = 'X'
                            print('Congrats! %s has been hit.' %(name))
                            print('You have %d times left.\n' %(chances-chance-1))
                            print_board(hidden_board)
            else:
                print('Missed.')
                print('You have %d times left.\n' %(chances-chance-1))
                print_board(hidden_board)
        else:
            print("You've bombed this spot.")
            print('You have %d times left.\n' %(chances-chance-1))
            print_board(hidden_board)



print("Let's play Battleship!\n")

hidden_board = []
for n in range(10):
    hidden_board.append(['~']*10)

board = []
for n in range(10):
    board.append(['~']*10)

board = ship_place(board)
print_board(hidden_board)
# print_board(board) '''Answer'''
spaces = ship_space(ship_type())
play(board, hidden_board, spaces)
print('Game over.')
