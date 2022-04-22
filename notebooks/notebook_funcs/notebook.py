# Useful functions for the notebooks in the notebooks subdirectory
import nltk 

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import re

# ===================== FUNCTIONS =====================
# Makes a boxplot with my overall preferred settings
def barplot(x:list=[], y:list=[], title:str='NO TITLE', xlabel:str='x', ylabel:str='y', xtickrot:float=0.0):

    ax = sns.barplot(x=x, y=y)
    sns.set_style(style='dark')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=xtickrot)
    plt.bar_label(ax.containers[0])    

# Function such that it counts all instances of the given regular expression for each item in a dataframe's specified column
def locator(series: pd.Series, regex:re.Pattern) -> int:
    return np.sum([len(x) for x in series.str.findall(regex)])

# Generator which yields the concordances for a given textual column of a dataframe
# phrase should be a raw string, context cols should be a list of column names
# once_per = only one concordance per textual datapoint (if there is more)
# sides = # of chars to the left and right
# num = number of concordances to display, -1 for all
# Assumes properly formatted text
# If default is false, entire phrase will be treated as the concordance
# highlight will capitalize the find, recommended to turn off for custom regex
def concordances(df:pd.DataFrame, phrase:str or re.Pattern, col:str='text', context_cols: list()=[], sides:int=7, num:int=20, 
                once_per:bool=False, highlight:bool=True):
    
    # Set-up
    context = bool(len(context_cols))
    regex = re.compile(r'((?:[\S]+ ){,' + str(sides) + r'})(\b' + phrase + r'\b)((?:[\S]+)?(?: [\S]+){,' + str(sides) + r'})', re.I) if isinstance(phrase, str) else phrase
    cutoff = 0

    for (ind, concordance_list) in enumerate(df[col].str.findall(regex)):
        
        if len(concordance_list) == 0:
            continue
       
        # Format text if context was stated
        output = ''
        if context:
            cont = df.loc[ind, context_cols]
            output = ' | '.join([col.title() + ": " + cont[col] for col in context_cols]) + " | Concordance:\n\t"

        for concordance in concordance_list:
            
            # Disgusting, I know. It gets the job done for now, but if I use this again, I will try to opt.
            if num != -1:
                cutoff += 1  
                if cutoff > num:
                    return

            if highlight:
                concordance = list(concordance) 
                concordance[1] = concordance[1].upper() # Do it separately due to edge case "your you" -> "YOUr YOU"

            yield output + '...' + ''.join(concordance) + '...'
                
            if once_per:
                break