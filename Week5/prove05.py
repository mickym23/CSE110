# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Text commands based on adventure story
# Process: Get input and generate relevant story 
# Output: Printed adventure story

import time

name = input('\nPlease enter you name, my friend: ')

time.sleep(1)

print('\nWelcome to the adventure of Caliban, '+ str(name.lower().title()) + '!')

time.sleep(2)

print('''\nThe international titan agency (ITA) has sent you to lead your team to Caliban to retrieve an ancient artifact.
An artifact that could destroy the world if it fell into the wrong hands. After a long journey on horseback,
you finally arrive in the poverty-stricken village of Caliban. You look into the far distance and see the famous tourist
attraction of Caliban - the ancient ruins of Madara. Your team sets forward to travel to the ruins and scout for enemies.''')

print('''\nYour team arrives at the ruins of Madara. OH NO! The evil Pendragon has already sent his agents to surround the ruins and steal
the artifact. You look towards your right in the direction of the village you just passed through. 
No! The evil agents have taken the village hostage and are pillaging the houses and their farms.''')

print('Your team awaits your decisive call, should they ATTACK the evil agents with the artifact or DEFEND the village from destruction?')

# Loop around if answer is not "attack" or "defend"
while True:
   # Ask user for first choice's input
   choice1 = input('\nWhat is your choice? : ');

   time.sleep(2)

   if choice1.lower() == 'attack':
      print('''\nYou scream the battle cry and order a full engage attack! Your team speeds in to fight the evil agents
You look through all the smoke and dust and see Genral Kaiser, one of Pendragon's main henchmen.
You fly in on your wingsuit to attack the General. You notice that you have two weapons at your disposal,
you can conjure a frost SPELL or summon your titan from your AMULET. Which do you choose?''')
      break 
   elif choice1.lower() == 'defend':
      print('''\nYou order your team for a full retreat and reorganization to carry out the attack on the evil agents
that are destroying the village. You summon Solwing, your scouting titan, from your bonded amulets.
Solwing flies over the village and sees two main evil agent infantries - the crystal spear troopers and flame art spell snipers.
You have to create an execution plan immediately!! The spell snipers are closely protected by the spear troopers and the spell snipers
grant long range cover for the spear troopers. You have two deadshot frost spell snipers in your team. It is unlikely that they would
be able to take out all the flame spell snipers before the other snipers start shooting. What is your plan? Execute the TROOPERS or the SNIPERS first?''')
      break
   else:
      print('The action you entered in invalid. Please try again.')
      continue

# Ask user for second choice
# I will continue with second adn third choices in Week 6 (Snipers or Troopers)
# while True:
#    choice2 = input('\nWhat is your choice? : ')
#    break

# print(choice2)
