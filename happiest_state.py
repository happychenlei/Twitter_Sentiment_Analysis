import sys

#Global Variables
#contentlist = []
dict_state_scores = {}
scores = {}
#outputlist = []


def read_sentiment_scores():
	global scores
	afinnfile = open("AFINN-111.txt")
	
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)
	print len(scores)

def parse_tweet_file(fp):
	tweet_list = fp.readlines()
	print len(tweet_list)
	
	key_text = '"text":"'
	key_source = '"source":"'
	key_lang = ':"en",'
	key_cc = '"country_code":"US"'

	count = 0
	senti_score = 0
	global dict_state_scores
	for index in range(len(tweet_list)):
		str_raw_tweet = tweet_list[index]
		if (str_raw_tweet.find(key_lang) != -1 and str_raw_tweet.find(key_cc) != -1):
			
			str_statename = get_statename(str_raw_tweet)
			
			text_startpos = str_raw_tweet.find(key_text)
			temp_str1 = str_raw_tweet[text_startpos:]
			text_endpos = temp_str1.find(key_source)
			tweet_content = temp_str1[:text_endpos]
			
			senti_score = getsentimentscore(tweet_content)
			
			if (dict_state_scores.has_key(str_statename)):
				senti_score += dict_state_scores.get(str_statename)
				dict_state_scores[str_statename] = senti_score
			else:
				dict_state_scores[str_statename] = senti_score
			#count += 1
	#sort before print
	#sorted(dict_state_scores.items(), key=lambda x: x[1])
	
	for key in sorted(dict_state_scores, key=dict_state_scores.get, reverse=True):
		print key, dict_state_scores[key]

#	print count
#	print tweet_content
#	print len(contentlist)

def get_statename(str_tweet):
	key_city = '"place_type":"city"'
	key_statename = '"full_name":'
	key_countrycode = '"country_code":'	
	statename = ''
	
	if (str_tweet.find(key_city) != -1 and str_tweet.find(key_statename) != -1 
        and str_tweet.find(key_countrycode) != -1):
		fullname_startpos = str_tweet.find(key_statename)
		temp_str1 = str_tweet[fullname_startpos:]
		fullname_endpos = temp_str1.find(key_countrycode)
		raw_statename = temp_str1[:fullname_endpos]
		raw_statename = raw_statename[-4:]
		statename = raw_statename[:2]
	return statename

def getsentimentscore(str_tweet_text):
	global scores
	sentimentscore = 0
	templist = []
	
	templist = str_tweet_text.split(" ")
	for index in range(len(templist)):
		rawkey = templist[index]
		if (scores.has_key(rawkey.lower())):
			sentimentscore += scores.get(rawkey.lower())
	return sentimentscore


def count_sentiment(ListTweets, DictSentiwords):
	global outputlist
	TempList = []
	
	for index in range(len(ListTweets)):
		TempList = ListTweets[index].split(" ")
		sentimentcount = 0
		for index1 in range(len(TempList)):
			rawkey = TempList[index1]
			if (DictSentiwords.has_key(rawkey.lower())):
				#key = TempList[index1]
				sentimentcount += DictSentiwords.get(rawkey.lower())
		stroutput = "sentiment:" + str(sentimentcount)
		outputlist.append(stroutput)
		if (sentimentcount > 0):
			print ListTweets[index]
			print sentimentcount

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    read_sentiment_scores()
    parse_tweet_file(tweet_file)
    #count_sentiment(contentlist, scores)
    

if __name__ == '__main__':
    main()

