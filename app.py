import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "You win"
    return "Computer wins"

def play_game():
    user_score = 0
    rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()  # Ensure this line generates a random choice.
        result = determine_winner(user_choice, computer_choice)

        print(f"You chose {user_choice}, computer chose {computer_choice}. {result}")

        if result == "You win":
            user_score += 1

        rounds += 1
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Game over! You won {user_score} out of {rounds} rounds.")
            break

if __name__ == "__main__":
    play_game()
