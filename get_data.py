import pandas as pd
import csv
import googletrans
from googletrans import Translator
# for tweet in data["tweet"]:
# 	print(tweet)

# with open('hashtag_donaldtrump.csv', newline='') as csvfile:
# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
# 	for row in spamreader:
# 		print(', '.join(row))


def ft_get_data() -> list:
	'''
	Retrun a list wich contains 2 dataframe
	one for donald_trump
	second for joe_biden
	'''
	
	countries_to_keep = ["United States of America", "United Kingdom", "Canada", "Australia", "Ireland"]
	trans = Translator()

	print("Chargement du dataset Trump")
	data_D = pd.read_csv("hashtag_donaldtrump.csv",lineterminator='\n')
	data_D = data_D.dropna()
	data_D = data_D.drop(columns=["lat", "long", "source", "state_code", "user_description", "user_join_date", 
								"user_followers_count", "user_name", "user_screen_name", 
								"user_location", "user_name", "collected_at"])
	data_D = data_D.drop(index=data_D.query("country not in @countries_to_keep").index)
	print("Chargement du dataset Biden")
	data_J = pd.read_csv("hashtag_joebiden.csv",lineterminator='\n')
	data_J = data_J.dropna()
	data_J = data_J.drop(columns=["lat", "long", "source", "state_code", "user_description", "user_join_date", 
								"user_followers_count", "user_name", "user_screen_name", 
								"user_location", "user_name", "collected_at"])
	data_J = data_J.drop(index=data_J.query("country not in @countries_to_keep").index)
	return ([data_D, data_J])
		
if __name__ == "__main__":
	# datas = ft_get_data()
	# datas[0].to_csv("Trump.csv")
	# datas[1].to_csv("Biden.csv")
	trump = pd.read_csv("Trump.csv")
	print(trump["tweet"])
