# Program to convert kilometers into miles 
# Input is provided by the user in kilometers

# take input from the user
kilometers = float(input('How many kilometers?: '))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))
print('This program, kilometers_to_miles.py© is by Vishwanath Mallela.')
print('It has © 2016 - 2020. Do not copy')