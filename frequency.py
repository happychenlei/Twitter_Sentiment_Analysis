import sys

#Global Variables
tweetwordsdict = {}

#function defination
def parse_tweet_file(fp):
	tweet_list = fp.readlines()
	key1 = '"text":"'
	key2 = '"source":"'
	wordslist = []
	global tweetwordsdict
	for index in range(len(tweet_list)):
		str_rawtweet = tweet_list[index]
		text_startpos = str_rawtweet.find(key1)
		temp_str1 = str_rawtweet[text_startpos:]
		text_endpos = temp_str1.find(key2)
		tweet_content = temp_str1[:text_endpos]
		wordslist = tweet_content.split(" ")
		for index1 in range(len(wordslist)):
			strword = wordslist[index1]
			strwordlow = strword.lower()
			if (tweetwordsdict.has_key(strwordlow) != True):
				tweetwordsdict.update({strwordlow:0})
				#print strwordlow
			else:
				value = tweetwordsdict.get(strwordlow)
				value += 1
				tweetwordsdict.update({strwordlow:value})
#	print len(tweetwordsdict)

def count_freq():
	global tweetwordsdict
	dictcount = len(tweetwordsdict)
	for key in tweetwordsdict:
		value = tweetwordsdict.get(key)
		if (value != 0):
			ffreq = float(value)/dictcount
			print key, "%2.5f" % ffreq

def main():
	tweet_file = open(sys.argv[1])
	parse_tweet_file(tweet_file)
	count_freq()


if __name__ == '__main__':
	main()
