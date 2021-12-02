people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest_age = 9999

youngest_name = ''

for line in people:
   person = line.split(' ')

   name = person[0]
   age = int(person[1])

   if age < youngest_age:
      youngest_age = age

      youngest_name = name

print(f'The youngest person was {youngest_name} who was {youngest_age} years old.')