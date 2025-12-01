import random
option = ("rock", "paper", "scissors")
running = True

while running:

    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    if player == computer:
        print("It is a tie!")
    elif player == "rock" and computer == "scissors":
        print("YOU WIN!")
    elif player == "paper" and computer == "rock":
        print("YOU WIN!")
    elif player == "scissors" and computer == "paper":
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
    print(f" player:   {player}")
    print(f" computer: {computer}")

    if not input("Play again? (y/n): ").lower() == "y" :
        running = False

print("Thanks for playing!")