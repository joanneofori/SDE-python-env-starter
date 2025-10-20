color = 'green'

guess = input('What is my favorite color? ')

while guess != color:
  print(f'Nope! {guess} is not my favorite color.')
  guess = input('Try again: ')

print('Yup! It was green.')
