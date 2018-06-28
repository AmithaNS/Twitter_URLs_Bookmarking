# Twitter_URLs_Bookmarking
An application which can bookmark all the links in your twitter feed and store in a data base. So that you can login whenever required and check all the links shared on  a particular day.

1. Getting Twitter API keys:
To start with, you will need to have a Twitter account and obtain credentials (i.e. API key, API secret, Access token and Access token secret) on the Twitter developer site to access the Twitter API, following these steps:

Create a Twitter user account if you do not already have one.
Go to https://apps.twitter.com/ and log in with your Twitter user account. This step gives you a Twitter dev account under the same name as your user account.
Click “Create New App”
Fill out the form, agree to the terms, and click “Create your Twitter application”
In the next page, click on “Keys and Access Tokens” tab, and copy your “API key” and “API secret”. Scroll down and click “Create my access token”, and copy your “Access token” and “Access token secret”.

2.After obtaining all the credentials:
Install tweepy using  the command---pip install tweepy (or) py -m pip install tweepy
Then install Flask using the following commands--
•create a virtual environment
  •pip install virtualenv
  •virtualenv flask
  •flask/Scripts/activate
•pip install Flask
•md flaskproject
•cd flaskproject

3.After all the installations:
1)create a python script as "twitter_client.py",this for authorizing your credentials and getting access to the twitter feed.
2)Then create a python script called "twitter_bookmark.py" where you are streaming the timeline feed of the required user(the screen name is passed as commandline argument) and then filter the tweet id,url and creation time and store that into a database.
3)Then create a python file "TwitterBookmark.py" which is the flask app in which the urls for the web pages and their definitions are put.
4)Then create a folder named templates inside flaskproject where we put all the html templates. The "listTweets.html" file is for displaying the list of urls. The "thome.html" is for displaying the homepage.

Command to execute:
(flask) C:\Users\Amitha\flaskproject>py TwitterBookmark.py <provide the required user's screen_name>
Eg:(flask) C:\Users\Amitha\flaskproject>py TwitterBookmark.py AnushkaSharma

Images:

![1](https://user-images.githubusercontent.com/37702827/42020824-a115a1ee-7ad6-11e8-91e9-e31c55f3efcc.PNG)

