# Functions specifically designed and oriented for my research
import nltk

import pandas as pd

import spacy.language

import os

import notebook_funcs.notebook as nf

# ===================== FUNCTIONS =====================
# Generate the text dumps used for spaCy's nlp pipeline
# Hollowknigh and Torchlight II are in full, KOTOR and TES Books are not
# Those are randomly sampled specificly to work with spaCy's nlp pipeline
def random_sample_texts(es_df:pd.DataFrame, hk_df:pd.DataFrame, kr_df:pd.DataFrame, tl_df:pd.DataFrame, status:bool=False):

    # Create a stream dump of all the text from hollow_knight_df and torchlight_df, save them to two files in my private sub-directory
    # Create random sample .txts from elder_scrolls_df and kotor_df, 1000000 is the max amount of tokens
    # MADE FALSE TO PREVENT ACCIDENTAL FILE CREATION
    if status:
        # I FORMATTED EVERYTHING, I'M NOT REDOING IT
        #with open('../private/text_dumps/hollow_knight.txt', 'w') as src:
            #for text in hollow_knight_df['text']:
                #src.write(text)

        with open('../private/text_dumps/torchlight.txt', 'w') as src:
            for text in tl_df['text']:
                src.write(text)

        with open('../private/text_dumps/elder_scrolls_samp.txt', 'w') as src:

            # I have to curate the elder scrolls data to have sentences with less than 500 tokens
            # Or else I will get indexing errors in the final model
            def approve(text) -> bool:
                for sent in nltk.sent_tokenize(text):
                    if len(nltk.word_tokenize(sent)) > 500:
                        return False
                return True

            es_df['APPROVED'] = es_df['text'].map(approve)
            for text in es_df[es_df['APPROVED'] == True].text.sample(500):
                src.write(text)

            es_df.drop(columns=['APPROVED'])

        with open('../private/text_dumps/kotor_samp.txt', 'w') as src:
            for text in kr_df['text'].sample(500):
                src.write(text)

# create Doc objects for each game, returned as a tuple in the following order
# (elder scrolls, )
def create_docs(nlp:spacy.language, status:bool=False):
    # Create document objects from the texts
    # MEMORY INTENSIVE!!!
    if status:
        docs = []
        FILEPATH = '../private/text_dumps/'
        for file in os.listdir(FILEPATH):
            print(file)
            with open(FILEPATH + file, 'r') as src:
                docs.append(nlp.pipe(src.read(-1)))
                print(type(docs[-1]), len(docs[-1]))

        return (docs[2], docs[0], docs[1], docs[3]) # Have to due this due to how I set up the dataset and dictionary

# Write to the orders_requests.txt file given a bunch of regular expressions for a given game
def write_to_ordreq_regex(ordreq:dict()={}, game:str='NO TITLE', context:list()=[], data:dict()={}, fresh_write:bool=False):

    write_mode = 'w' if fresh_write else 'a'
    with open('orders_requests.txt', write_mode) as src:

        # Write-in Regular Expression Finds
        src.write("=============== ORDER AND REQUESTS FOR " + game + " ===============\n")
        for regex in ordreq:
            src.write('\n\t' + regex + '\n')
            for text in nf.concordances(data[game][0], ordreq[regex], context_cols=context, num=-1, highlight=False):
                src.write(text + '\n')

# Write to the orders_requests.txt file given a bunch of spaCy Matcher Patterns for a given game
def write_to_ordreq_pattern(nlp:spacy.language, matcher:spacy.matcher.Matcher, game:str='NO TITLE', data:dict()={}, fresh_write:bool=False):

    write_mode = 'w' if fresh_write else 'a'
    with open('orders_requests.txt', write_mode) as src:

        # Write-in Matcher Expression Finds
        src.write('\nMATCHER EXPRESSIONS\n')
        
        matches = matcher(data[game][1])
        matches.sort(key=lambda x: x[0])

        sep = 'on_start'
        for (id, start, end) in matches:
            if (sa := nlp.vocab.strings[id]) != sep:
                src.write('\n\t' + sa + '\n')
                sep = sa
            src.write(data[game][1][start:end].text + '\n')