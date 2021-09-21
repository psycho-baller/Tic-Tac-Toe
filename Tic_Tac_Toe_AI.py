from random import randint

xo = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

coordinates = ([1, 1], [1, 2], [1, 3],
               [2, 1], [2, 2], [2, 3],
               [3, 1], [3, 2], [3, 3]) 

winning_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],[1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def print_xo():
    print('---------')
    print('|', xo[0], xo[1], xo[2], '|')
    print('|', xo[3], xo[4], xo[5], '|')
    print('|', xo[6], xo[7], xo[8], '|')
    print('---------')
    
def x_win(): 
    for l in winning_patterns:
        line = [xo[l[0]], xo[l[1]], xo[l[2]]]
        if line.count('X') == 3:
            return True
        
def o_win(): 
    for l in winning_patterns:
        line = [xo[l[0]], xo[l[1]], xo[l[2]]]
        if line.count('O') == 3:
            return True

def is_full():
  for s in xo:
    if s == ' ':
        return False
  return True

def did_game_end():
    print_xo()
    if x_win():
        print('X wins\n')
        main()
    elif o_win():
        print('O wins\n')
        main()  
    elif is_full():
        print('Draw\n')
        main()
        
def is_end():
    x_win, o_win = False, False
    for x in winning_patterns:
        line = [xo[x[0]], xo[x[1]], xo[x[2]]]
        if line.count('X') == 3:
            x_win = True
            return 'X'
        if line.count('O') == 3:
            o_win = True
            return 'O'
    if not x_win and not o_win:
        if ' ' not in xo:
            return ' '
    return None
    
def med(output,check):
    for r,l in enumerate(winning_patterns):
        line = [xo[l[0]], xo[l[1]], xo[l[2]]]
        if line.count(check) == 2:
            for c, l in enumerate(line):
                if l == ' ':
                    xo[winning_patterns[r][c]] = output
                    print('Making move level "medium"')
                    did_game_end()
                    return True
    return False

def user(x_o):
    coord = input('Enter the coordinates: ').split()
    try:
        coord = [int(x) for x in coord]
        if any(t >= 4 for t in coord):
            print("Coordinates should be from 1 to 3!")
            user(x_o)
        for x in range(9):
            if coord == coordinates[x]:
                if xo[x] != ' ':
                    print("This cell is occupied! Choose another one!")
                    user(x_o)
                else:
                    xo[x] = x_o
                    did_game_end()
    except Exception:
        print("You should user numbers!")
        user(x_o)

def easy(x_o, level='easy'):
    coord = randint(0,8)
    if xo[coord] != ' ':
        easy(x_o)
    else:
        print(f'Making move level "{level}"')
        xo[coord] = x_o
        did_game_end()
               
def medium(x_o):
    o_x = 'O' if x_o == 'X' else 'X'
    check1 = med(x_o,x_o)
    if not check1:
        check2 = med(x_o,o_x)
        if not check2:
            easy(x_o, 'medium')
            
def hard(x_o):
    if x_o == 'X':
        (m, qx, qy) = min()
        xo[coordinates.index([qx, qy])] = 'X'
    else:
        (m, px, py) = max()
        xo[coordinates.index([px, py])] = 'O'
    print('Making move level "hard"')
    did_game_end()
    
def max():
    px, py = None, None
    maxv = -2
    result = is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == ' ':
        return (0, 0, 0)
    for p, (x, y) in zip(range(9), coordinates):
        if xo[p] == ' ':
            xo[p] = 'O'
            (m, min_x, min_y) = min()
            if m > maxv:
                maxv = m
                px, py = x, y
            xo[p] = ' '
    return (maxv, px, py)

def min():
    minv = 2
    qx, qy = None, None
    result = is_end()
    if result == 'X':
        return (-1, 0, 0)
    elif result == 'O':
        return (1, 0, 0)
    elif result == ' ':
        return (0, 0, 0)
    for p, (x, y) in zip(range(9), coordinates):
        if xo[p] == ' ':
            xo[p] = 'X'
            (m, max_x, max_y) = max()
            if m < minv:
                minv = m
                qx, qy = x, y
            xo[p] = ' '
    return (minv, qx, qy)
         
    
def main():
    global xo
    xo = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while True:
        command = input('Input command:').split()
        if command[0] == 'exit':
            exit()
        elif command[0] == 'start' and len(command) == 3:
            start(command)
        else:
            print('Bad parameters!')
            main()

def start(command):
    print_xo()
    first = command[1] + "('X')"
    second = command[2] + "('O')"
    while True:
        eval(first)
        eval(second)
main()