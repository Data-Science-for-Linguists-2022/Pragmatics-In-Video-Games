# Hollow Knight Dialogue Parser, Dialogue from https://docs.google.com/document/d/1oaED7I6xL5NItD-wKyDB455f58d3weLz8OMIkRyEQlo/edit#heading=h.wgd1af4mikjx
from io import TextIOWrapper
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import re

def getSection(soup: bs4.BeautifulSoup, tag: str='h1') -> list:
    section = [char.string for char in soup.find_all(tag)]
    return section

def getDialogue(file: TextIOWrapper, pattern: re.Pattern) -> list:
    dialogue = list()
    section = ""
    try:
        count = 0
        for line in file.readlines():
            if re.match(pattern, line.strip()):
                dialogue.append(section)
                section = ""
                count+=1
            else:
                section += line
        dialogue.append(section)
        file.close()
    except:
        print("SOMETHING WENT WRONG")
    return dialogue

def annon(raw: TextIOWrapper, anno: TextIOWrapper, tag: list=['START', 'END'], applicable: list=['']):
    # Annotate for a dialogue extractor .txt file
    try:
        raw = open('../private/self-made/HollowKnightCompleteScript.txt', 'r')
        anno = open('../private/self-made/HollowKnightCompleteScriptAN.txt', 'w')

        for line in raw.readlines():
            if (formatted := line.strip()) in applicable:
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
    chars = getSection(soup, tag='h2')
    stop = chars.index('Passive Ghosts') # No more dialogue
    chars = chars[:stop]

    # GET DESCRIPTIONS
    desc = getSection(soup, tag='h3')
    stop = desc.index('Other Godseekers') - 1
    desc = desc[:stop]

    for line in desc:
        print(line)

    # ANNOTATE A DIALOGUE FILE
    annon(open(src + '.txt', 'r'), open(src + 'AN.txt', 'w'), tag=['<character>', '</character>\n'], applicable=chars)

    # Now make a dataframe
    hollow_knight_df = pd.DataFrame({"character": chars})

    # Get the dialogue sections from the annotated file
    hollow_knight_df['dialogues'] = getDialogue(open(src + 'AN.txt', 'r'), re.compile(r'<character>.+</character>'))[1:]
    print(hollow_knight_df.sample())
    
    # IT'S TOO BIG OH GOD OH NO
    # hollow_knight_df.to_pickle('../sample_data/hollow_knight.pkl')

    # Welp...
    hollow_knight_df.to_csv('../private/self-made/hollow_knight.csv')