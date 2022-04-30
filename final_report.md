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
4. [Analysis](#analysis)
    * [Overview of the Games](#overview-of-the-games)
    * Q1
    * Q2
    * Q3
5. Conclusion
6. Bibiography
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
After reading their paper, I was able to use a couple of their techniques to get the script data from _Hollow Knight_. I was lucky enough to have found an extremely well made [fan-written script](https://docs.google.com/document/d/1oaED7I6xL5NItD-wKyDB455f58d3weLz8OMIkRyEQlo/edit#heading=h.wgd1af4mikjx) containing all of the text from the game. I then used my [`HDialogueParser.py`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/scripts/HDialogueParser.py) script on an HTML version of the file to parse the characters and a dump of their dialogues throughout the game and put them into a dataframe. The section for _Hollow Knight_ in [`initial_data_exploration.ipynb`](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb#Hollow-Knight) is mostly just me doing some quick renaming and adding word counts.
***
## Analysis
### Overview of the Games
Before going through each question in-detail, it’s important to give a brief overview of each game in the dataset, discussing their genre, main themes, and what the data from the game pertains to and how it relates to the game as a whole. In doing this, it’ll be easier to contextualize the data and understand why the results given are the way they are.

First, the biggest dataset is that from _The Elder Scrolls Series_, a series of [single-player role-playing](https://en.wikipedia.org/wiki/Role-playing_game#:~:text=Single-player%20role-playing%20video%20games%20form%20a%20loosely%20defined,,%20settings,%20and%20game%20mechanics.) games where the player takes control of the main character (usually some [prophesied hero](https://elderscrolls.fandom.com/wiki/Last_Dragonborn)) to explore a region of the medieval-style fantasy world [_Tamriel_](https://elderscrolls.fandom.com/wiki/Tamriel). Created by [_Bethesda Softworks_](https://bethesda.net/en/dashboard), the game series first entry, [_Elder Scrolls: Arena_](https://en.wikipedia.org/wiki/The_Elder_Scrolls:_Arena), was published in 1994 and the datasets most recent entry, [_The Elder Scrolls: Online_](https://en.wikipedia.org/wiki/The_Elder_Scrolls_Online), was released in 2014. Note, however, the latest entry is not single-player, but a [massive multiplayer online](https://en.wikipedia.org/wiki/Massively_multiplayer_online_game) game (_MMO_). The data from this game is completely made of [in-game books](https://elderscrolls.fandom.com/wiki/Books_(Oblivion)) which players can read when they come across them throughout each game's [open-world](https://en.wikipedia.org/wiki/Open_world).

The second game in the dataset is _Torchlight II_, another single-player role-playing game where the player completes quests while exploring [randomly generated dungeons](https://en.wikipedia.org/wiki/Random_dungeon). A dungeon is a series of rooms and corridors where the player is pitted against enemies, all in the hope to find items and complete quests. The game was made by [_Runic Games_](https://www.runicgames.com) and released in 2012. This game’s dataset pertains to the quest dialogue given to the player as well as who (or what) said it. Note also that this game has multiple dialogue options at points, meaning that dialogue can change depending on what the player chooses.

The third game is _Star Wars: Knights of the Old Republic_ (which, from now on, will always be abbreviated as _KOTOR_ because I am tired of writing that), a 2003 single-player role-playing game released by [_Bioware_](https://www.bioware.com) and published through [_LucasArts_](https://www.lucasfilm.com/what-we-do/games/). The player plays as [_Revan_](https://en.wikipedia.org/wiki/Revan) and traverses the _Star Wars_ universe during the age of the [_Old Republic_](https://en.wikipedia.org/wiki/Star_Wars:_The_Old_Republic) (set before the prequel trilogy). An interesting note about this game is that said player character has a voice, whereas in other games (e.g. _The Elder Scrolls Series_), the player character does not have a voice, but rather simply displays [what the player character is saying](https://en.wikipedia.org/wiki/Dialogue_tree). This game’s dataset is all the dialogue from the game, including background voicelines. It also contains speaker and listener information as well as comments from the developers.

The last game in the list is _Hollow Knight_, a [Metroidvania](https://en.wikipedia.org/wiki/Metroidvania#:~:text=Metroidvania%20is%20a%20subgenre%20of,genre%20borrowing%20from%20both%20series.)-style game made by [_Team Cherry_](https://www.teamcherry.com.au) and released early 2017. The player controls _The Knight_ as they make their way through its dark fantasy world, the _Kingdom of Hallownest_. Along the way, the player encounters various creatures and NPCs which give text-based dialogue to them. The dataset for this game contains all the dialogue given by all the characters throughout the entire game. Note that this means dialogue is only sorted by who said it and not by when the player meets them. However, there is still a slight chronological ordering regarding which dialogue is said when. For an extremely detailed list of when certain dialogue is said (as well as the complete text of the game), please see the Google Doc.
***
## Bibliography
### Dataset Based On:
van Stegeren, J., & Theune, M. (2020). Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora. In Intelligent Narrative Technologies Workshop. essay, AAAI Press.

### Data Collected From:
Bioware. (2003). Star Wars: Knights of the Old Republic (PC Version) [Video Game]. LucasArts.

Torchlight II (PC Version) [Video Game]. (2012). Runic Games.

The Elder Scrolls I-V and The Elder Scrolls Online (PC Versions) [Video Games]. (1994-2014). Bethesda Softworks.

Hollow Knight (PC Version) [Video Game]. (2017). Team Cherry.

### Additional Resources
Dobrilova, T. (2022, April 26). How much is the gaming industry worth in 2022? [+25 powerful stats]. Techjury. Retrieved April 30, 2022, from https://techjury.net/blog/gaming-industry-worth/ 