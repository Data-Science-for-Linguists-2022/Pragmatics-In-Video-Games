# Here, I store the text strings I used to text the regular expressions
# needed for the first question of my exploratory research
import pytest

import spacy
from spacy.matcher import Matcher

import re

# text TEXT USED FOR BOTH REGEX AND SPACY MATCHER
text = """Release me, I command it! I will force you to. We won't let you. We are demanding you to provide a sacrifice! We were demanding it.
We order that you come with us! Order us a burger, will ye? Your goals are to assassinate the meaniehead and curse the witch. 
Your task is to dance your cares away. Your missions was to sink the ship. I am requiring your service. I need you to kill him for me, please.
I needed  your help! I was desiring your assistance. Hail, newcomer! I ask of you this, can you destroy the world for me? If not, I ask you to marry me.
I really don't think it's possible for me to go over there. Are you able to!? Are you able to travel there for me? Are you? 
You should get going, you have a long day ahead. You really need to get this done. You need to. You think so, don't you?
Do you think we can do this? Do not go gentle into that good night! Do you not? Don't touch it, please. Don't you think so? Don't dance? Look, don't you touch that!
Come! Let us feast upon the thoughts of yesteryear, and drink for the new gods! You won't let us talk.
Please, can we just talk? Like we used to. I miss you. Please come back, I miss you! Don't forget me, please. I would like you to kiss him, 
on the lips. We would like to dance!
We would like that you come with us. We would like you. We would like you to sing. May I dance with you? Can you trick the beast? Is it possible to kill him?
Is it possible for you to go over there and teach him a thing or two!?"""

# MATCHER EXPRESSIONS TO text
DO1 = [{"IS_SENT_START": True, "MORPH": "VerbForm=Inf"},
    {"LOWER": {"REGEX": "[a-z]+"}, "OP": "+"},
    {"IS_PUNCT": True}] # 2

DO3 = [{"LEMMA": {"IN": ["I", "we"]}}, 
    {"LEMMA": "be", "MORPH": {"IS_SUPERSET": ["Tense=Pres"]}, "OP":"?"}, 
    {"LOWER": {"REGEX": "^(order|force|demand|command)(ing)?$"}},
    {"LOWER": {"REGEX": "[a-z]+"}, "OP": "+"},
    {"IS_PUNCT": True}] # 3

IO2 = [{"LOWER": "your"},
    {"LEMMA": {"IN": ["objective", "goal", "quest", "task", "mission", "target"]}},
    {"LEMMA": "be", "MORPH": {"IS_SUPERSET": ["Tense=Pres"]}},
    {"LOWER": {"REGEX": "[a-z]+"}, "OP": "+"},
    {"IS_PUNCT": True}] # 2

IO3 = [{"LEMMA": {"IN": ["I", "we"]}},
    {"LEMMA": "be", "MORPH": {"IS_SUPERSET": ["Tense=Pres"]}, "OP":"?"}, 
    {"LOWER": {"REGEX": "^(need|want|require|desire|requir|desir)(ing)?$"}},
    {"LOWER": "that", "OP": "?"},
    {"LEMMA": "you"},
    {"LOWER": {"REGEX": "[a-z]+"}, "OP": "+"},
    {"IS_PUNCT": True}] # 1

DR2 = [{"LEMMA": {"IN": ["I", "we"]}},
    {"LEMMA": "be", "MORPH": {"IS_SUPERSET": ["Tense=Pres"]}, "OP":"?"}, 
    {"LOWER": {"REGEX": "^(request|ask)(ing)?$"}},
    {"LOWER": {"REGEX": "^that|of$"}, "OP": "?"},
    {"LEMMA": "you"},
    {"LOWER": {"REGEX": "[a-z]+"}, "OP": "+"},
    {"IS_PUNCT": True}] # 2

# REGULAR EXPRESSIONS
DO2 = re.compile(r'(?<=[\.!\?,;:]\s)Do(?: not|n\'t(?: you)?)?(?:[^\.!\?]+)?[\.!]', re.I)

IO1 = re.compile(r'\byou (?:really )?(?:(?:need to)|(?:have to)|must|should)(?:[^\.!\?]+)?[\.!]', re.I)
IO4 = re.compile(r'(?<=[\.!\?,;:]\s)Let(?:\'s| us)(?:[^\.!\?]+)?[\.!]', re.I)

DR1 = re.compile(r'(?<=[\.!\?]\s)Please(?:[^\.!\?]+)?[\.!\?]', re.I)

IR1 = re.compile(r'\b(?:I|we) would like(?: that)? you(?:[^\.!\?]+)[\.!]', re.I)
IR2 = re.compile(r'\b(?:May|Would|Can|Could) you(?:[^\.!\?]+)?[\.!\?]', re.I)
IR3 = re.compile(r'\bIs it possible for you to(?:[^\?]+)?\?', re.I)
IR4 = re.compile(r'(\bAre you able to(?:[^\?]+)?\?)', re.I)

# PYTEST SECTION
@pytest.fixture
def setup():

    nlp = spacy.load("en_core_web_trf")

    # Load doc
    doc = nlp(text)

    # Load matcher
    matcher = Matcher(nlp.vocab)

    return [nlp, doc, matcher]

def test_spacy(setup):
    
    setup[2].add("DIRECT ORDERS", [DO1, DO3], greedy="LONGEST")
    assert len(list(setup[2](setup[1]))) == 7

    setup[2].add("INDIRECT ORDERS", [IO2, IO3], greedy="LONGEST")
    assert len(list(setup[2](setup[1]))) == 10

    setup[2].add("DIRECT REQUESTS", [DR2], greedy="LONGEST")
    assert len(list(setup[2](setup[1]))) == 12



def test_re():
    
    assert len(DO2.findall(text)) == 4

    assert len(IO1.findall(text)) == 3
    assert len(IO4.findall(text)) == 1

    assert len(DR1.findall(text)) == 2

    assert len(IR1.findall(text)) == 3
    assert len(IR2.findall(text)) == 2
    assert len(IR3.findall(text)) == 1
    assert len(IR4.findall(text)) == 2