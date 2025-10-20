import random

name = input('What is your name? ')

#custom theme = space
print(f'Welcome to the INTERGALACTIC Escape Room, {name}!')

door = input('Please choose a door (1, 2, or 3): ')

correct_door = random.choice(['1', '2', '3'])

if door == correct_door:
  print('You escaped!')
else:
  print('You did not escape :(')


#password puzzle + description message
print('You enter an empty dark room...')
print()
print('There is something glowing in the corner. ')

#space theme: asteroid, planet, star, moon, astronaut, sun
options = ['asteroid', 'planet', 'star', 'moon', 'astronaut', 'sun']

correct_password = random.choice(options)

for word in options:
  if word == correct_password:
    print(word.capitalize())
  else:
    print(word)

print('In front of you, you see a computer terminal asking you for a password.') #custom message

password_guess = input('Choose the password from the list. ')

if password_guess == correct_password:
  print('The computer begins to glow.')
  print('The wall in front of you sinks into the ground, revealing a getaway space craft! ')
  print('You have escaped!')
else:
  print('Capitalization is key! Try again! ')
