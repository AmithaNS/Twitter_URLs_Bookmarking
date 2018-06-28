import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from flask import Flask,render_template,request
import sqlite3 as sql
import twitter_bookmark 
#import get_timeline
app=Flask(__name__)               #A flask project
twitter_bookmark.get_timeline()

@app.route('/')                        #home page url
def home():
    return render_template('thome.html') # home page html file

@app.route('/login',methods=['POST','GET']) #trying to login  
def login():
    if request.method=='POST':  #Trying to grant access using all the keys
        try:
            global db,tb
            cs=request.form['cs']
            csk=request.form['csk']
            at=request.form['at']
            atk=request.form['atk']
            consumer_key=cs
            consumer_secret=csk
            access_token=at
            access_secret=atk
            auth=OAuthHandler(consumer_key,consumer_secret)
            auth.set_access_token(access_token,access_secret)
            client=API(auth)
            msg="Access Granted"
        except:
        	msg="Access Failed"
        finally:
            return render_template("result.html",msg=msg)

@app.route('/list') #getting the list of urls
def list():
	con=sql.connect("tweet.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from tweeturl")
	rows=cur.fetchall()
	return render_template('listTweets.html',rows=rows)

if __name__=='__main__':
	app.run(debug=True)