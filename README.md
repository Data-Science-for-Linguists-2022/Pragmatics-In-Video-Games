# Pragmatics-In-Video-Games
***
[Alejandro Ciuba](https://alejandrociuba.github.io), alc307@pitt.edu

February 14, 2022-April 29,2022
***
## Summary
This repository seeks to explore the following avenues on a small sampleset of video game text data:
1. How are orders/requests realized in video game dialogues? Are there more direct or indirect orders?
2. What is the frequency of the 2nd person pronoun, _you_? 
    * Extending that, what are the frequencies of other pronouns?
3. What are some common named entities in video games?
    * Extending this, what are some hapaxes related to named entities?
***
**PLEASE NOTE** I am only publishing a _very small_ sample of any dataset I did not originally make (excluding [`meta_kotor.pkl`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/sample_data/meta_kotor.pkl)); however, I am including full data of any video game texts I parsed myself. If you wish to obtain a full dataset of any samples, please visit the original repository this research is based on, which can be found [here](https://github.com/hmi-utwente/video-game-text-corpora).
***
## Overview
### Main Files
* [**`final_report.md`**](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/final_report.md): The final full-length report where I conclude my exploratory research as well as present the statistics I found.
* [`Pragmatics in Video Games Presentation`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/Pragmatics%20in%20Video%20Games%20-%20Repo%20Copy,%20Alejandro%20Ciuba.pdf): A copy of my original presentation given on April 19, 2022 to my _Data Science for Linguists_ peers and professor, [Dr. Na-Rae Han](https://sites.pitt.edu/~naraehan/).
* [`progress_report.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/progress_report.md) contains status updates on the research and data collected.
* [`data_description.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/data_description.md) succinctly describes and overviews the data. 
* [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/README.md) this, contains general repository information and **necessary** citations should one use research/data from this repository.

### Misc. Files
* [`project_plan.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/project_plan.md) is the repository's initial purpose and highlights a road map of goals, subject to change.
* [`LICENSE.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/LICENSE.md) is this repository's license, `GNU General Public License v3.0`

### Subdirectories
* [`sample_data/`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/sample_data) contains sample datasets used in this research. Any dataset originally made by me is in full, this includes: [`hollow_sample.pkl`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/sample_data/hollow_sample.pkl).
* [`scripts/`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/scripts) contains any full `.py` scripts I made during this research, mostly parsers. Some might not have been used (... or completed...).
* [`notebooks/`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/notebooks) contains any `.ipynb` Jupyter Notebook files I made during this research. As well as two Python packages ([`notebook_funcs`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/notebooks/notebook_funcs) and [`specific_funcs`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/notebooks/specific_funcs)) used throughout the main [`research.ipynb`](https://nbviewer.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/research.ipynb) notebook (a better view of [`research.ipynb`](https://nbviewer.jupyter.org/github/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/research.ipynb))
* [`images/`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/images) contains all graphs made in `matplotlib` during the project. Most graphs are used in the [`final_report.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/final_report.md).
***
Here's what [my fellow classmates](https://github.com/Data-Science-for-Linguists-2022/Class-Lounge/blob/main/guestbooks/guestbook_alejandro.md) said about my project while it was in development!
***
## Citations:
### Dataset Based On:
van Stegeren, J., & Theune, M. (2020). Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora. In Intelligent Narrative Technologies Workshop. essay, AAAI Press.

### Data Collected From:
Bioware. (2003). Star Wars: Knights of the Old Republic (PC Version) [Video Game]. LucasArts.

Torchlight II (PC Version) [Video Game]. (2012). Runic Games.

The Elder Scrolls I-V and The Elder Scrolls Online (PC Versions) [Video Games]. (1994-2014). Bethesda Softworks.

Hollow Knight (PC Version) [Video Game]. (2017). Team Cherry.
