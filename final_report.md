# Final Report:
***
[Alejandro Ciuba](https://alejandrociuba.github.io), alc307@pitt.edu
***
## Summary
This `final_report.md` file contains in-detail descriptions of the process I went through for getting, cleaning, and exploring the data. As well as where I try to draw conclusions given my findings.
### Table of Contents
1. [Introduction](#introduction)
    * [Opening](#opening)
    * [History of The Repository](#history-of-the-repository)
2. [The Questions](#the-questions)
    * [Why I Selected What I Did](#why-i-selected-what-i-did)
    * [What Conclusions Can I Draw?](#what-conclusions-can-i-draw)
3. [Data-Sourcing & Clean-Up](#data-sourcing--clean-up)
    * [The Original Repository](#the-original-repository)
    * [The Hollow Knight Data](#the-hollow-knight-data)
4. Analysis
    * Overview of the Games
    * Q1
    * Q2
    * Q3
5. Conclusion
***
## Introduction
### Opening
Video game corpora are surprisingly hard to find. For an industry that had a global revenue of over 150 billion dollars in 2019, and with multiple billion dollar companies creating games which are played by millions of people worldwide ([Dobrilova, 2022](https://techjury.net/blog/gaming-industry-worth/)), the linguistic research conducted on the media is extremely sparse, and public linguistic data even more so. It is an artistic medium which is rife with linguistic research waiting to be done. The research in this repository set out to answer these questions:

1. How are orders/requests realized in video game dialogues? 
2. What is the frequency of the 2nd person pronoun, you? 
3. What are some common named entities in video games?

Note that the research ended up being more exploratory and that, while these questions were answered, they were so on a _per-game_ basis and a larger dataset would be necessary to draw conclusions about the medium as a whole. While the research completed in this repository may be small and only focused on a small set of video games, it is still a starting point for what could be more-developed linguistic research in the future—especially for pragmatics. 
### History of The Repository
The repository’s original research was slightly different. In the beginning, I had set out to answer various [sociolinguistic questions](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/aff36d937302643f623fbc6e64fd6d98d0260181/README.md) related to video games; I was particularly interested in the fantasy-race sociolinguistics found in The Elder Scrolls—a game I had in my dataset. However, these questions ended up being too broad for me to answer and I felt like I lacked the proper time and knowledge needed to tackle them adequately. Ultimately, it was _what_ I wanted to research given my data that caused the most headaches, with frequent changes and refinements made to the research questions. Questions were added, dropped, added again, dropped again, and altered during the beginning phases. It was not until I made [`research.ipynb`](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/research.ipynb) that I got a true sense of what I should do and what questions I could/wanted to answer.

While most of the issues lied in what I should answer, there still were slight problems in other departments. For example, I had wanted to examine the use of deixis in video game quest dialogue, but creating a [script](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/scripts/brown_deictic_extractor.py) which could accurately identify such a phenomena was out of my grasp. This question ultimately ended up being dropped in favor of my current question about orders and requests in video games. I thought this would be a better fit because it would be easier to identify false positives in the data. Now it was a question of how to answer it, which I quickly realized was a big issue. While I could turn common order and request phrases into regular expressions using Python’s [`re`](https://docs.python.org/3/library/re.html) package, I quickly discovered, however, that I would need way more linguistic context for some (more on that in the analysis section), which then led me down a rabbit hole learning [_spaCy_](https://spacy.io). Learning _spaCy_ honestly took the biggest chunk of time and also contributed way more to the research than I expected. I cannot say this was a bad thing at all, as I absolutely loved learning it.
***
## The Questions
### Why I Selected What I Did
As previously mentioned, I originally wanted to answer various sociolinguistic questions regarding the video games I had at my disposal. However, these plans changed. With first question:

1. _How are orders/requests realized in video game dialogues?_ 

I wanted to try to examine in what ways do video games drive the player to complete what they want/need them to. For example, if a player needs to go somewhere, how does the game (or the game’s characters) tell the player to head over there? Do they try to frame it in a way that gives the player more adjacency?
	
For the second question:

2. _What is the frequency of the 2nd person pronoun, you?_
I wanted to see how often the game refers to the player. I wanted to also see how often games use other pronouns and if the context of the text affects this.

Lastly, in the third question:
3. _What are some common named entities in video games?_

I wanted to examine what type of named entities are common in the games I had. Do they mention people frequently, what about places? Can these entities be used in more than one context (i.e. toponyms)?
### What Conclusions Can I Draw?
All of my analysis will be done on a _per-game_ basis. This means, while I may compare the games I have between each other, I will not make assumptions on all games or even all games in any given genre. This is mainly because the dataset I am working with is extremely small and (particularly with anything which uses ML models) there are some false positives and false negatives which might slightly bias the data.
***
## Data-Sourcing & Clean-Up
### The Original Repository
I did not obtain most of this data from scratch. In fact, all of the data from _The Elder Scrolls Series_, _Star Wars: Knights of The Old Republic_, and _Torchlight II_ were gotten by [Judith van Stegeren](https://judithvanstegeren.com) for their paper, [_Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora_](https://judithvanstegeren.com/assets/2008-vanstegeren2020fantastic-preprint.pdf), where they explore various ways of obtaining workable video game text corpora.

The data they had gotten from the games was in a really good state. All I had to do was look through each of the dataframes they had made and adapt what was in them, which was all done in [`initial_data_exploration.ipynb`](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb). This mostly involved just reorganizing the columns and dropping unnecessary data, as well as adding word counts to each dataframe. However, I needed to parse the book titles from the URLs in the original [_Elder Scrolls_](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb#The-Elder-Scrolls-Data) data and some columns in the [_Torchlight II_](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb#Torchlight-Data:) and [_Star Wars: Knights of the Old Republic_](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb#Star-Wars:-Knights-of-The-Old-Republic) data frames had to be standardized.
### The Hollow Knight Data
After reading their paper, I was able to use a couple of their techniques to get the script data from _Hollow Knight_. I was lucky enough to have found an extremely well made [fan-written script](https://docs.google.com/document/d/17zFS-WaLwkEw-4UV3ByH2SCmkAjQHHRY5_izHbdKSdI/edit#heading=h.f4w4zmow6unc) containing all of the text from the game. I then used my [`HDialogueParser.py`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/scripts/HDialogueParser.py) script on an HTML version of the file to parse the characters and a dump of their dialogues throughout the game and put them into a dataframe. The section for _Hollow Knight_ in [`initial_data_exploration.ipynb`](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb#Hollow-Knight) is mostly just me doing some quick renaming and adding word counts.
***