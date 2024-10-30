#Importing the ASCII Art using the print('''....''')
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Using the \ to escape a symbol
point1 = input('You\'re at a crossroad, where do you turn to? "Left" or "Right": \n').lower()
if point1 == "left":
  print("You walk till you get to The Johnson River. What do you do?")
  point2 = input('Type "swim" to swim or "wait for a boat" to wait for a boat.\n').lower()
  if point2 == "wait for a boat":
    print("The boat comes, you get into it, and arrive safely at a beach house with three doors. Which door do you enter")
    point3 = input("Which door do you enter? Red, Blue or Yellow: \n").lower()
    if point3 == "yellow":
      print("The door unlocks and you found the treasure. Congratulations!")
    elif point3 == "red":
      print("It's a room full of fire. Game Over!")
    elif point3 == "blue":
      print("You enter a room of beasts. Game Over!")
    else:
      print("The door doesn't exist. Sorry, Game Over!")
  else:
    print("Ops, unknown to you, there are crocordiles in the river which attacks you. Game Over!")
else:
  print("You walk into a jungle and get lost. Game Over!")