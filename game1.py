import random

options = ("rock", "paper", "scissors", "fire", "waterballoon")
playing = True

while playing:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors, fire, waterballoon): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "fire" and computer == "rock":
        print("You win!")
    elif player == "fire" and computer == "paper":
        print("You win!")
    elif player == "fire" and computer == "scissors":
        print("You win!")
    elif player == "waterballoon" and computer == "rock":
        print("You win!")
    elif player == "waterballoon" and computer == "paper":
        print("You win!")
    elif player == "waterballoon" and computer == "scissors":
        print("You win!")
    elif player == "waterballoon" and computer == "fire":
        print("You win!")
    else:
        print("You lose! he he!")

    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Skedaddle!!")
