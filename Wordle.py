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
        # What should happen when RETURN/ENTER is pressed.
        get_row()

    def get_row():
        value = ""
        for i in range(0, 5):
            coll = i
            gw.get_square_letter(0, coll)
            value += gw.get_square_letter(0, coll)
            value = value.lower()
        if value in ENGLISH_WORDS:
            gw.show_message("yay! your word is a word ")
        else:
            gw.show_message(":< your word is not a word")

    def word_to_row(word: str, row: int):
        for i in range(0, 5):
            coll = i
            gw.set_square_letter(0, coll, word[i])

    def word_from_row(row: int) -> str:
        gw.show_message("To do: row_to_word")
        return ""  # placeholder


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
