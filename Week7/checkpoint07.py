
# While Loop Practice

number_input = int(input('\nPlease type a positive number: '))

while number_input < 0:
   print('\nSorry that is a negative number. Please try again.')
   number_input = int(input('\nPlease type a positive number: '))


print(f'\nThe number is: {number_input}')


# Sweets?
answer = input('May I have a piece of candy? ')

while answer.lower().strip() != 'yes':
  answer = input('May I have a piece of candy? ')

print('Thank you.') 