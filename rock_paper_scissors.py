import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_win_counter = 0
computer_win_counter = 0

play_again = ""

while play_again != "no":
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")
    print(f"You chose: {player_move}")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors
    print(f"The computer chose: {computer_move}")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_win_counter += 1
        print("You win!")
    elif player_move == computer_move:
        print("Draw!")
    else:
        computer_win_counter += 1
        print("You lose!")
    print(f"Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")
    player_decision = input("Type [yes] to Play Again or [no] to Quit: ")
    if player_decision == "yes":
        play_again = "yes"
    elif player_decision == "no":
        play_again = "no"
        print("Thank you for playing!")
    print(f"Final Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")