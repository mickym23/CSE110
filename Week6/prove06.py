# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: Text commands based on adventure story
# Process: Get input and generate relevant story 
# Output: Printed adventure story

import time

name = input('\nPlease enter you name, my friend: ')

time.sleep(1)

print('\nWelcome to the adventure of Caliban, '+ str(name.lower().strip().title()) + '!')

def main():

   time.sleep(2)

   print('''\n   The international titan agency (ITA) has sent you to lead your team to Caliban to retrieve an ancient artifact.
   An artifact that could destroy the world if it fell into the wrong hands. After a long journey on horseback,
   you finally arrive in the poverty-stricken village of Caliban. You look into the far distance and see the famous tourist
   attraction of Caliban - the ancient ruins of Madara. Your team sets forward to travel to the ruins and scout for enemies.''')

   print('''\n   Your team arrives at the ruins of Madara. OH NO! The evil Pendragon has already sent his agents to surround the ruins and steal
   the artifact. You look towards your right in the direction of the village you just passed through. 
   No! The evil agents have taken the village hostage and are pillaging the houses and their farms.''')

   print('   Your team awaits your decisive call, should they ATTACK the evil agents with the artifact or DEFEND the village from destruction?')

   # Loop around if answer is not "attack" or "defend"
   while True:
      # Ask user for first choice's input
      choice1 = input('\n   What is your choice? : ');

      time.sleep(2)

      if choice1.lower().strip() == 'attack':
         print('''\n   You scream the battle cry and order a full engage attack! Your team speeds in to fight the evil agents
   You look through all the smoke and dust and see Genral Kaiser, one of Pendragon's main henchmen.
   You fly in on your wingsuit to attack the General. You notice that you have two weapons at your disposal,
   you can conjure a frost SPELL or summon your titan from your AMULET. Which do you choose?''')
         break 
      elif choice1.lower().strip() == 'defend':
         print('''\n   You order your team for a full retreat and reorganization to carry out the attack on the evil agents
   that are destroying the village. You summon Solwing, your scouting titan, from your bonded amulets.
   Solwing flies over the village and sees two main evil agent infantries - the crystal spear troopers and flame art spell snipers.
   You have to create an execution plan immediately!! The spell snipers are closely protected by the spear troopers and the spell snipers
   grant long range cover for the spear troopers. You have two deadshot frost spell snipers in your team. It is unlikely that they would
   be able to take out all the flame spell snipers before the other snipers start shooting. What is your plan? Execute the TROOPERS or the SNIPERS first?''')
         break
      else:
         print('   The action you entered in invalid. Please try again.')
         continue

   # Ask user for second choice
   # I will continue with second adn third choices in Week 6 (Snipers or Troopers)
   while True:
      choice2 = input('\n   What is your choice? : ')
      
      time.sleep(2)

      if choice2.lower().strip() == "spell":
         print('''\n   You hone your chakra and draw the frost symbol in the air. Suddenly both your hands start emitting
   tremendous amounts of power, you have never seen this amount of power before. The ancient site evokes an ancestral
   rage within you. You look towards your hands again and in there you have two energy balls enchanted with the frost spirit's 
   power. You start spiraling in the air to gain maximum speed. As you approach General Kaiser, you toss the energy balls.
   He dodged the first one, but didn't see the second one coming. In order to save General Kaiser, his power-bonded
   titan, Beerus the Bone Crusher, summons itself and takes the energy ball damage, leaving him vulnerable. 
   You notice that you are flying right into Beerus, will you continue shooting energy balls to KILL the titan and risk being captured
   by General Kasier or will you use your frost wind SPELL to change your trajectory and risk breaking a bone on landing?''')
         break
      elif choice2.lower().strip() == "amulet":
         print('''\n   You call out to summon your titan, you focus on channeling your frost energy to your amulet. You 
   begin to feel the connection with your titan. You finally exclaim "Summon Ymir, Guardian of Asgard!" You hear a rumbling 
   in the sky. Down from the heavens dives the frost giant titan. General Kaiser orders some of his evil agents to protect him.
   General Kaiser calls out and summons his monolithic titan, Beerus the Bone Crusher. His evil agents call on their titans,
   Stryxes, the flying battallion. Ymir catches you mid-air and safely lands on the ground. However, you are completely surrounded.
   General Kaiser and the evil agents alongside their titans have you completely cornered. Do you FIGHT them alone with Ymir, will
   you SURRENDER your titan and amulet to escape, or will you SETTLE for a deal that they can take the ancient artifact?''')
         break
      elif choice2.lower().strip() == "troopers":
         print('''\n   You create a game plan with your team. You organize the frontmen to conjure radiant frost shield spells. 
   These special shields will be able to protect majority of your team for a limited time. They block flame spells, but allow
   frost spells through. You team engages the troopers and push toward their base. The flame troopers become aware of this
   attack and retaliate with their flame spells and flame spears. With oversight from the flame snipers they start shooting the shields,
   but your shields are holding up so far. Your frost snipers are able to find gaps through which they can shoot the flame troopers.
   You hear a massive thump and see two members of your team laying on the ground. They have been shot by a rogue enemy frost sniper.
   Your team is now considerably vulnerable. Do you issue a RETREAT or do you continue to ENGAGE hoping that your frost snipers
   can locate and execute the enemy frost sniper?''')
         break
      elif choice2.lower().strip() == "snipers":
         print('''\n   You order your team to execute operation black cat--the ultimate stealth formation--your spellcasters begin
   conjuring mirage spells as you cross over into the thick bush. Your frost snipers are ready. They have a shot on the flame snipers
   and are awaitng your call. You give them the green light. They take both frost shots at the same time. They are successful!
   The flame spear troopers are vulnerable now. You defeat them and reclaim the village. You hear a thump and see one of your team
   members are dead on the ground. This was an enemy frost sniper. You see the flash from his frost rifle in the distance. 
   Do you CHASE after him or do you RETURN back to the ancient ruins to pursue General Kaiser for the ancient artifact?''')
         break
      else:
         print('   The action you entered in invalid. Please try again.')
         continue

   # Ask user for third choice
   while True:
      choice3 = input('\n   What is your choice? : ')
      
      time.sleep(2)

      if choice3.lower().strip() == "kill":
         print('''\n   You focus your energy back to your frost powers. You realize that if you don't deal a crushing blow to both 
   Beerus and General Kaiser, you will be captured. You are the only barrier stopping them from gaining an advantage in the titan
   war. You look round and see the water droplets in the air starting to crystalize. What is happening? Your hands are turning a 
   bright blue radiating in the sun, it's your ancient ancestral power flow. Your energy balls have been fuelled tenfold. You toss
   the enregy balls directly at Beerus. The first energy ball destroys him, causing him to return back to the amulet. However, your
   second ball is travelling directly at General Kaiser. You hit him with the energy ball, he is knocked out unconcious. The
   evil agents see that their leader is down and immediately retreat. they leave with General Kaiser, but not with the ancient
   ruin. You have saved the day and protected humanity!''')
         break
      
      elif choice3.lower().strip() == "spell":
         print('''\n   You channel your energy and cast your frost wind spell. You are pushed horizontally in the air, avoiding
   Beerus and General Kaiser. As you land you call on the very last of your chakra left in you to cast another frost wind spell allowing you to
   land softer. However, all of your evergy is spent. You are no longer able to fight. Your team sees your distress and comes to
   the rescue. They determine that the mission can no longer continue, considering the team's overall chakra levels. You have lost
   the battle, but you have not lost the war. You'll get them next time soldier.''')
         break

      elif choice3.lower().strip() == "fight":
         print('''\n   You and power-bonded Ymir steps up to the task at hand. You fight valiantly and sweep the entire Stryxes battalion.
   You and Ymir are battle weary, you are feeling low on chakra. General Kaiser is the only one left standing. Beerus approaches Ymir
   and slashes him with his bear claws. Ymir is defeated and returns back to his amulet. Beerus now approaches you. You have nothing
   left to defend yourself. You've done a great deal, but cannot anymore. From the sky like a soaring eagle flys Solwing, your
   scouting titan. Solwing has felt your distress and dives in like a spiralling spear piercing Beerus and forcing him to return back to his
   amulet. Solwing grabs the ancient artifact and comes to rescue you. You, Solwing, and Ymir have saved the day and protected
   the world. You call your team for a swift retreat, knowing that you have accomplished the task.''')
         break

      elif choice3.lower().strip() == "surrender":
         print('''\n   Unfortunately, to secure your own survival, you decide to surrender and give up your titan Ymir's amulet.
   As you escape you sprint over and steal the ancient artifact. Your teams grabs you at the last second and you all retreat.
   You had to sacrifice Ymir in order to save lives and gain an advantage in the war. You vow to find Ymir again and restore the 
   amulet in its rightful place.''')
         break

      elif choice3.lower().strip() == "settle":
         print('''\n   You realize the predicament that you are in and call for a settlement. You say that General Kaiser can leave with the
   ancient artifact if he leaves you, your titans, yout team, and the village alone. General Kaiser ponders on his response and eventually
   agrees to the conditions. You call your team for a full retreat and summon Ymir back to his amulet. You lost the artifact into
   the wrong hands, but you saved many lives today. The battle is lost, but the war is not. You'll get them next time.''')
         break

      elif choice3.lower().strip() == "retreat":
         print('''\n   You are hit by the realization of this mission and the dangers is holds. You call a full retreat for your entire team.
   The team was not prepared for a rogue frost sniper and needs to regroup. You unfortunately have to give up the ancient artifact and
   the village, but the safety of your team is priority. You are set to report of the rogue agent sighting and suggest more comprehensive
   teams in future in case of any snags. Well done soldier.''')
         break

      elif choice3.lower().strip() == "engage":
         print('''\n   You empower your team and call for them to press forward. The rogue agent strike again and injures one of your frontmen.
   He shoots three more times until you finally spot the flash in the distance and notify your frost snipers. They identify him and set up their frost rifles. 
   You give the execute go-ahead and they snipe. It's a hit! The enemy rogue frost sniper is down. Your team has full control over the battle and
   destroy the evil agent base. You have saved the village from the evil agents. Unfortunately, you lost the ancient artifact, but you
   saved many lives in the village today. Well done soldier.''')
         break

      elif choice3.lower().strip() == "return":
         print('''\n   You have saved the village and the lives of all those people. You regroup your team to pursue General Kaiser back
   at the ruins. You arrive at the ruins and see the evil agents and General Kaiser fleeing in the distance. Although you lost the artifact,
   you saved many important lives today. Even though you lost the battle over the artifact, you have not lost the overall war
   against the evil agents and Pendragon.''')
         break

      elif choice3.lower().strip() == "chase":
         print('''\n   You call your team to execute operation hot pursuit. Your spell casters cunjure sprint spells allowing the entire team
   to gain faster sprint pace. You see the rogue frost sniper running away in the distance. You charge your frost snipers to execute him.
   They lock onto him and wait for your call. You exclaim, "Green Light!" Your frost snipers shoot and hit him directly. The rogue sniper is down.
   You assess the mission. You might not have retrieved the ancient artifact, but you have saved the village and its people and 
   killed the missing rogue frost sniper. You will get General Kasier next time!''')
         break

      else:
         print('  The action you entered in invalid. Please try again.')
         continue

main()

time.sleep(2)

print(f'\n   Thank you for playing the game!')

while (True):
   again = input('\n   Do you want to play again? (yes/no) : ')

   if again.lower().strip() == 'yes':
      main()
      break
   elif again.lower().strip() == 'no':
      print('\n   We hope to see you next time soldier!')
      break
   else:
      print('   The action you entered in invalid. Please try again.')
      continue


   