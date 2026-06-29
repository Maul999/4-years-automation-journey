# << Boolean >>

#T = True
#F = False

# Comparasion operators

# == Equal to
# != Not equal to
# < = Less than
# > = Greater than
# <= = less than or equal to
# >= = Greather than or equal to

#Example

E = 25 == 25
# = True
25 == 30
# = False
NE = 25 != 30
# = True
25 != 25
# = False

# The and Operator's truth table
True and True
# = True
True and False
# = False

# The or Operator's truth table
True or True
# = True
True or False
# = True

# The nor operator's truth table
not True
# = False
not False
# = True

#Example if else
usn = "Maul"
pw = "forsaken"
if usn == "Maul":
    print ("Yo whatsupp, Maul!")
if pw == "forsaken":
    print ("That's right.")
else:
    print ("Wrong.")
# = Yo whatsupp, Maul! 
   # That's right. (Why not "Wrong."? Because usn and pw in variabel is True.)

#Example if else again - - -
name = "Maul"
age = 18
if name == "Maul":
    print ("Hi, Maul!")
elif age < 18:
    print ("You're not Maul!")
# = You're not Maul! (Why?? Because age under 18 that's why output is else)

#Exampe convert - - -
# Ask user for the storage unit (TB or GB)
print('Enter TB or GB for the advertised unit:')
unit = input('>')

# Calculate the discrepancy ratio based on the unit chosen
if unit == 'TB' or unit == 'tb' or unit == 'Tb' or unit == "tB":
    discrepancy = 1000000000000 / 1099511627776
    # 1024 ** 4 = 1099511627776
elif unit == 'GB' or unit == 'gb' or unit == 'Gb' or unit == "gB":
    discrepancy = 1000000000 / 1073741824
    # 1024 ** 3 = 1073741824

# Get the factory capacity and convert the string input to float
print('Enter the advertised capacity:')
advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate real capacity, round to 2 decimal places, and convert to string
real_capacity = str(round(advertised_capacity * discrepancy, 2))

# Print the final converted result
print('The actual capacity is ' + real_capacity + ' ' + unit)