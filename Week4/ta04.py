import math

print('\nWelcome to the velocity calculator. Please enter the following:\n')

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = float(input('Time (in seconds): '))
p = float(input('Density of the fluid (inkg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

c = 1/2 * p * A * C

print(f'\nThe inner value of c is: '+"{:.3f}".format(c))

velocity = math.sqrt( (m * g) / c) * (1 - math.exp(((-math.sqrt(m*g*c)/m)*t)))

print(f'The velocity after '+"{:.1f}".format(t)+' seconds is: '+"{:.3f}".format(velocity)+" m/s\n")

t_velocity_guess = float(input('\nWhat is your guess for the terminal velocity? (Accurate to three decimal spaces) '))

t_velocity = math.sqrt((m*g)/c)

if round(t_velocity, 3) == round(t_velocity_guess, 3):
   print(f'\nYou are correct! The terminal velocity is: '+"{:.3f}".format(t_velocity)+"\n")
else:
   print(f'\nUnfortunately you missed it! the terminal velocity is: '+"{:.3f}".format(t_velocity)+"\n")


