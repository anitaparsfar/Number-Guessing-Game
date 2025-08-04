import random
class Game:
    def __init__(self):
        self.number = random.randint(1,100)
        self.attempts = 0
    def guess(self, player_guess):
        self.attempts += 1
        if player_guess == self.number:
            print(f"Correct answer! number of attempts: {self.attempts}")
            
        elif  player_guess > self.number and player_guess <= 100:
            print(f"too high!Try again")
            
        
        elif player_guess < self.number and player_guess >= 1:
            print(f"too low!Try again")
            
        else:
            print("You can only pick a number between 1 to 100!")
            
    def is_over(self):
        choice = input("would you like to play again? (yes/no) ").strip().lower()
        if choice == "yes":
            self.number = random.randint(1, 100)
            self.attempts = 0
            return True
        else:
            return False
    
def main():
    game = Game()
    print("-------------Welcome to Number Guessing Game-------------")
    while True:
        guess = int(input("Guess a number between 1 to 100: "))
        game.guess(guess)
    
        if guess == game.number:
            if game.is_over():
                game = Game()  
                print("\n--- New game started! ---")
            else:
                break
main()