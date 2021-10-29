# This line imports or includes the library we will need
from PIL import Image

# This line opens the image and loads it into a variable called "image_original"
image_original = Image.open("beach.jpg")

# This line attempts to open a new window to display the image.
image_original.show()

width, height = image_original.size

print(width, height)


pixels_original = image_original.load()

print(pixels_original[1,1])

r, g, b = pixels_original[100, 200]
print(f'Pixel #1: ', r, g, b)

r, g, b = pixels_original[120, 500]
print(f'Pixel #2: ', r, g, b)

r, g, b = pixels_original[799, 400]
print(f'Pixel #3: ', r, g, b)

r, g, b = pixels_original[20, 500]
print(f'Pixel #4: ', r, g, b)

r, g, b = pixels_original[100, 200]
print(f'Pixel #5: ', r, g, b)

# Don't forget to use parentheses around your (r, g, b)
pixels_original[100, 200] = (0, 0, 0)
pixels_original[100, 201] = (0, 0, 0)
pixels_original[100, 202] = (0, 0, 0)
pixels_original[100, 203] = (0, 0, 0)
pixels_original[100, 204] = (0, 0, 0)

image_original.save("output_file.jpg")