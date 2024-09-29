########################################
# Name:Aly Chollet
# Collaborators (if any):
# GenAI Transcript (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################
from operator import truediv

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    def enter_action():
        guess = get_row(0)
        color_guess(guess, "glass", 0)

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



    def color_guess(guess, correct, row,): # row += 1 so row changes when click enter
        letter_left = correct
        green_list = ""
        for i in range(len(guess)):
            gw.set_square_color(row, i, MISSING_COLOR)
            if guess[i] == correct[i]:
                gw.set_square_color(row, i, CORRECT_COLOR)
                green_list += guess[i]
                letter_left = letter_left.replace(guess[i], "_")
        for i in range(len(guess)):
            if guess[i] in letter_left:
                if guess[i] not in green_list:
                    gw.set_square_color(row, i, PRESENT_COLOR) #color yellow
                    letter_left = letter_left.replace(guess[i], "_")
                '''elif guess[i] not in green_list:
                    if guess[i] not in letter_left:
                        gw.set_square_color(row, i, MISSING_COLOR)  # color yellow'''
        print(guess)
        print(green_list)
        print(letter_left)



    def col_check(col):
        for i in range(0, 5):
            col = i




        #hih




    def word_to_row(word: str, row: int):
        for i in range(0, 5):
            coll = i
            gw.set_square_letter(0, coll, word[i])




    def word_from_row(row: int) -> str:
        gw.show_message("To do: row_to_word")
        return ""  # placeholder

    #def change_row():


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
