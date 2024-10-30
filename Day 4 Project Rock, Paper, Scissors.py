import random
# Rock Paper Scissors ASCII Art

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Code

game = [Rock, Paper, Scissors]
prompt = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if prompt >=3 or prompt < 0:
    print("You typed an invalid number, you lose!")
else:
    choice = game[(prompt)]
print(f"You chose {choice}")

computer = random.randint(0, 2)
computer_choice = game[computer]
print("Computer chose: ")
print(computer_choice)

#Conditionals
if prompt == computer:
    print("It is a draw")
elif prompt == 0 and computer == 2:
    print("You win")
elif prompt == 2 and computer == 1:
    print("You win")
elif prompt == 1 and computer == 0:
    print("You win")
elif prompt >=3 or prompt < 0:
    print("You typed an invalid number, you lose!")
else:
    print("You lose")

'''
#OR
game_images = [Rock, Paper, Scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

#Conditionals

if user_choice == computer_choice:
    print("It is a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You win!")
else:
    print("You lose")
    '''