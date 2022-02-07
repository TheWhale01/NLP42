import spacy
from re import sub

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

def get_subject(txt) -> list():
	nlp = spacy.load("en_core_web_lg")
	doc = nlp(txt)
	subjs = []
	for ent in doc.ents:
		subjs.append(ent.text)
	return (subjs)

def	hugo(txt :str, dico: dict) -> dict:
	
	doc = nlp(txt)
	for topic in doc.ents:
		if topic.text not in dico.keys():
			dico[topic.text] = [txt]
		else:
			if (txt not in dico[topic.text]):
				dico[topic.text].append(txt)
	return (dico)


if (__name__ == "__main__"):
	dico = {}
	nlp = spacy.load("en_core_web_lg")
	txt = "I'm Joe Biden. Jules is an enormous idiot. Bob. Apple is an amazing compagny. Jules."
	hugo(txt, dico)
	txt = "I'm Spiderman. Jules is an enormous idiot. Bob. Apple is an amazing compagny. Jules."
	hugo(txt, dico)
	# nlp = spacy.load("en_core_web_lg")
	
	# doc = nlp(txt)
	# text_topics = []
	# # [[topic, [strings]], [topic2, [str2]]
	# ret = []
	# for topic in doc.ents:
	# 	if (topic.text not in text_topics):
	# 		top = [topic.text, txt]
	# 		ret.append(top)
	# 		text_topics.append(topic.text)
	print(dico)