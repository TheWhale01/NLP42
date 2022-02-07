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

print(clear_str("#cool I love my @Tesla \n    Model Y more é with every update"))
