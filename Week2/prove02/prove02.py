# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Mab Lib words (prompted)
# Process: Read input, set variables, add to Mad Lib paragraph
# Output: Complete Mad Lib Paragraph

print('\nPlease enter the following: \n')

adjective = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
vowels = ['a','e','i','o','u']
article = 'a'
adjective2 = input('adjective: ')
food = input('favorite food: ')

outputExclamation = "\""+exclamation.capitalize()+"!\""

for vowel in vowels:
   if adjective2[0] == vowel:
      article = 'an'
   elif adjective2[0] != vowel:
      continue
print('\nYour story is: \n')

print(f'The other day, I was really in trouble. It all started when I saw a very','\n'+
adjective.strip(),animal.strip(),verb1.strip(), 'down the hallway.',outputExclamation.strip(),'I yelled. But all\n'+
'I could think to do was to', verb2.strip(), 'over and over. Miraculously,\n'+
'that caused it to stop, but not before it tried to', verb3.strip(), '\n'+
'right in front of my family.','After all of that drama and craziness,\n'+
'I decided to take my family out for',article.strip(),adjective2.strip(),food.strip()+'.\n')