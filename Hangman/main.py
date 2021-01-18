import random
import hangman

class Game:

    def __init__(self):
        self.guesses = []
        self.acceptable_chars = 'ABCDEFGIHJKLMNOPQRSTUVWXYZ'

    def start(self):
        print("+" + "=" * 50 + "+")
        print("|\tWelcome to Hangman Game!\t         |".expandtabs(14))
        print("|The game has 3 levels:(1:Easy,2:Hard,3:Impossible)|")
        print("+" + "=" * 50 + "+")

        self.level = int(input(">>Enter a level: "))
        while True:
            if self.level < 0 or self.level > 3:
                self.level = int(input(">>Give a level between (1:Easy,2:Hard,3:Impossible): "))
            else:
                break

        if self.level == 1:
            self.lifes = 10
        elif self.level == 2:
            self.lifes = 5
        else:
            self.lifes = 3

        with open("words.txt") as f:
            self.word = random.choice(f.readlines()).strip()
        self.guessed_chars = "_" * len(self.word)

    def play(self):
        while True:
            if self.word == self.guessed_chars:
                print("You found the word!")
                break
            elif self.lifes == 0:
                print("Out of tries..")
                print("The word was %s"% self.word)
                break
            
            self.letter = input(">>Enter an english letter: ").upper().strip()
            self.check_letter()
            
            if self.letter in self.guesses:
                print("\nYou tried this letter already!\nTry a different one.")
                continue
            self.guesses.append(self.letter)
            
            if self.letter in self.word:
                for i in range(len(self.word)):
                    if self.letter == self.word[i]:
                        self.guessed_chars = self.guessed_chars[:i] + self.letter + self.guessed_chars[i+1:]
            else:
                self.lifes -= 1
            hangman.hangman(self.lifes,self.level)
            print(f"You guessed:{self.guessed_chars}\n")
            print(f"Lifes left:{hangman.lifes(self.lifes)}\n")

    def check_letter(self):
        while True:
            try:
                if len(self.letter) == 0:
                    self.letter = input(">>Enter a letter in english: ")
                    continue
                elif len(self.letter) > 1:
                    print("You should type only one letter..")
                    print("Try Again!")
                    self.letter = input(">>Enter a letter in english: ")
                    continue
                elif self.letter.upper() not in self.acceptable_chars:
                    print(self.letter in self.acceptable_chars)
                    print(f"{self.letter} is not an english letter..")
                    print("Try Again!")
                    self.letter = input(">>Enter a letter in english: ")
                    continue
                else:
                    break
            except TypeError:
                print("Invalid letter.")
                self.letter = input(">>Enter a letter in english: ")
    
    def restart(self):
        while True:
            choice = input(">>Do you want to play again?(Y/n): ")
            if choice.lower() == 'y':
                self.guesses = []
                self.start()
                self.play()
            else:
                print("Thank you for playing!")
                break

if __name__ == '__main__':
    
    game = Game()
    game.start()
    game.play()
    game.restart()