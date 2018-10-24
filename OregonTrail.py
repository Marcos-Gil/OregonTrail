# By: Marcos Gil

# Introduction screen letting the user know they should buy Supplies
print('=====================')
print('  The Oregon Trail   ')
print('=====================')
print(' ') # Space to make it easier to read

# Asking the user which job they would like followed by if statements to print out what they chose
job = int(input("Which profession would you like to be? \nEnter 1 for a Banker \nEnter 2 for a Carpentor \nEnter 3 for a Farmer\n"))

if job == 1:
	print('\nYou have chosen to be a Banker')
	print(' ')

if job == 2:
	print('\nYou have chosen to be a Carpentor')
	print(' ')
	
if job == 3:
	print('\nYou have chosen to be a Farmer')
	print(' ')

# The user must name themselves and 4 other people on the wagon, then all names are printed back after they have been entered
print('You must now name the 5 pioneers on the wagon.\n ')
namePlayer = input('What will be your name? ')
nameTwo = input('What is the second persons name? ')
nameThree = input('What is the third persons name? ')
nameFour = input('What is the fourth persons name? ')
nameFive = input('What is the fifth persons name? ')
print('\nAwesome! Your name is',namePlayer,'and you have',nameTwo,',',nameThree,',',nameFour,', and',nameFive, 'along with you in the wagon.')

# Letting the user know they should buy Supplies and it's prices
print('\nBefore leaving Independence you should buy equipment and supplies.')
print("You can buy whatever you need at Matt's General Store.")
print(' ')
print('Oxen is $40.00/yoke')
print('Food is $0.20/pound')
print('Clothes is $10/set')
print('Bullets are $2.00/box')
print('Spare parts are $10.00/each')
print('\n===========================')
print("   Matt's General Store    ")
print('===========================')
print(' ') # Space to make it easier to read

# Telling the user each Yoke is $40.00, then asking them how many yokes they want,
# then showing them the total bill so far
yoke = int(input('Oxen costs $40.00 a yoke. How many yoke do you want? '))
print('Bill so far: $%5.2f'%(yoke*40.0))

# Telling the user food  is $0.20/pound, then asking them how many pounds they want,
# Afterwards it shows them the updated total bill so far with yokes + food
food = int(input('Food costs $0.20 a pound. How many pounds do you want? '))
print('Bill so far: $%5.2f'%(yoke*40+food*0.2))

# Telling the user each set of clothes is $10.00, then asking them how many sets they want.
# Afterwards it shows them the updated total bill so far with yokes + food + clothes
clothes = int(input('Clothing costs $10.00 a set. How many sets do you want? '))
print('Bill so far: $%5.2f'%(yoke*40+food*0.2+clothes*10))

# Telling the user a box of bullets is $2.00, then asking them how many boxes they want
# Afterwards it shows them the updated total bill so far with yokes + food + clothes + bullets
bullets = int(input('Bullets cost $2.00 a box. How many boxes do you want? '))
print('Bill so far: $%5.2f'%(yoke*40+food*0.2+clothes*10+bullets*2))

# Telling the user each spare part is $10.00, then asking them how many spare parts they want
# Afterwards it shows them the updated total bill so far with yokes + food + clothes + bullets + spare parts
spareParts = int(input('Spare parts cost $10.00 each. How many spare parts do you want? '))
print('Bill so far: $%5.2f'%(yoke*40+food*0.2+clothes*10+bullets*2+spareParts*10))

# Final output after the user has entered what they would like to buy, the amount spent on
# each item is listed seperately, then added all together at the end to show the total bill with a goodbye message
print(' ') # Space to make it easier to read
print('===========================')
print("   Matt's General Store    ")
print('===========================')
print('1. Oxen          $%5.2f'%(yoke*40))
print('2. Food          $%5.2f'%(food*0.2))
print('3. Clothing      $%5.2f'%(clothes*10))
print('4. Ammunition    $%5.2f'%(bullets*2))
print('5. Spare parts   $%5.2f'%(spareParts*10))
print('===========================')
print('    Total Bill:  $%5.2f'%(yoke*40+food*0.2+clothes*10+bullets*2+spareParts*10))
print(' ')
print('Thanks for shopping, bye!')