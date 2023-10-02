import random

game_free = 1
game_3_out_of_5 = 2
game_6_out_of_10 = 3

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_win_counter = 0
computer_win_counter = 0
games_counter = 0

play_again = ""


print("[1] Free game")
print("[2] 3 out of 5 game")
print("[3] 6 out of 10 game")
game_type = int(input("Please select the type of game: "))
print()

if game_type == game_free:
    print("You've chosen: \"Free game\"")
    print()
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
        print()
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
            games_counter += 1
            print("You win!")
            print()
        elif player_move == computer_move:
            games_counter += 1
            print("Draw!")
            print()
        else:
            computer_win_counter += 1
            games_counter += 1
            print("You lose!")
            print()
        print(f"Games played: {games_counter}")
        print(f"Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")
        print()
        player_decision = input("Type [yes] to Play Again or [no] to Quit: ")
        if player_decision == "yes":
            play_again = "yes"
        elif player_decision == "no":
            play_again = "no"
            print("Thank you for playing!")
        else:
            raise SystemExit("Invalid Input. Try again...")

        print()
    print(f"Final Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")

if game_type == game_3_out_of_5:
    print("You've chosen: \"3 out of 5 game\"")
    print()
    while player_win_counter < 3 or computer_win_counter < 3:
        player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
        if player_move == "r":
            player_move = rock
        elif player_move == "p":
            player_move = paper
        elif player_move == "s":
            player_move = scissors
        else:
            raise SystemExit("Invalid Input. Try again...")
        print()
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
            games_counter += 1
            print("You win!")
            print()
        elif player_move == computer_move:
            games_counter += 1
            print("Draw!")
            print()
        else:
            computer_win_counter += 1
            games_counter += 1
            print("You lose!")
            print()
        print(f"Games played: {games_counter}")
        print(f"Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")
        print()

if game_type == game_6_out_of_10:
    print("You've chosen: \"6 out of 10 game\"")
    print()
    while player_win_counter != 6 or computer_win_counter != 6:
        player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")
        if player_move == "r":
            player_move = rock
        elif player_move == "p":
            player_move = paper
        elif player_move == "s":
            player_move = scissors
        else:
            raise SystemExit("Invalid Input. Try again...")
        print()
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
            games_counter += 1
            print("You win!")
            print()
        elif player_move == computer_move:
            games_counter += 1
            print("Draw!")
            print()
        else:
            computer_win_counter += 1
            games_counter += 1
            print("You lose!")
            print()
        print(f"Games played: {games_counter}")
        print(f"Results: Player: {player_win_counter} W / Computer: {computer_win_counter} W")
        print()

player_win_percentage = player_win_counter / (games_counter / 100)
computer_win_percentage = computer_win_counter / (games_counter / 100)
print(f"You won {player_win_percentage:.2f}% of the games")
print(f"The computer won {computer_win_percentage:.2f}% of the games")