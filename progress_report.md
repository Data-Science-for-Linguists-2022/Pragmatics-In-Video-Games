# Progress Report
***
Here is where I highlight and update the progress I make on the project.
***
1. February 14th, 2022:
    I have made the repository, project plan, and started forming a better idea about what I want my project to be.
***
## Progress Report 1:
I have gotten a lot accomplished with this project throughout the last two weeks. First, I was able to get into contact with the original repository's creator directly through email. They helped me a lot with understanding and setting up my repository and they seemed excited about the research I wanted to do with it. I also read their paper [*Fantastic Strings and Where to Find Them: The Quest for High-Quality Video Game Text Corpora*](https://judithvanstegeren.com/assets/2008-vanstegeren2020fantastic-preprint.pdf), an academic paper which highlights how to find and curate good video game text data]. I was actually able to use some of the paper's advice and compile another dataset for myself. Using [this script](https://github.com/Data-Science-for-Linguists-2022/Sociolinguistics-In-Video-Games/blob/main/scripts/HDialogueParser.py) on a fan-made Google Document, I was able to get all the dialogue from another game _Hollow Knight_. I am also currently trying to get even more dialogue from other games that I think can contribute a lot to the research: _Divinity II: Original Sin_ and _The Dishonored Series_. However, I have not gotten the data from them yet as they are stretch goals. I already have plenty of data to accomplish my analysis. After getting the text from _Hollow Knight_, I began to clean the original repository's datasets to be more tailored to what I needed, which can be found [here](https://github.com/Data-Science-for-Linguists-2022/Sociolinguistics-In-Video-Games/blob/main/notebooks/initial_base_data_exploration.ipynb). Lastly, I further developed the questions I want to answer based on what data I had available and how I plan to do it. This can be found in the [data overview](https://github.com/Data-Science-for-Linguists-2022/Sociolinguistics-In-Video-Games/blob/main/notebooks/overview.ipynb).

### Data-Sharing Scheme:
My philosophy was as follows:
    I want to guide those who find this repository to the original repository, while also giving them free access to the data in some form.
With that in-mind, I decided to use the `GNU General Public License v3.0` for three main reasons:

1. I didn't want to hinder anyone from using the research, but I also wanted credit for the research done.
2. I am a massive supporter of free software and FOSS, so seeing that this is what a lot of FOSS uses, I kind of understood what the license entailed.
3. I did not want the license to change between this and repository's based on this one.

Finally, I decided to only release [sample data](https://github.com/Data-Science-for-Linguists-2022/Sociolinguistics-In-Video-Games/tree/main/sample_data) so people interested in the original repository's datasets would be guided there. However, any datasets I make myself will be available, in-full, in the sample data folder (e.g. `hollow_sample.pkl` is a full dataset).
***
## Progress Report 2:
The data acquisition process has been complete; unfortunately, I was not able to obtain the extra data from other games as I had hoped, but I still have plenty of data to begin answering my questions proposed in the `README.md` file. My data has been clean (although I recommend anyone using my _Hollow Knight_ data clean it more if they are not familiar with the game). A brief overview describing the various `.csv`s can be found in `data_description.md`. I begin the analysis of my data in `analysis.ipynb`, which is a continuation of the previous `overview.ipynb` notebook.

### Data-Sharing Scheme:
I did not change from my original plans as stated in the previous progress report. It has been finalized.

### Licensing:
My license and justification of it have not changed since the previous progress report and have been finalized.