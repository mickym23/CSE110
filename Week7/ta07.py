import random

number = random.randint(1, 100)

guess = 0
#print(number)
while guess != number:
   guess = int(input('What is your guess? '))

   if guess < number:
      print('Higher')
   elif guess > number:
      print('Lower')
   else:
      print('You guessed it!')
   