import random
print("Rock paper scissors game in Python")


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

# 1. Rock wins against scissors
# 2. Scissors win against paper
# 3. Paper wins against rock


game_images = [rock, paper, scissors]
user_chioce = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_chioce])
computer_choice = random.randint(0, 2)
print("computer chose:")
print(game_images[computer_choice])
#print(f"computer chose {computer_choice}")

if user_chioce >= 3 or user_chioce < 0:
  print("you typed an invalid number, you lose!")

elif user_chioce == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice == 0 and user_chioce == 2:
    print("you lose")
elif computer_choice > user_chioce:
    print("you lose")
elif user_chioce > computer_choice:
    print("you win!")
elif computer_choice == user_chioce:
    print("Its a draw")

