name = input('What is your name? ')
print(f'Welcome to our escape room, {name}!')

door = input('Please choose a door (1, 2, or 3): ')
if door == '1':
  print('You escaped!')
else:
  print('You did not escape :( ')
