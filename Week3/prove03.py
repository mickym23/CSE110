# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Restaurant, Family, and Meal Orders
# Process: Calculate sales tax and subtotal
# Output: Complete end of receipt

waterPrice = 2.99
softDrinkPrice = 3.99

childMealPrice = float(input('What is the price of the child\'s meal? '))
adultMealPrice = float(input('What is the price of an adult\'s meal? '))
amountOfWater = int(input('How many bottles of water would you like to order? '))
amountOfSoftDrinks = int(input('How many bottles of soft drinks would you like to order? '))
amountOfChildren = int(input('How many children are there? '))
amountOfAdults = int(input('How many adults are there? '))
salesTax = float(input('What is the sales tax rate? '))

subtotal  = (childMealPrice * amountOfChildren) + (adultMealPrice * amountOfAdults) + (amountOfWater * waterPrice) + (amountOfSoftDrinks * softDrinkPrice)
print(f'\nSubtotal: $'+"{:.2f}".format(subtotal))
salesTaxPercent = salesTax / 100
mealSalesTax = subtotal * salesTaxPercent;
print(f'Sales Tax: $' + "{:.2f}".format(mealSalesTax))
total = subtotal + mealSalesTax
print(f'Total: $'+"{:.2f}".format(total))

moneyPaid = float(input('\nWhat is the payment amount? '))
change = moneyPaid - total
print(f'Change: $'+"{:.2f}".format(change))

print(f'\nThank you! Have a great day.\n')





