import sys

#Global Variables
contentlist = []
scores = {}
outputlist = []

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def read_sentiment_scores():
	global scores
	afinnfile = open("AFINN-111.txt")
	
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)
#	print scores.items()	

def parse_tweet_file(fp):
	tweet_list = fp.readlines()
	key1 = '"text":"'
	key2 = '"source":"'
	key3 = ':"en",'
	count = 0
	global contentlist
	for index in range(len(tweet_list)):
		str_raw_tweet = tweet_list[index]
		if (str_raw_tweet.find(key3) != -1):
			text_startpos = str_raw_tweet.find(key1)
			temp_str1 = str_raw_tweet[text_startpos:]
			text_endpos = temp_str1.find(key2)
			tweet_content = temp_str1[:text_endpos]
			contentlist.append(tweet_content)
		else:
			count += 1
#	print count
#	print tweet_content
#	print len(contentlist)

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
#    lines(sent_file)
#    lines(tweet_file)
    read_sentiment_scores()
    parse_tweet_file(tweet_file)
    count_sentiment(contentlist, scores)
    

if __name__ == '__main__':
    main()
