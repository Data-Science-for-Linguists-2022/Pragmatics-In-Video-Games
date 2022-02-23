# Hollow Knight Dialogue Parser, Dialogue from https://docs.google.com/document/d/1oaED7I6xL5NItD-wKyDB455f58d3weLz8OMIkRyEQlo/edit#heading=h.wgd1af4mikjx
from io import TextIOWrapper
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import pickle as pkl
import re

def getCharacters(soup: bs4.BeautifulSoup) -> list:
    characters = [char.string for char in soup.find_all("h2")]
    stop = characters.index('Passive Ghosts') # No more dialogue
    return characters[:stop]

def getDialogue(file: TextIOWrapper, pattern: re.Pattern, end: int) -> list:
    dialogue = list()
    section = ""
    try:
        count = 0
        for line in file.readlines():
            if re.match(pattern, line.strip()):
                dialogue.append(section)
                section = ""
                count+=1
            elif count > end:
                return dialogue
            else:
                section += line
            
        file.close()
    except:
        print("SOMETHING WENT WRONG")
    return dialogue

def annon(raw: TextIOWrapper, anno: TextIOWrapper, tag: list=['START', 'END']):
    # Annotate for a dialogue extractor .txt file
    try:
        raw = open('../private/self-made/HollowKnightCompleteScript.txt', 'r')
        anno = open('../private/self-made/HollowKnightCompleteScriptAN.txt', 'w')

        for line in raw.readlines():
            if (formatted := line.strip()) in chars:
                anno.write(tag[0]+formatted+tag[1])
            else:
                anno.write(line)
                anno.write('\n')

        raw.close()
        anno.close()
    except:
        print("SOMETHING WENT WRONG")

if __name__ == '__main__':

    # OPEN
    print("SCRAPPING DIALOGUE...")
    src = '../private/self-made/HollowKnightCompleteScript'

    file = open(src + '.html', 'rb')
    soup = BeautifulSoup(file, 'lxml')
    file.close()
    
    # GET CHARACTERS
    chars = getCharacters(soup)

    # ANNOTATE A DIALOGUE FILE
    annon(open(src + '.txt', 'r'), open(src + 'AN.txt', 'w'), tag=['<character>', '</character>\n'])

    # Now make a dataframe
    hollow_knight_df = pd.DataFrame({"character": chars})

    # Get the dialogue sections from the annotated file
    hollow_knight_df['dialogues'] = getDialogue(open(src + 'AN.txt', 'r'), re.compile(r'<character>.+</character>'), 56)[1:]

    # I don't know why... but the last one is a bit too long
    print(len(hollow_knight_df.loc[55, 'dialogues']))
    hollow_knight_df.loc[55, 'dialogues'] = hollow_knight_df.loc[55, 'dialogues'][:11585]
    
    # IT'S TOO BIG OH GOD OH NO
    # hollow_knight_df.to_pickle('../sample_data/hollow_knight.pkl')

    # Welp...
    hollow_knight_df.to_csv('../private/self-made/hollow_knight.csv')