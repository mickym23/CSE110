print()
name_input = ''
names = []

while name_input.lower() != 'end':
   name_input = input('Type in the name of a friend: ')
   if (name_input.lower() == 'end'):
      break;
   else: 
      names.append(name_input.lower().title())

print() 

if name_input.lower() == 'end':
   if names == []:
      print('Unfortunately, you have no friends.')
   else:
      print('Your friends are: ')
      for name in names:
         print(name)
