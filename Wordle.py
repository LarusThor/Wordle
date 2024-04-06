from random import *
class Word:
    def __init__(self, no_guesses, word_length) -> None:
        secret_word = choice(self.word_bank_reader(word_length))
        self.secret_word_dict = self.word_into_dict(secret_word)
        self.word_length = word_length
        self.no_guesses = no_guesses

    def word_bank_reader(self, word_length):
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                i = i.rstrip()
                if len(i) == word_length:
                    word_list.append(i)
        return word_list
    
    def word_into_dict(self, word):
        secret_word_dict = {}
        index = 0
        for letter in word:
            secret_word_dict[index] = letter.lower()
            index += 1

        return secret_word_dict

class Wordle:
    def __init__(self) -> None:
        self.word = None
        
    def format_guess_str(self, word):
        ret_str = ""
        for letter in word:
            ret_str += f"{letter} "
        return ret_str
    
    def valid_guess(self, guess):
        if len(guess) == self.word.word_length and guess.isalpha():
            return True
        return False
    
    def check_guess(self, word):
        guess_word = self.word.word_into_dict(word)
        ret_str = ""
        for index, letter in guess_word.items():    
            if letter in self.word.secret_word_dict.values():
                if self.word.secret_word_dict[index] == letter:
                    ret_str += "C "   
                else:
                    ret_str += "c "      
            else:
                ret_str += "- "
        
        return ret_str

    def word_length_input():
        print("Enter length of word, must be 5, 6 or 7 letters.")
        word_length = int(input("Input word length: "))
        while word_length < 5 or word_length > 7:
            word_length = int(input("Input word length: "))
        return word_length

    def play_game(self):
        
        total_score = 0
        game_input = input("Start new game? (Y/N): ").lower()
        while game_input == "y":
            no_guesses = int(input("Number of guesses: "))
            word_length = self.word_length_input()
            total_score += self.play_round(no_guesses, word_length)
            game_input = input("Start new game? (Y/N): ").lower()
        if word_length is 5:
            with open('scores5.csv', 'a') as scores:
                scores.write(str(total_score) + "\n")
        elif word_length is 6:
            with open('scores6.csv', 'a') as scores:
                scores.write(str(total_score) + "\n")
        elif word_length is 7:
            with open('scores7.csv', 'a') as scores:
                scores.write(str(total_score) + "\n")

    def play_round(self, no_guesses, word_length):
        self.word = Word(no_guesses, word_length)
        print(self.word.secret_word_dict)
        guess_counter = 0
        while guess_counter < self.word.no_guesses:
            print("Take a guess!")
            guess_word = input().lower()
            validity_check = self.valid_guess(guess_word)
            if validity_check:
                guess_counter += 1
                guess = self.check_guess(guess_word)
                print()
                print(self.format_guess_str(guess_word))
                print(guess)
                if guess == "C "* self.word.word_length:
                    print("You won!") 
                    return (self.word.word_length + 1) - guess_counter
            else:
                print()
                print(f"Not a valid guess, word must contain {word_length} letters")
                print()
                
        print("You lost!")
        return
        


wordle = Wordle()

wordle.play_game()

    

