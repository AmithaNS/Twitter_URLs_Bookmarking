import json
import sqlite3
from tweepy import Cursor
from twitter_client import get_twitter_client
import re
import sys

def get_timeline():
	user = sys.argv[1]
	client=get_twitter_client()
	m=re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

	#Storing some of the recent tweets into a file in json format

	fname="user_timeline_{}.json1".format(user)
	with open(fname,'w') as f:
		for page in Cursor(client.user_timeline, screen_name=user, count=50).pages(4):
			for status in page:
				f.write(json.dumps(status._json)+"\n")
	f.close()
	with sqlite3.connect("tweet.db")as con:
		cur=con.cursor()
		cur.execute("DROP TABLE tweeturl")
		cur.execute("CREATE TABLE tweeturl(tid INT PRIMARY KEY NOT NULL,url TEXT NOT NULL,created_at TEXT)")
		con.commit()
		#con.close()
	tweets_file = open(fname, "r")
	for line in tweets_file:           #opening the above file accessing the required data like tweet id,tweet url and tweet time into the database
		try:
			tweet = json.loads(line.strip())
			if 'text' in tweet:
			    u=tweet['user']['id']
			    print(u) 
			    i=tweet['id']
			    #print(i) 
			    t=tweet['created_at']
			    #print(t) 
			    p=m.findall(tweet['text'])
			    #print(p)
			    try:
			    	with sqlite3.connect("tweet.db")as con:
			    		cur=con.cursor()
			    		cur.execute("INSERT INTO tweeturl(tid,url,created_at)VALUES(?,?,?)",(i,p[0],t))
			    		con.commit()
			    		print("Record successfully added")
			    except:
			    	con.rollback()
			    	print("error in insert operation")
			    	con.close()
		except:
			continue
