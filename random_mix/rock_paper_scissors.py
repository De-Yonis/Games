import random

def play_game():
    print("Can you beat a computer!")
    user_choice = (input("Choose wisely,'r' for rock, 'p' for paper, 's' for scissors: ").lower())
    computer_choice = random.choice(['r','p','s'])
    


    if user_choice == computer_choice:
        print(f"It's a Tie, the computer also choice {computer_choice}")
    
    if is_win(user_choice, computer_choice):
        print(f"{user_choice} beat {computer_choice}, Great Job, You have defeated the computer!!!")

    else:
        print(f"Hahahaaa, You have lost, {computer_choice} beat {user_choice}")


def is_win(player, opponent):
    #returns true if player wins
    if(player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

play_game()