temp = float(input(f'What is the temperature? '))
scale = input('Fahrenheit or Celsius (F/C)? ')

def get_wind_chill(temp, wind):
   chill = 35.74 + (0.6215 * temp) - (35.75 * (wind ** 0.16)) + (0.4275 * temp * (wind ** 0.16))
   return chill

while True:
   if scale.lower() == 'f':
      for speed in range(5, 61, 5):
         wind_chill = get_wind_chill(temp, speed)
         print(f'At temperature {round(temp, 2)}F, and wind speed {speed} mph, the windchill is {round(wind_chill, 2)}F')

   if scale.lower() == 'c':
      tempF = (temp * 9/5) + 32
      for speed in range(5, 61, 5):
         wind_chill = get_wind_chill(tempF, speed)
         print(f'At temperature {round(tempF, 2)}F, and wind speed {speed} mph, the windchill is {round(wind_chill, 2)}F')
   temp = float(input(f'\nWhat is the temperature? '))
   scale = input('Fahrenheit or Celsius (F/C)? ')