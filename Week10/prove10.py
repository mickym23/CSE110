# Title: Shopping Cart and Product List
# Author: Mikhail Cedras

print('\nWelcome to the Shopping Cart Program!')

inventory = []
action = ''

while (action != 5):
   print('''
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
         ''')
   try:
      # Ask for user input
      action = int(input('Please enter an action: '))

      # Error handle if user enters anything other than the required number range
      while action <= 0 or action > 5:
         print('\nInvalid input, please enter a value between 1 and 5')
         action = int(input('Please enter an action: '))
   except: 
      # Handles input that is not an int
      print('\nInvalid input, please enter a value between 1 and 5')
      action = int(input('Please enter an action: '))

   # Add item to cart
   if action == 1:
      item = input('What item would you like to add? ')
      try:
         price = float(input(f'What is the price of \'{item}\'? '))
      except:
         print('\nInvalid input, please enter a valid number.')
         price = float(input(f'What is the price of \'{item}\'? '))

      itemObj = {
         "item_name": item.lower().title(),
         "item_price": format(price, '.2f')
      }
      inventory.append(itemObj)
      print(f'\'{item}\' has been added to the cart.')

   # View cart
   if action == 2:
      if len(inventory) == 0:
         print('You have no items in the cart.')
      else:
         print('The contents of the shopping cart are: ')
         counter = 1
         for product in inventory:
            print(f'{counter}. {product["item_name"]} - ${product["item_price"]}')
            counter += 1

   # Remove item from cart
   if action == 3:
      if (len(inventory) == 0):
            print('Action could not be completed. No items in cart.')
            continue
      
      try:
      
         index = int(input(f'Which item would you like to remove? '))

         while index <= 0:
            print('\nInvalid input, please enter a valid number between 1 and ' + str(len(inventory)) + '.')
            index = int(input(f'Which item would you like to remove? '))

         while index > len(inventory):
            print('\nInvalid input, please enter a valid number between 1 and ' + str(len(inventory)) + '.')
            index = int(input(f'Which item would you like to remove? '))
      except:
         print('\nInvalid input, please enter a valid number between 1 and ' + str(len(inventory)) + '.')
         index = int(input(f'Which item would you like to remove? '))

      inventory.pop(index-1)
      print('Item has been removed.')

   # Compute Total
   if action == 4:
      total_price = 0.00
      for product in inventory:
         item_price = product["item_price"]
         total_price += float(item_price)
      print(f'The total price of the items in the shopping cart is ${total_price}')
   
   # Quit
   if action == 5:
      print('Thank you for shopping with us!')
      break
      




