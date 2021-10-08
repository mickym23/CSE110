# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Restaurant, Family, and Meal Orders
# Process: Calculate sales tax and subtotal
# Output: Complete end of receipt

water_price = 2.99
soft_drink_price = 3.99

child_meal_price = float(input('What is the price of the child\'s meal? '))
adult_meal_price = float(input('What is the price of an adult\'s meal? '))
amount_of_water = int(input('How many bottles of water would you like to order? '))
amount_of_soft_drinks = int(input('How many bottles of soft drinks would you like to order? '))
amount_of_children = int(input('How many children are there? '))
amount_of_adults = int(input('How many adults are there? '))
sales_tax = float(input('What is the sales tax rate? '))

subtotal  = (child_meal_price * amount_of_children) + (adult_meal_price * amount_of_adults) + (amount_of_water * water_price) + (amount_of_soft_drinks * soft_drink_price)
print(f'\nSubtotal: $'+"{:.2f}".format(subtotal))
sales_tax_percent = sales_tax / 100
meal_sales_tax = subtotal * sales_tax_percent;
print(f'Sales Tax: $' + "{:.2f}".format(meal_sales_tax))
total = subtotal + meal_sales_tax
print(f'Total: $'+"{:.2f}".format(total))

def moneyPayment():
   money_paid = float(input('\nWhat is the payment amount? '))
   change = money_paid - total

   if money_paid < total:
      change = change * -1
      print(f'Hi there, you still need to pay: $' + "{:.2f}".format(change) + '. Please restart transaction.')
      moneyPayment();
   else:
      print(f'Change: $'+"{:.2f}".format(change))
      print(f'\nThank you! Have a great day.\n')

moneyPayment();





