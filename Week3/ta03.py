import math


squareLength = float(input('What is the length of a side of the square? '))
sqArea = squareLength ** 2
print(f'The area of the sqaure is: ' + str(sqArea))
rectLength  = float(input('What is the length of the rectangle? '))
rectWidth  = float(input('What is the width of the rectangle? '))
rectArea = rectLength * rectWidth
print(f'The area of the rectangle is: ' + str(rectArea))
cirRadius = float(input('What is the radius of the circle? '))
cirArea  = math.pi * (cirRadius ** 2)
print(f'The area of the circle is: ' + str(cirArea))
