from random import *


class Wordle:
    def __init__(self) -> None:
        self.secret_word_dict = self.word_into_dict(choice(self.word_bank_reader()))
        
    def word_into_dict(self, word):
        secret_word_dict = {}
        index = 0
        for letter in word:
            secret_word_dict[index] = letter
            index += 1

        return secret_word_dict


    def word_bank_reader(self):
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                i = i.rstrip()
                word_list.append(i)
        return word_list
    
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
        pass


wordle = Wordle()

print(wordle.secret_word_dict)
print(wordle.check_guess("mrush"))



    

