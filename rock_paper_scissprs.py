import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"



player_move = input("Choose [r]ock,  [p]aper or [s]cissors:")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3 + 1)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

if player_move == rock:
    if computer_move == scissors:
        print("You Win!")
    elif computer_move == paper:
        print("You lose!")
    else:
        print("Draw!")
elif player_move == paper:
    if computer_move == scissors:
        print("You lose!")
    elif computer_move == rock:
        print("You Win!")
    else:
        print("Draw!")
elif player_move == scissors:
    if computer_move == rock:
        print("You lose!")
    elif computer_move == paper:
        print("You Win!")
    else:
        print("Draw!")



