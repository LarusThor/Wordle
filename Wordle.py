from random import *
from BST import *

class Wordle:
    def __init__(self) -> None:
        pass

    def display_word(self):
        word = choice(self.word_bank_reader())
        secret_word = BSTMap()
        letter_counter = 0
        for key in word:
            secret_word.insert(key, letter_counter)
            letter_counter += 1
        return secret_word


    def word_bank_reader(self):
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                i = i.rstrip()
                word_list.append(i)
        return word_list

wordle = Wordle()

print(wordle.display_word())
    

