########################################
# Name:Aly Chollet
# Collaborators (if any): Sophie, Cordelia
# GenAI Transcript (if any):
# Estimated time spent (hr): 6
# Description of any added extensions:
########################################
from operator import truediv

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    five_letter = ''
    five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
    five_letter += random.choice(five_letter_words)
    def enter_action():
        row = gw.get_current_row()
        guess = get_guess(row)
        get_row(row)
        color_guess(guess, five_letter, row)
        #move row
        row = row + 1
        gw.set_current_row(row)

    def row_move():
        gw.set_current_row(+1)


    def random_five_letter_word(): # I cant seem to call this function anywhere that alows me to use 'five_letter' so i typed the code under wordle()
        five_letter = ''
        five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
        five_letter += random.choice(five_letter_words)
        return five_letter

    def get_row(row):
        value = ""
        for i in range(0, 5):
            coll = i
            gw.get_square_letter(row, coll)
            value += gw.get_square_letter(row, coll)
            value = value.lower()
            #return value
        if value in ENGLISH_WORDS:
            gw.show_message("yay! your word is a word ")
            return value
        else:
            gw.show_message(":< your word is not a word")

    def get_guess(row):
        imput = ""
        for i in range(0, 5):
            col = i
            gw.get_square_letter(row, col)
            imput += gw.get_square_letter(row, col)
            imput = imput.lower()
        return (imput)

    def color_guess(guess, correct, row): # row += 1 so row changes when click enter
        letter_left = correct
        green_list = ""
        for i in range(len(guess)):
            gw.set_square_color(row, i, MISSING_COLOR)
            if guess[i] == correct[i]:
                gw.set_square_color(row, i, CORRECT_COLOR) #set green
                green_list += guess[i]
                letter_left = letter_left.replace(guess[i], "_")
        for i in range(len(guess)):
            if guess[i] in letter_left:
                if guess[i] not in green_list:
                    gw.set_square_color(row, i, PRESENT_COLOR) #color yellow
                    letter_left = letter_left.replace(guess[i], "_")
                elif guess[i] not in green_list:
                    if guess[i] not in letter_left:
                        gw.set_square_color(row, i, MISSING_COLOR) #color grey
        #just for testing
        print(row)
        print(guess)
        print(green_list)
        print(letter_left)
        print(correct)


    def word_from_row(row: int) -> str:
        gw.show_message("To do: row_to_word")
        return ""  # placeholder

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
