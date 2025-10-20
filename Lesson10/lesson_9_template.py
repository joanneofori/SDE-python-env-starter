import random

#custom intro story
print('You wake up on your couch. \n')

print('"Is there anyone there? Can anyone hear me?" says a voice from your television. \n')

print('Yes, the TV is talking to you. You are not going insane. \n')

name = input('"What is your name?" says the voice. ')

print('\n...I guess the voice heard you. \n')

print(f'"You gotta help me escape, {name}. I am trapped in here! Tell me where to go!?" \n')

print('"There should be a set of glasses on top of your TV. Put it on so you can see what I see." \n')

print('You realize the voice was not joking when a set of sunglasses miraculously appears on top of your TV. \nHesitantly, you put them on. \n')

door = input('Please choose a door (1, 2, or 3): ')

correct_door = random.choice(['1', '2', '3'])

while door!= correct_door:
  door = input('Nope, try again! 1, 2, or 3. ')

def puzzle():

  #custom message before seeing password list 

  options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']

  correct_password = random.choice(options)
 
  for word in options:
    if word == correct_password:   
      print(word.capitalize())
    else:
      print(word)

  #custom message before asking for a guess

  password_guess = input('Choose the password from the list.\n ') 
 

  while password_guess != correct_password:
    print('Incorrect password. Try again. ')
    password_guess = input('Password: ')

  #success message
 
"""
room = [
  'xxxxx',
  'x..ex',
  'x...x',
  'x...x',
  'xxxxx',
]
"""
#customize room layout 
room = [
  'xxxxxxxxxxxxxx',
  'x..........pex',
  'xxxxxxxxxxxxxx',
]

def announce_walls(current_row, current_col):
  if room[current_row - 1][current_col] == 'x': #up
    print('There is a wall up. ')
  if room[current_row + 1][current_col] == 'x': #down
    print('There is a wall down. ')
  if room[current_row][current_col - 1] == 'x': #left
    print('There is a wall left. ')
  if room[current_row][current_col + 1] == 'x': #right
    print('There is a wall right. ')
      
def move(current_row, current_col, direction):
  new_row = current_row
  new_col = current_col

  if direction == 'up':
    new_row -= 1
  elif direction == 'down':
    new_row += 1
  elif direction == 'left':
    new_col -= 1
  elif direction == 'right':
    new_col += 1
  else:
    print(f'You can not move {direction_choice}. Try up, down, left, or right')

  if room[new_row][new_col] == 'x': # Hit a wall!
    print('You can not move that way')
    return current_row, current_col
  elif room[new_row][new_col] == 'p': #Activate puzzle
    puzzle()
    return new_row, new_col 
    
  return new_row, new_col

player_row = 1
player_col = 1

while room[player_row][player_col] != 'e':
  announce_walls(player_row, player_col)
  direction_choice = input('What direction would you like to move? ')
  player_row, player_col = move(player_row, player_col, direction_choice)
  print(f'New row is {player_row}')
  print(f'New col is {player_col}')

print('You have unlocked the door. ')
print('You hear the voice again....')
print('\n"Thank you again for your help!" \n')