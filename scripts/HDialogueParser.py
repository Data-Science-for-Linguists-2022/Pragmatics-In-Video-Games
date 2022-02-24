# Hollow Knight Dialogue Parser, Dialogue from https://docs.google.com/document/d/1oaED7I6xL5NItD-wKyDB455f58d3weLz8OMIkRyEQlo/edit#heading=h.wgd1af4mikjx
from collections import defaultdict
from bs4 import BeautifulSoup
import bs4
import pandas as pd
import re

def getSection(soup: bs4.BeautifulSoup, tag: re.Pattern) -> list:
    section = [char.text for char in soup.find_all(tag)]
    return section

def getFromAnnon(filepath: str='FILEPATH', pattern_nest: list() = r'') -> defaultdict:
    main_dict = defaultdict()
    try:
        file = open(filepath, 'r')

        # Jump to tagging section
        line = file.readline()
        while not re.match(pattern_nest[0], line.strip()): line = file.readline()
        
        # We may begin
        fline = ''
        start = True
        text = ''
        while line != '':
            if re.match(pattern_nest[0], line.strip()):
                if start:
                    start = False
                else:
                    main_dict[fline] = text
                    text = ''
                fline = re.sub(pattern_nest[0], r'\1', line.strip())
            else:
                text += line.strip() + '\n'
            line = file.readline()

    except:
        print("SOMETHING WENT WRONG")

    return main_dict
    
def annon(filepath: str='FILEPATH', tag: list=['START', 'END'], applicable: list=['']):
    # Annotate for a dialogue extractor .txt file
    try:
        file = open(filepath, 'r')
        replace = ""
        for line in file:
            if (formatted := line.strip()) in applicable:
                replace += (tag[0]+formatted+tag[1])
            else:
                replace += line.strip()
            replace += '\n'
        file.close()

        file = open(filepath, 'w')
        file.write(replace)
        file.close()
    except:
        print("SOMETHING WENT WRONG")

def pretty(l:list, chunk: int = 3):
    start = 0
    base = chunk
    while start < len(l):
        print(' | '.join(l[start:chunk]))
        start = chunk
        chunk += base

if __name__ == '__main__':

    # OPEN
    print("SCRAPPING DIALOGUE...")
    src = '../private/self-made/HollowKnightCompleteScript'

    file = open(src + '.html', 'rb')
    soup = BeautifulSoup(file, 'lxml')
    file.close()
    
    # GET CHARACTERS
    chars = getSection(soup, tag=re.compile(r'h2'))

    #print("===================== CHARACRTERS =====================")
    #print("NUMBER:", len(chars))
    #pretty(chars, 9)

    # GET DESCRIPTIONS
    desc = getSection(soup, tag=re.compile(r'h[3-6]'))
    #print("===================== SECTIONS =====================")
    #print("NUMBER:", len(desc))
    #pretty(desc, 9)

    # ANNOTATE A DIALOGUE FILE
    annon(src + 'AN.txt', tag=['<character>', '</character>\n'], applicable=chars)
    annon(src + 'AN.txt', tag=['<description>', '</description>\n'], applicable=desc)

    # Get the dialogue sections from the annotated file
    main_dict = getFromAnnon(src + 'AN.txt', [re.compile(r'<character>(.+)</character>')])
    

    # Now make a dataframe
    hollow_knight_df = pd.DataFrame({'characters': main_dict.keys(), 'dialogue': main_dict.values()})
    print(hollow_knight_df.loc[0])
    
    # IT'S TOO BIG OH GOD OH NO
    # hollow_knight_df.to_pickle('../sample_data/hollow_knight.pkl')

    # Welp...
    hollow_knight_df.to_csv('../private/self-made/hollow_knight.csv')