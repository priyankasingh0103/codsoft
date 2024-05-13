import random

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.system_score = 0

    def determine_winner(self, user_choice, system_choice):
        if user_choice == system_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and system_choice == "scissors") or \
             (user_choice == "scissors" and system_choice == "paper") or \
             (user_choice == "paper" and system_choice == "rock"):
            self.user_score += 1
            return "You win!"
        else:
            self.system_score += 1
            return "system wins!"

    def play(self):
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            user_choice = input("Enter your choice: ").lower()

        system_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(user_choice, system_choice)
        print(f"\nYou chose: {user_choice}\nsystem chose: {system_choice}\n{result}")
        print(f"Your Score: {self.user_score}\nsystem Score: {self.system_score}\n")

        # Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            self.play()
        else:
            print("Thanks for playing!")

# Start the game
game = RockPaperScissors()
game.play()
