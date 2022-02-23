# Hollow Knight Dialogue Parser, Dialogue from https://docs.google.com/document/d/1oaED7I6xL5NItD-wKyDB455f58d3weLz8OMIkRyEQlo/edit#heading=h.wgd1af4mikjx
from bs4 import BeautifulSoup
import pandas as pd
import nltk
import bs4

def getCharacters(soup: bs4.BeautifulSoup) -> list:
    characters = [char.string for char in soup.find_all("h2")]
    stop = characters.index('Howling Cliffs') # No more dialogue
    return characters[:stop]

if __name__ == '__main__':

    # OPEN
    print("SCRAPPING DIALOGUE...")
    src = '../private/self-made/HollowKnightCompleteScript.html'

    file = open(src, 'rb')
    soup = BeautifulSoup(file, 'lxml')
    file.close()
    
    # GET CHARACTERS
    chars = getCharacters(soup)
