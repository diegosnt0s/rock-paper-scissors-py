import game_logic

if __name__ == "__main__":
    
    quit_prompt = False

    while(quit_prompt != True):
        user_input = input("Do you want to play Rock, Paper, Scissors? ")
        user_input = user_input.lower()

        if(user_input in ["yes","y"]):
            game_logic.get_choice()
            
        elif(user_input in ["no","n"]):
            print("Ok, Bye!")
            quit_prompt = True
        else:
            print("Invaild choice, pick either Yes or No.")

    