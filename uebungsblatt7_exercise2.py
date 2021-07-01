import random
import nltk
from nltk.corpus import names
nltk.download('names')

#copied from https://github.com/sukleja/nltk_example/blob/master/main.py
female_names = names.words('female.txt')
male_names = names.words('male.txt')

#randomize names
random.shuffle(female_names)
random.shuffle(male_names)

#---exercise 2---

def char_input():

    # loop until input is valid
    while True:
        # input() automatically returns a string
        char = input("Please enter a single letter: ")
        #make sure its just 1 character
        if len(char) > 1:
            print("Please enter a SINGLE letter!")
        # make sure its a letter
        elif char.isalpha() == False:
            print("Please enter a single LETTER!")
        else:
            break
    return char


def generate_names(char:str):
    print("Hello")


generate_names(char_input())

