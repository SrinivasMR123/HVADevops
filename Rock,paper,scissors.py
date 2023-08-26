def determine_winner(player1, player2_):
    if player1 == player2_:
        return "It's a tie!"
    elif (
        (player1 == "rock" and player2== "scissors") or
        (player1 == "scissors" and player2 == "paper") or
        (player1 == "paper" and player2 == "rock")
    ):
        return "congratulations,Player 1 wins! \n Wanna play new game" 
    else:
        return "congratulations,Player 2 wins! \n Wanna play new game"

player1= input("Player 1, enter your choice (rock/paper/scissors): ").lower()
player2 = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

if player1 in ["rock", "paper", "scissors"] and player2 in ["rock", "paper", "scissors"]:
    winner = determine_winner(player1, player2)
    print( winner)
else:
    print("Invalid choice. Please choose from rock, paper, or scissors.")
