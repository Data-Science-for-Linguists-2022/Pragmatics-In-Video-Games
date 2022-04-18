# Data Description
***
This file summarizes the data contained in the `.csv` files used in this project.
***
## Video Game Data:
### The Elder Scrolls:
Contains written books from all main-series _Elder Scrolls_ games (_Arena_, _Daggerfall_, _Morrowind_, _Oblivion_, _Skyrim_, _Elder Scrolls Online_) with the following information:

| Column Name | Description |
| ----------- | ----------- |
| `title` | Name of the document in-game |
| `author` | **In-game** author of the document |
| `description` | (Optional, could be empty) A brief summary of the text |
| `game` | Python `List` containing strings, identifying which game(s) the document has appeared in |
| `text` | The actual text, scraped from fan wiki |
| `word_count`| The book's word count (according to `nltk.word_tokenize`). |
| `url` | URL to the scraped webpage |
    
There are:
- 5446 Entries
- 2106 **Unique** Authors (_anonymous_ are counted as 1)
***
### Torchlight II
Contains the quest dialogue from _Torchlight II_ with the following information:

| Column Name | Description |
| ----------- | ----------- |
| `speaker` | Who says/displays the text |
| `text` | Text from quest |
| `word_count`| The text's word count (according to `nltk.word_tokenize`). |
| `dialogtype` | Describes the purpose of the dialogue in-relation to the quest |
| `quest_displayname` | Name of the quest associated with the text as displayed **in-game** |
| `quest_name` | Name of the quest associated with the text as displayed **in-game-engine** (_NON-QUEST_ entries are hooked up to names here)|

There are:
- 1008 Entries
- 9 Dialogue Types
- 84 **Unique** Speakers
***
### Star Wars: Knights of the Old Republic
Abbreviated as _KOTOR_, contains the following information, inside `kotor.pkl`:

| Column Name | Description |
| ----------- | ----------- |
| `speaker` | Speaker of dialogue |
| `listener` | **In-game intended** listener |
| `text` | Transciption of dialogue |
| `word_count`| The text's word count (according to `nltk.word_tokenize`). |
| `animation` | Python `List` describing what animations the character does while saying the dialogue |
| `next` | Python `List` containing the next "chunks" of dialogue (if any) |
| `previous` | Python `List` containing the previous "chunks" of dialogue (if any) |
| `comment` | Comments (if any) left by the developer in any **in-game** files|

Data pertaining to the animations listed in the `animation` column can be found in `meta_kotor.pkl`.

There are:
- 29213 Entries
- 538 **Unique** Speakers
- 152 **Unique** Listeners (Including the _PLAYER_)
- 31 Associated Animation
***
### Hollow Knight
Very simple `.csv`, containing only the following information:

| Column Name | Description |
| ----------- | ----------- |
| `character` | Name of the speaker |
| `text` | Text dump containing **all** dialogue (_partially_ tagged in `.xml` format) from the speaker throughout their various appearances in the game |
| `word_count`| The text's word count (according to `nltk.word_tokenize`). |
    
There are:
- 55 Characters
- Tags Include: `<description>` with their associated end tags
***
***
## Metadata:
### Entities
Another extremely simple `.csv` made via using _spaCy_'s `ner` model to tag entities within the texts, containing only the following information:

| Column Name | Description |
| ----------- | ----------- |
| `entity` | Name of the entity |
| `tag` | `ent.label_` production as given (potential inaccuracies) |
| `source` | Game from which the entity came |

**NOTE:** Only the data from _Hollow Knight_ and _Torchlight_ are from the full text data, _KOTOR_ and _The Elder Scrolls_ were taken as samples due to memory limitations. Tagger accuracy estimated to be around 89% as per [_spaCy_'s website](https://spacy.io/usage/facts-figures#benchmarks).
***
### ordreq.pkl
A `.csv` containing the following regarding various orders and requests capture from my regular expressions and _spaCy's Matcher_:

| Column Name | Description |
| ----------- | ----------- |
| `speech_act_type` | Type of speech act |
| `text` | Text captured |
| `game` | Original game |

**NOTE:** Despite my best efforts, there are false negatives and positives. Although I assume the precision and recall rates are good, there have been no formal tests to prove this. Use at your own discretion.