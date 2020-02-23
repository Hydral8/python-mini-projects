import nltk
import random

nltk.download()
# def playGame():


def genRandomWord():
    print(words.words[:10])
    string = words[random.randint(0, len(words) - 1)]
    return string


genRandomWord()
