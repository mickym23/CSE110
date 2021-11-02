
# Colors array
colors = ["red", "blue", "green", "yellow"]

print('Colors: ')
for color in colors:
   print(color)

nums = range(1, 9)

print('Numbers 1-8: ')
for num in nums:
   print(num)

num_range = range(2, 21)

print('Even numbers 2-20: ')
for num in num_range:
   while num % 2 == 0:
      print(num)
      break