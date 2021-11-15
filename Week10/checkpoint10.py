print('\nPlease enter the items of the shopping list (type: quit to finish):')

item = ''

cart = []
print()
while (item.lower() != 'quit'):
   item = input('Item: ')

   if (item.lower() == 'quit'):
      break
   else:
      cart.append(item)


print('\nThe shopping list is:')
for prod in cart:
   print(prod.lower().title())

print('\nYour shopping list with indexes is: ')
index = 0
for prod in cart:
   print(f'{index}. ' + str(prod.lower().title()))
   index += 1

change_item_index = int(input('\nWhich item would you like to change? '))
change_item_name = input('What is the name of the new item? ')

cart[change_item_index] = change_item_name


print('\nYour shopping list with indexes is: ')
index = 0
for prod in cart:
   print(f'{index}. ' + str(prod.lower().title()))
   index += 1
