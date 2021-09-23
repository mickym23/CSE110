# BYUI-I Course: CSE110
# Author: Mikhail Cedras

# Input: User Details
# Process: Format strings according to desired format
# Output: Complete formatted form

first_name = input('Please enter your firstname: ')
last_name = input('Please enter your lastname: ')
email = input('Please enter your email address: ')
phoneNum = input('Please enter your phone number: ')
jobTitle = input('Please enter your job title: ')
idNum = input('Please enter your ID number: ')
hairColor = input('Please enter your hair color: ')
eyeColor = input('Please enter your eye color: ')

print('------------------------------')
print(last_name.upper(), ', ', first_name.capitalize())
print(jobTitle.title())
print(idNum, '\n')
print(email.lower())
print(phoneNum, '\n')
print('Hair: ', hairColor, '\t', 'Eyes: ', eyeColor )
print('------------------------------')
