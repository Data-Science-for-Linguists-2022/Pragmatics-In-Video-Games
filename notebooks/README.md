# Jupyter Notebooks
***
By [Alejandro Ciuba](https://alejandrociuba.github.io), alc307@pitt.edu
***
This subdirectory contains the primary research and exploratory "pokes" of the data via _Jupyter_ notebook files. In particular, the following notebooks can be found:
### Subdirectories:
- `notebook_funcs`: Contains a simple package where I stuff the longer more generalized functions I use in `research.ipynb`.

    **NOTE:** This package can be easily used in any notebook, feel free to use this. Please just give me credit.
- `specific_funcs`: Contains another simple package where the functions used to create text dumps and `Doc` objects are stored.

    **NOTE:** This package is specific to my research and folder structure, use and modify at your own risk.

### Misc. Files:
- `orders_requests.txt`: Full list of orders and requests generated via the `re` regexes and _spaCy's Matcher_.

### Main Files
- `initial_base_data_exploration.ipynb`: Where I take the original data gotten from both my `HDialogueparser.py` script and the [_Video Game Text Corpora_](https://github.com/hmi-utwente/video-game-text-corpora) repository and clean then up for my intended use cases. I also create the data located in [`sample_data`](https://github.com/Data-Science-for-Linguists-2022/Pragmatics-In-Video-Games/tree/main/sample_data) (for the most part).
- `overview.ipynb`: An extremely brief notebook detailing information regarding to each of the games and their respectice dataframes. Some slight modifications to the data were made here (column names).
- `research.ipynb`: This is the main notebook, containing the primary exploratory-focused research I conducted over the Spring 2022 Semester of [Data Science for Linguists](https://github.com/Data-Science-for-Linguists-2022). It is also where I created the `entities.pkl` and `ordreq.pkl` Dataframes. This notebook is also where I also go through all the steps I did more thoroughly and create the documents and tweak the _spaCy_ model's settings.

The following are smaller notebooks containing only the research done from each topic:

- `speech_acts.ipynb`: Contains all my research relating to orders and requests.
- `pronoun_freqs.ipynb`: Contains all my research relating to pronoun frequencies.
- `named_entities.ipynb`: Contains all my research relating to named entities.

***
**NOTE:** For anyone who finds this repository, please tell me what you think via email! This was my first big project which involved both linguistics and computer science. While it may not be much, I am extremely proud of the work I done and I hope I and anyone else interested are able to use what's here to extend what I've research as well as form new research.