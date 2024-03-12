from flair.data import Sentence
from flair.models import SequenceTagger
from segtok.segmenter import split_single
import re

def named_entity_extraction(string):
    tagger = SequenceTagger.load("ner-ontonotes")
    sentence = [Sentence(sent, use_tokenizer=True) for sent in split_single(string)]
    tagger.predict(sentence)
    result = {}
    for sent in sentence:
        for entity in sent.get_spans("ner"):
            tag = entity.tag
            if tag == "GPE":
                result["location"] = [entity.text]
            elif tag == "MONEY":
                result["price"] = [int(re.search(r'\d+', entity.text).group())]
            elif tag == "CARDINAL":
                result["num_of_room_availables"] = [1] if entity.text == "one" else [2]
    return result

# print(named_entity_extraction("I want to rent in Mississauga for under 1000 dollars. I prefer a condo with one room available. I have a pet and also I want to park my car."))
# doc = nlp(string) #Tokenize
# entities = []
# for ent in doc.ents:
#     print(ent.label_, ent.text)
#     if ent.label_ in ner_categories.keys():
#         ner_categories[ent.label_].append(ent.text)

# print(ner_categories)
