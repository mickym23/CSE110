# This line imports or includes the library we will need
from PIL import Image

# Open and set images
penguin_image = Image.open("penguin.jpg")
snow_image = Image.open("snowscape.jpg")
final_image = Image.new("RGB", penguin_image.size)

# Load pxels from images
pixels_penguin = penguin_image.load()
pixels_snow = snow_image.load()
pixels_final = final_image.load()

# Printing RGB values of pixel (1, 1)
print(pixels_penguin[400,400])

for y in range(0, 600):
   for x in range(0, 800):
      # Save background pixels
      r, g, b = pixels_snow[x, y]

      # Fill final image with background
      pixels_final[x, y] = (r, g, b)

      # Save all pengiun pixels
      r, g, b = pixels_penguin[x, y]

      # Save penguin pixels to final image if pixel RGB condition is met
      if not((r <= 80) and (g >= 80) and (g <= 230)):
         pixels_final[x, y] = (r, g, b)

# Saving to output image file
final_image.save("output_file.jpg")

# Open the new file
new_image = Image.open("output_file.jpg")
new_image.show()