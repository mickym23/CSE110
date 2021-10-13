num1 = int(input('\nWhat is the first number? '))
num2 = int(input('What is the second number? '))

if num1 > num2:
   print('The first number is greater')
else:
   print('The first number is not greater')

if num1 == num2:
   print('The numbers are equal')
else:
   print('The numbers are not equal')

if num1 < num2:
   print('The second number is greater')
else:
   print('The second number is not greater')

animal = input('\nWhat is your favorite animal? ')

if animal.lower() == 'dog':
   print('That\'s my favorite animal too!')
else:
   print('That is not my favorite.')