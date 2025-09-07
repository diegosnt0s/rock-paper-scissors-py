import random

def get_choice():

    move_choices = ["rock","paper","scissors"]
    computer_move = random.choice(move_choices)
    print(computer_move)

    invalid_choice = True

    while(invalid_choice):
        player_choice = input("Pick your move (Rock, Paper, Scissors): ")
        player_choice = player_choice.lower()
    
        if(player_choice in move_choices ):
            print(f"Computer Move: {computer_move}")
            print(f"Player Move: {player_choice}")

            result = get_winner(player_choice,computer_move)

            print(result)
            
            invalid_choice = False
        else:
            print("Invaild choice, choose Rock, Paper, or Scissors.")
    




def get_winner(player_move, computer_move):
    
    # If player picks rock then we will get scissors and if computer pick scissors 
    # then we win, since rock beats scissors

    # Example: 
    # Player = "rock", Computer = "scissors"
    # winning_cases["rock"] → "scissors"
    # "scissors" == "scissors"

    winning_cases = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
    }


    if (player_move == computer_move):
        return "Tie Game!"
    
    elif(winning_cases[player_move] == computer_move):
        return "Player Wins!"
    
    else:
        return "Computer Wins"
