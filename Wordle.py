from random import *

class Wordle:
    def __init__(self) -> None:
        pass

    def display_word(self, word):
        return word
    
    def word_bank_reader(self):
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                word_list.append(i)
        word = choice(word_list)
        return word

wordle = Wordle()

print(wordle.word_bank_reader())
    

