import random

def puzzle():
    print('You enter a room with large words printed on the walls.')

    words = ['tracker', 'ribbon', 'corkscrew', 'sawhorse', 'tranquility', 'hyacinth']
    true_password = random.choice(words)
    for word in words:
        if word == true_password:
            print(word.upper())
        else:
            print(word)
    print('In front of you, you see a computer terminal asking you for a password.')
    guess = input('Password: ')
    while guess != true_password:
        print('Nope.')
        guess = input('Password: ')

    print('The computer begins to glow.')
    print('The wall in front of you sinks into the ground.')

def move(row, col, move_dir):
    row_change = 0
    col_change = 0

    if move_dir == 'u':
        row_change = -1
        col_change = 0
    elif move_dir == 'd':
        row_change = 1
        col_change = 0
    elif move_dir == 'l':
        row_change = 0
        col_change = -1
    elif move_dir == 'r':
        row_change = 0
        col_change = 1
    return row + row_change, col + col_change

def game(maze, start_row, start_col):
    name = input('What is your name? ')
    row, col = start_row, start_col

    print(f'Welcome to our escape room, {name}.')
    while maze[row][col] != 'e':
        move_dir = input('What direction would you like to move? ')
        if move_dir not in ('u', 'd', 'l', 'r'):
            print('Direction must be u, d, l, or r')
            continue

        next_row, next_col = move(row, col, move_dir)

        if maze[next_row][next_col] == 'x':
            print('There is a wall there')
        elif maze[next_row][next_col] == 'p':
            puzzle()
            row = next_row
            col = next_col
        else:
            row = next_row
            col = next_col

    print('You have escaped!')

maze = [
    'xxxxxxxxxx',
    'x........x',
    'xxxxxx.xxx',
    'xe.x.x.x.x',
    'xpx..x.x.x',
    'x.x..x...x',
    'x.x.xx.xxx',
    'x......x.x',
    'x........x',
    'xxxxxxxxxx',
]

if __name__ == '__main__':
    #game(maze, start_row=1, start_col=1))
    game(maze, start_row=5, start_col=1)
