from random import *


class Wordle:
    def __init__(self) -> None:
        self.secret_word_dict = self.word_into_dict(choice(self.word_bank_reader()))
        self.word_length = len(self.secret_word_dict)
        self.num_guesses = self.word_length

    def word_into_dict(self, word):
        secret_word_dict = {}
        index = 0
        for letter in word:
            secret_word_dict[index] = letter.lower()
            index += 1

        return secret_word_dict

    def format_guess_str(self, word):
        ret_str = ""
        for letter in word:
            ret_str += f"{letter} "
        return ret_str
    
    def valid_guess(self, guess):
        if len(guess) == self.word_length and guess.isalpha():
            return True
        return False

    def word_bank_reader(self):
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                i = i.rstrip()
                word_list.append(i)
        return word_list
    
    def format_guess_str(self, word):
        ret_str = ""
        for letter in word:
            ret_str += f"{letter} "
        return ret_str
    
    def check_guess(self, word):
        guess_word = self.word_into_dict(word)
        ret_str = ""
        for index, letter in guess_word.items():    
            if letter in self.secret_word_dict.values():
                if self.secret_word_dict[index] == letter:
                    ret_str += "C "   
                else:
                    ret_str += "c "      
            else:
                ret_str += "- "
        
        return ret_str

    def play_game(self):
        print("Take a guess!")
        guess_word = input().lower()
        guess_counter = 0
        while guess_counter < self.num_guesses:
            validity_check = self.valid_guess(guess_word)
            if validity_check:
                guess = self.check_guess(guess_word)
                print()
                print(self.format_guess_str(guess_word))
                print(guess)
                if guess == "C "* self.word_length:
                    guess_counter += 1
                    print("You won!")
                    return
                else:
                    print("Take a guess!")
                    guess_word = input().lower()
                    guess_counter += 1
            else:
                print("Enter valid guess")
                guess_word = input().lower()
        print("You lost!")
        return

wordle = Wordle()
print(wordle.secret_word_dict)
print(wordle.check_guess("mrush"))



    

