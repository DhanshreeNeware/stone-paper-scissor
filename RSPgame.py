# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper

import random
Rock = '✊'
paper = '🖐️'
scissor = '✌️'

emoje = [Rock , paper , scissor]

user_action = int(input(f"Enter a choice {emoje} : "))
print(emoje[user_action])

# possible_actions = ["rock", "paper", "scissors"]

computer_action = random.randint(0 ,2)
print(emoje[computer_action])

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == 0:
    if computer_action == 2:
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == 1:
        if computer_action == 2:
            print("scissors cut paper! You lose!")
        else:
            print("Paper covers rock! You win!.")

elif user_action == 2:
    if computer_action == 1:
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")