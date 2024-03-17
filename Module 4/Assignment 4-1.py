"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00
# Number of characters.
numChars = 20
# Color of characters.
color = "gold"
# Type of wood.
woodType = "pine"
# Write assignment and if statements here as appropriate.
charge = 35.00
if numChars > 5:
    charge = charge + ((numChars-5) * 4)
if color == "gold":
    charge = charge + 15.0
if woodType == "oak":
    charge = charge + 20.00
# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
