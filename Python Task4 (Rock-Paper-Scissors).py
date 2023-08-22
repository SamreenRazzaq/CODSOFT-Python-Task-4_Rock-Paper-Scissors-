#ROCK PAPER SCISSORS:

import random

#User Input
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            
#Computer Selection
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#Game Logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"
    
#Display Result
def print_result(user_choice, computer_choice, winner):
    print(f"Your choice: {user_choice.capitalize()}")
    print(f"Computer's choice: {computer_choice.capitalize()}")
    if winner == "tie":
        print("Game tie!")
    elif winner == "user":
        print("Congratulations! You win!")
    else:
        print("Sorry, Computer wins!")

def main():
    print("ROCK, PAPER, SCISSORS GAME")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"Score: You {user_score} - Computer {computer_score}")
        
#Play Again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing this Game!")
            break

if __name__ == "__main__":
    main()
