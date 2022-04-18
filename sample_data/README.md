# Sample Data
***
By [Alejandro Ciuba](https://alejandrociuba.github.io), alc307@pitt.edu
***
This subdirectory is free for anyone to use! This sample data contains the following pickled _pandas_ Dataframes:
- `elder_sample.pkl`: Sample of the _TES Books_ Dataframe, containing all entries with less than 50 words.
- `entities.pkl`: A list of named entities from all games as tagged by _spaCy_'s `en_core_web_trf` model.
    **NOTE:** Only a partial list from _KOTOR_ and _TES Books_ due to memory limitations.
- `hollow_sample.pkl`: The complete (kind of garbagely-tagged) script of Hollow Knight character dialogue.
- `kotor_sample.pkl`: The first 5,000 entries of character dialogue from _Star Wars: Knights of the Old Republic_.
- `meta_kotor.pkl`: Complete list of animations that can occur during dialogue in _Star Wars: Knights of the Old Republic_.
- `ordreq.pkl`: Tagged sentences for orders and requests.
    **NOTE:** There exists some inaccuracies in counts.
- `torchlight_sample.pkl`: The first 100 entries from all the quest dialogue of _Torchlight II_.
***
**NOTE:** If you use any of this, please give credit not only to me, but also to Judith Von Stegeren and Mari Theune (cited in the main [`README.md`](https://github.com/Data-Science-for-Linguists-2022/Sociolinguistics-In-Video-Games/blob/main/README.md)).