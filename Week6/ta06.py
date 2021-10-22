first_person  = int(input('What is the age of the first rider? '))
first_person_height  = int(input('What is the height of the first rider? '))

ask = input('Is there a second rider (yes/no)? ')

if (ask.lower() == 'no'):
   print('Sorry, you may not ride.');
else:
   second_person  = int(input('What is the age of the second rider? '))
   second_person_height  = int(input('What is the height of the second rider? '))
   if (first_person_height < 36 or second_person_height < 36):
      print('Sorry, you may not ride.');
   elif (first_person >= 18) and (first_person_height >= 62):
      print('Welcome to the ride. Please be safe and have fun!')
   elif (first_person >= 18) or (second_person >= 18):
      print('Welcome to the ride. Please be safe and have fun!')
   else:
      print('Sorry you may not ride.')


