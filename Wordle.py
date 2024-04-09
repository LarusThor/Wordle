MAIN_MENU = """
****************************
Select (H) for Highscore
Select (P) for Play Game
Select (W) to add a new word

Select (q) for quit
****************************
"""

HIGH_SCORE_MENU = """
***********************************************
Select (5) to view Highscore for 5 letter words
Select (6) to view Highscore for 6 letter words
Select (7) to view Highscore for 7 letter words

Select (b) for back
***********************************************
"""

from random import *
class Word:
    def __init__(self, no_guesses, word_length) -> None:
        secret_word = choice(self.word_bank_reader(word_length))
        self.secret_score_dict = self.word_into_dict(secret_word)
        self.word_length = word_length
        self.no_guesses = no_guesses

    def word_bank_reader(self, word_length):
        """ Adds word from wordbank to a list for implementation """
        word_list = []
        with open('wordbank.csv', newline='') as wordbank:
            for i in wordbank:
                i = i.rstrip()
                if len(i) == word_length:
                    word_list.append(i)
        return word_list
    
    def word_into_dict(self, word):
        """ Creates a dictionary for index and letter checking in wordle game """
        secret_score_dict = {}
        index = 0
        for letter in word:
            secret_score_dict[index] = letter.lower()
            index += 1

        return secret_score_dict

class Wordle:
    def __init__(self) -> None:
        self.word = None

    def format_guess_str(self, word):
        """ Corrects format of users guess """
        ret_str = ""
        for letter in word:
            ret_str += f"{letter} "
        return ret_str
    
    def valid_guess(self, guess: str):
        """ Check to see if length of guess word is correct and is only letters """
        if len(guess) == self.word.word_length and guess.isalpha():
            return True
        return False
    
    def check_guess(self, word):
        """ Checks and gives feedback on correctness of users guess """
        guess_word = self.word.word_into_dict(word)
        ret_str = ""
        for index, letter in guess_word.items():    
            if letter in self.word.secret_score_dict.values():
                if self.word.secret_score_dict[index] == letter:
                    ret_str += "C "   
                else:
                    ret_str += "c "      
            else:
                ret_str += "- "
        return ret_str

    def word_length_input(self):
        """ User chooses their word length between 5-7 letters """
        print("Enter length of word, must be 5, 6 or 7 letters.")
        word_length = int(input("Input word length: "))
       
        while word_length < 5 or word_length > 7:
            word_length = int(input("Input word length: "))
        return word_length
    
    def insert_into_scoreboard(self, word_length, score_dict:dict):
        """ Adds new items into scoreboard from a sorted dictionary by values """
        with open(f'scores{word_length}.csv', 'w'):
            pass

        score_list = sorted(score_dict.items(), key=lambda x: x[1], reverse=True)
        with open(f'scores{word_length}.csv', 'a', encoding='utf-8') as scores:
            for (key, item) in score_list:
                scores.write(f'{key}: {str(item)}' + "\n")
    
    def update_scoreboard(self,id, word_length, score):
        """ If scoreboard is full(5) it overwrites the scoreboard with new score
         otherwise it appends it into the scoreboard """
        score_dict = self.check_scoreboard(id, score, word_length)
        if score_dict:
            self.insert_into_scoreboard(word_length, score_dict)
        else:
            with open(f'scores{word_length}.csv', 'a') as scores:
                scores.write(f'{id}: {str(score)}' + "\n")


    def check_scoreboard(self, id, incoming_score, word_length):
        """ Creates a dictionary from the scores in the scoreboard, If length is less than capacity(5)
        returns None otherwise it updates/adds a new score to the scoreboard and removes lowest """
        score_dict = {}
        with open(f'scores{word_length}.csv', newline='') as highscores:
            for score in highscores:
                name, number = score.split(" ")
                name = name[:-1]
                score_dict[name] = int(number)
        
        if len(score_dict) < 5:
            return 
        
        if len(score_dict) == 5:
            if min(score_dict.values()) > incoming_score:
                return
            
        key_to_remove = ""
        for key, value in score_dict.items():
            if value == min(score_dict.values()):
                key_to_remove = key

        score_dict.pop(key_to_remove)
        score_dict[id] = incoming_score
        return score_dict
        
                

    
    def view_highscore(self):
        """Highscore menu, while the user doesn't enter 'b'(for back), it allows the user
        to view the high score for a given table"""
        print(HIGH_SCORE_MENU)
        choice = input()
        while choice != "b".lower() and  "5" <= choice <= "7":
            if choice != "b".lower():
                high_score = (self.high_score_reader(choice))
                print(high_score)

            print(HIGH_SCORE_MENU)
            choice = input()
        return

    def high_score_reader(self, word_length):
        """Takes all the items from the high score table csv file, puts them into a list,
        return a formatted string of all the highscores"""
        score_list = []
        with open(f'scores{word_length}.csv', newline='') as wordbank:
            for i in wordbank:
                score_list.append(i)
        ret_str = ""
        for score in score_list:
            id, number = score.split(" ")
            ret_str += f"ID: {id[:-1]} SCORE: {number}"
        
        return ret_str

    def main_menu(self):
        print(MAIN_MENU)
        choice = input()
        while choice != "q".lower():
            if choice == "h".lower():
                self.view_highscore()
            elif choice == "p".lower():
                self.play_game()
            elif choice == "w".lower():
                self.add_new_word()
            print(MAIN_MENU)
            choice = input()

    def add_new_word(self):
        """Allows the user to enter a word containing between 5 and 7 letters, if the
        word isn't of that length it prompts the user to try again"""

        print("Enter a new word from 5 to 7 letters")
        new_word = input("Enter a valid word: ")
        while len(new_word) > 7 or len(new_word) < 5 or new_word is not new_word.isalpha():
            new_word = input("Enter a valid word: ")
        with open('wordbank.csv', 'a') as wordbank:
            wordbank.write(f"\n{new_word.lower()}")
        return
    
    def id_validation(self):
        """Checks if the id that the user enters contains any spaces"""

        id = input("Enter a ID for the scoreboard: ")
        while " " in id:
            print("Id cant contain spaces")
            id = input("Enter a ID for the scoreboard: ")
        return id

    def play_game(self):
        
        total_score = 0
        word_length = None
        game_input = input("Start new game? (Y/N): ").lower()
        while game_input == "y":
            no_guesses = int(input("Number of guesses: "))
            if word_length is None:
                word_length = self.word_length_input()
            total_score += self.play_round(no_guesses, word_length)
            game_input = input("Start new game? (Y/N): ").lower()

        if total_score > 0:
            id = self.id_validation()
            self.update_scoreboard(id, word_length, total_score)
        return
        

    def play_round(self, no_guesses, word_length):
        """Plays a round of the game, repeatedly allows the user to make a guess
        until he runs out of guesses"""

        self.word = Word(no_guesses, word_length)
        print(self.word.secret_score_dict)
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
                if guess == "C "* (self.word.word_length):
                    print("You won!")
                    return (self.word.word_length + 1) - guess_counter
            else:
                print()
                print(f"Not a valid guess, word must contain {word_length} letters")
                print()
                
        print("You lost!")
        return
        


wordle = Wordle()

wordle.main_menu()

    

