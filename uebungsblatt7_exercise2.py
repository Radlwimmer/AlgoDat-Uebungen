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
    #capitalize letter
    return char.upper()


def generate_names(char:str):
    #fill a list with names that start with the right letter (loops through existing list)
    list_female = [name for name in female_names if name[0] == char]
    list_male = [name for name in male_names if name[0] == char]

    #check if list is empty
    if list_female == []:
        print(f"There are no female names starting with {char}")
    #if not, output the first 10 names
    else:
        print(f"Female names starting with {char}:")
        print(list_female[:10])
    if list_male == []:
        print(f"There are no male names starting with {char}")
    else:
        print(f"Male names starting with {char}:")
        print(list_male[:10])


generate_names(char_input())

