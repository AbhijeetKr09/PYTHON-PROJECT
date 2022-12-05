class Brain:
    def __init__(self):
        self.EASY = 10
        self.HARD = 5
        self.lives = 0
    
    def level(self):
        '''
        ask the user for level and then give lives to them accounding to their level
        by default easy = 10
        and hard = 5
        you can change them by calling them as Brain().EASY 
        '''
        difficulty = input("Select the level e for easy, h for hard: ").lower()
        if difficulty == "e":
            self.lives = self.EASY
        else:
            self.lives = self.HARD
        return self.lives
        
    def result(self, user_guess, number):
        if user_guess > number:
            print("Too High.")
            self.lives -= 1
            return self.lives
        elif user_guess < number:
            print("Too Low.")
            self.lives -= 1
            return self.lives
        else:
            print(f"You got it! The answer was {number}.")

