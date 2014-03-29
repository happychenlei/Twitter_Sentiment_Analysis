


import urllib
import json

response = urllib.urlopen("http://search.twitter.com/search.json?q=Adele")

#print type(response)
dict_info = json.load(response)

results = dict_info["results"]

for i in range(20):
	dict2 = results[i]
	print dict2["text"]



#content = results[0].keys()
#print type(content)




#print dict_info.keys()
#print dict_info.values()

















