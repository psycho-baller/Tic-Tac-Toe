xo = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def print_xo():
    print('---------')
    print('|', xo[0][0], xo[0][1], xo[0][2], '|')
    print('|', xo[1][0], xo[1][1], xo[1][2], '|')
    print('|', xo[2][0], xo[2][1], xo[2][2], '|')
    print('---------')


def x_win(): 
    if xo[0][0] == xo[0][1] == xo[0][2] == 'X' or xo[1][0] == xo[1][1] == xo[1][2] == 'X' or xo[2][0] == xo[2][1] == xo[2][2] == 'X' or xo[0][0] == xo[1][1] == xo[2][2] == 'X' or xo[0][2] == xo[1][1] == xo[2][0] == 'X' or xo[0][0] == xo[1][0] == xo[2][0] == 'X'or xo[0][1] == xo[1][1] == xo[2][1] == 'X' or xo[0][2] == xo[1][2] == xo[2][2] == 'X':
        return True

def o_win(): 
    if xo[0][0] == xo[0][1] == xo[0][2] == 'O' or xo[1][0] == xo[1][1] == xo[1][2] == 'O' or xo[2][0] == xo[2][1] == xo[2][2] == 'O' or xo[0][0] == xo[1][1] == xo[2][2] == 'O' or xo[0][2] == xo[1][1] == xo[2][0] == 'O' or xo[0][0] == xo[1][0] == xo[2][0] == 'O'or xo[0][1] == xo[1][1] == xo[2][1] == 'O' or xo[0][2] == xo[1][2] == xo[2][2] == 'O':
        return True

def is_full():
    full = 0
    for l in xo:
        for s in l:
            if s != ' ':
                full += 1
    if full == 9:
        return True
    else:
        return False

def did_game_end():
    print_xo()
    if x_win():
        print('X wins')
    elif o_win():
        print('O wins')  
    elif is_full():
        print('Draw')
 

n_of_turns = 0
def play():
    global n_of_turns
    while True:
        num = input('Enter the position you want put it in: ')
        if not (num.isdigit() and  1 <= int(num) <= 9):
            print('Please enter a number between 1 and 9')
            continue
        if num == '1':
            coord = '00'
        elif num == '2':
            coord = '01'
        elif num == '3':
            coord = '02'
        elif num == '4':
            coord = '10'
        elif num == '5':
            coord = '11'
        elif num == '6':
            coord = '12'
        elif num == '7':
            coord = '20'
        elif num == '8':
            coord = '21'
        elif num == '9':
            coord = '22'
        row = int(coord[0])
        column = int(coord[1])
        if xo[row][column] != ' ':
            print('This cell is occupied! Choose another one!')
            continue
        else:
            if n_of_turns % 2 == 0:
                xo[row][column] = 'X'
            else:
                xo[row][column] = 'O'
            n_of_turns += 1
            break

print("Input your X's and O's in this form shown below:")
print('-' * 9)
print('|', 1, 2, 3, '|')
print('|', 4, 5, 6, '|')
print('|', 7, 8, 9, '|')
print('-' * 9)
while True:
    did_game_end()
    if x_win() or o_win() or is_full():
        break
    play()