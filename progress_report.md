# Progress Report
***
Here is where I highlight and update the progress I make on the project.
***
1. February 14th, 2022:
    I have made the repository, project plan, and started forming a better idea about what I want my project to be.
***
## Progress Report 1:
I have gotten a lot accomplished with this project throughout the last two weeks. First, I was able to get into contact with the original repository's creator directly through email. They helped me a lot with understanding and setting up my repository and they seemed excited about the research I wanted to do with it. I also read their paper [*Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora*](https://judithvanstegeren.com/assets/2008-vanstegeren2020fantastic-preprint.pdf), an academic paper which highlights how to find and curate good video game text data]. I was actually able to use some of the paper's advice and compile another dataset for myself. Using [this script](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/scripts/HDialogueParser.py) on a fan-made Google Document, I was able to get all the dialogue from another game _Hollow Knight_. I am also currently trying to get even more dialogue from other games that I think can contribute a lot to the research: _Divinity II: Original Sin_ and _The Dishonored Series_. However, I have not gotten the data from them yet as they are stretch goals. I already have plenty of data to accomplish my analysis. After getting the text from _Hollow Knight_, I began to clean the original repository's datasets to be more tailored to what I needed, which can be found [here](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb). Lastly, I further developed the questions I want to answer based on what data I had available and how I plan to do it. This can be found in the [data overview](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/overview.ipynb).

### Data-Sharing Scheme:
My philosophy was as follows:
    I want to guide those who find this repository to the original repository, while also giving them free access to the data in some form.
With that in-mind, I decided to use the `GNU General Public License v3.0` for three main reasons:

1. I didn't want to hinder anyone from using the research, but I also wanted credit for the research done.
2. I am a massive supporter of free software and FOSS, so seeing that this is what a lot of FOSS uses, I kind of understood what the license entailed.
3. I did not want the license to change between this and repository's based on this one.

Finally, I decided to only release [sample data](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/sample_data) so people interested in the original repository's datasets would be guided there. However, any datasets I make myself will be available, in-full, in the sample data folder (e.g. `hollow_sample.pkl` is a full dataset).
***
## Progress Report 2:
The data acquisition process has been complete; unfortunately, I was not able to obtain the extra data from other games as I had hoped, but I still have plenty of data to begin answering my questions proposed in the `README.md` file; there, hypothesis regarding my research questions will be displayed and updated throughout the rest of the semester. Please note that `project_plan.md` will no longer be updated as to document the original ideas and outline surrounding this project. All future project updates will be reflected in any future Jupyter Notebooks and the `README.md`.

My data has been clean (although I recommend anyone using my _Hollow Knight_ data clean it more if they are not familiar with the game). A brief overview describing the various `.csv`s can be found in `data_description.md`. I begin the analysis of my data in `analysis.ipynb`, which is a continuation of the previous `overview.ipynb` notebook.

However, in regards to my analysis, I have hit a major road block and I intend to speak to you about these as soon as possible. Firstly, as noted in `analysis.ipynb` under the second hypothesis, there's no readily available list of deictic English words, meaning I am currently trying to create my own (with very little success) with `brown_deictic_extractor.py` whose goal will be to create a set of all the words which were tagged with tags that fall under deixis. 

Looking at my first hypothesis, I have gotten data from _COCA_ (after learning how to properly use the database) that I think could be useful in testing it. `analysis.ipynb` does not reflect what its final state will look like and, as of right now, contains only notes that I believe will assist me in answering these questions.

Overall, this part has been less about the corpus I've collected, and more so gathering the comparative data and statistics I need to compare the corpus to real-world sociolinguistics.

### Data-Sharing Scheme:
I did not change from my original plans as stated in the previous progress report. It has been finalized. I decided to keep it labelled as `sample_data` to make it very clear to anyone that this is not the full dataset, and they should seek out the original repository if they want it.

### Licensing:
My license and justification of it have not changed since the previous progress report and have been finalized.
***
## Progress Report 3:
A lot of progress has been made regarding both the questions I am looking to answer and the research on the data itself. My research questions have pretty much been finalized and one (question 2) has been covered very thoroughly. I am keeping everything in my [`research.ipynb`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/notebooks/research.ipynb) notebook (I renamed it from `analysis.ipynb` because it felt more apt to what I was doing). The notebook itself is properly formatted with section headings and a table of contents to guide the reader to whatever parts might interest them. Question 3 is also underway and is almost complete (the _Hapaxes_ section is not done yet), and I am currently working on the regular expressions needed for question 1. For questions 1 and 3, I have learned the basics of using _spaCy_ to make the identification of certain linguistic attributes (namely named entity and part-of-speech) much easier to work with. My data has been pretty static for the most part, but I did rename the column names for [`hollow_sample.pkl`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/sample_data/hollow_sample.pkl) and added [`entities.pkl`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/sample_data/entities.pkl)([`data_description.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/data_description.md) was also updated to reflect these changes). I also updated the [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/blob/main/README.md) with links to relevant files and directories and added a link to my guestbook!