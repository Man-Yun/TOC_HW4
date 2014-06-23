#-*-coding:utf-8-*-
#學號:F74002133 , 姓名:鐘曼芸

import urllib2
import json
import sys

if sys.getdefaultencoding() != 'utf-8' :
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
if len(sys.argv) < 2 :
	print "Error!"
	sys.exit(0)

sourceURL = urllib2.urlopen(sys.argv[1])
data = json.load(sourceURL)

num = 0
max_num = 0
now_road = ""
low_price = 0
max_price = 0
year_month = []
price = []
list_road = []
final_road = []

#get the different road in data
for i in range(len(data)):
	now_road = ""
	if u"大道" in data[i][u"土地區段位置或建物區門牌"] :
		if data[i][u"土地區段位置或建物區門牌"].index(u"大道") != 0 :
			now_road = data[i][u"土地區段位置或建物區門牌"][0:(data[i][u"土地區段位置或建物區門牌"].index(u"大道")+2)] 
	elif u"路" in data[i][u"土地區段位置或建物區門牌"] :
		if data[i][u"土地區段位置或建物區門牌"].index(u"路") != 0 :
			now_road = data[i][u"土地區段位置或建物區門牌"][0:(data[i][u"土地區段位置或建物區門牌"].index(u"路")+1)]
	elif u"街" in data[i][u"土地區段位置或建物區門牌"] :
		if data[i][u"土地區段位置或建物區門牌"].index(u"街") != 0 :
			now_road = data[i][u"土地區段位置或建物區門牌"][0:(data[i][u"土地區段位置或建物區門牌"].index(u"街")+1)] 
	elif u"巷" in data[i][u"土地區段位置或建物區門牌"] :
		if data[i][u"土地區段位置或建物區門牌"].index(u"巷") != 0 :
			now_road = data[i][u"土地區段位置或建物區門牌"][0:(data[i][u"土地區段位置或建物區門牌"].index(u"巷")+1)] 
	# now_road is in the list_road or not
	if now_road not in list_road :
		if now_road != "":
			list_road.append(now_road)
		
#get each road's deal month	
for i in range(len(list_road)):
	for j in range(len(data)):
			if list_road[i] in data[j][u"土地區段位置或建物區門牌"] : 
				if data[j][u"交易年月"] not in year_month :
					year_month.append(data[j][u"交易年月"])
	num = len(year_month)
	if max_num < num :
		final_road = []
		final_road.append(list_road[i])
		max_num = num
	if max_num == num :
		if list_road[i] not in final_road:
			final_road.append(list_road[i])
	year_month = []
	
# get the road's maximum and minimum price
for i in range(len(final_road)):
	for j in range(len(data)):
		if final_road[i] in data[j][u"土地區段位置或建物區門牌"] : 
			price.append(data[j][u"總價元"])
	max_price = max(price)
	low_price = min(price)
	price = []
	print ("%s, 最高成交價: %d, 最低成交價: %d" % (final_road[i], max_price, low_price))
	
