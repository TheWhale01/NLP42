import spacy
from re import sub
import pandas as pd

def clear_str(txt):
	txt = "".join([i if ord(i) < 128 else ' ' for i in txt])
	txt = txt.lower()
	txt = ' '.join(txt.split())
	txt = sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", txt)
	txt = sub(r"(\s\-\s|-$)", "", txt)
	txt = sub(r"[,\!\?\%\(\)\/\"]", "", txt)
	txt = sub(r"\&\S*\s", "", txt)
	txt = sub(r"\&", "", txt)
	txt = sub(r"\+", "", txt)
	txt = sub(r"\#", "", txt)
	txt = sub(r"\$", "", txt)
	txt = sub(r"\£", "", txt)
	txt = sub(r"\%", "", txt)
	txt = sub(r"\:", "", txt)
	txt = sub(r"\@", "", txt)
	txt = sub(r"\-", "", txt)
	return (txt)

def	store_dict(txt :str, dico: dict) -> dict:
	nlp = spacy.load("en_core_web_lg")
	doc = nlp(txt)
	for topic in doc.ents:
		if topic.text not in dico.keys():
			dico[topic.text] = [txt]
		elif (txt not in dico[topic.text]):
				dico[topic.text].append(txt)
	return (dico)

def get_data() -> dict():
	dico_trump = dict()
	dico_biden = dict()
	df_trump = pd.read_csv("./data/Trump.csv", low_memory=False)
	#df_biden = pd.read_csv("./data/Biden.csv")
	for tweet in df_trump["tweet"]:
		print(tweet)
	#for tweet in df_biden["tweet"]:
	#	dico_biden = store_dict(clear_str(tweet), dico_biden)
	return (dico_trump, dico_biden)

if (__name__ == "__main__"):
	dict_trump, dict_biden = get_data()
	print(dict_trump)