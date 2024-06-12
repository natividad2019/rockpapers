print("Rock paper scissors game in Python")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# is determined by 3 simple rules :

#1. Rock wins against scissors
#2. Scissors win against paper
#3. Paper wins against rock


user_chioce = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0, 2)
print(f"computer chose {computer_choice}")
if user_chioce ==  0 and computer_choice == 2:
  print("User wins")
elif computer_choice > user_chioce:
  print("you lose")
else: 
  print("You typed an invalid number, you lose!")
