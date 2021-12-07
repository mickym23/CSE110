import math

def compute_area_square(value):
   area = value * 4
   return area

def compute_area_rectangle(l, w):
   area = l * w
   return area

def compute_area_circle(r):
   area = math.pi * (r ** 2)
   return area

print()
shape = input('What would you like to compute? (square, rectangle, circle) ')
print()

while True:
   if shape.lower() == 'square':
      square_input = float(input('Please enter the length of one of your square\'s sides: '))
      area = compute_area_square(square_input)
      print()
      print(f'The area of your square is: {area}')
   elif shape.lower() == 'rectangle':
      length = float(input('Please enter the length of one of your rectangle\'s sides: '))
      width = float(input('Please enter the width of one of your rectangle\'s sides: '))
      area = compute_area_rectangle(length, width)
      print()
      print(f'The area of your rectangle is {area}')
   elif shape.lower() == 'circle':
      radius = float(input('Please enter the radius of your circle: '))
      area = compute_area_circle(radius)
      print()
      print(f'the area of your circle is {area}')
   shape = input('What would you like to compute? (square, rectangle, circle) ')