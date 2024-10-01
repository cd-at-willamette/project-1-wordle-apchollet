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
    five_letter = '' #this gives me a 5 letter random word that will = correct
    five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
    five_letter += random.choice(five_letter_words)

    def has_repeating_characters(word):
        return len(set(word)) < len(word)

    NEW_ENGLISH_WORDS = sorted([word for word in ENGLISH_WORDS if not has_repeating_characters(word)])


    def enter_action():
        row = gw.get_current_row()
        guess = get_guess(row)
        if get_row(row): #if word is in the list
            color_guess(guess, five_letter, row)
            row = row + 1 #changes row value
            gw.set_current_row(row) #changes row


    def random_five_letter_word(): # I cant seem to call this function anywhere that alows me to use 'five_letter' so i typed the code under wordle()
        five_letter = ''
        five_letter_words = [word for word in NEW_ENGLISH_WORDS if len(word) == 5]
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
        if value in NEW_ENGLISH_WORDS:
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
        yellow_list = ""
        for i in range(len(guess)):
            gw.set_square_color(row, i, MISSING_COLOR)
            if guess[i] == correct[i]:
                gw.set_square_color(row, i, CORRECT_COLOR) #set green
                green_list += guess[i]
                yellow_list += correct[i]
                for i in range(len(green_list)): #colors the letter green that are in green_list
                    gw.set_key_color(green_list[i], CORRECT_COLOR)
                yellow_list += guess[i]
                letter_left = letter_left.replace(guess[i], "_")
        for i in range(len(guess)):
            if guess[i] in letter_left:
                if guess[i] not in green_list:
                    gw.set_square_color(row, i, PRESENT_COLOR) #color yellow
                    gw.set_key_color(guess[i], PRESENT_COLOR)
                    letter_left = letter_left.replace(guess[i], "_")
                    letter_left = letter_left.replace(guess[i], "_")
                elif guess[i] not in green_list:
                    if guess[i] not in letter_left:
                        gw.set_square_color(row, i, MISSING_COLOR) #color grey

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
