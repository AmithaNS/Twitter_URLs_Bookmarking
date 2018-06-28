import os
import sys
from tweepy import API
from tweepy import OAuthHandler

def get_twitter_auth():       #getting authorized with the client using tweepy
    try:
        consumer_key='wqnYElEgg35yIS486Nup2azOh'
        consumer_secret='GNhzrNhWXoOUSDt5Hu5wNr32bS3dKYbtmSQsoGLa85lWvtp03r'
        access_token='1011600302473031680-qcLpH3fCBFSYg8WypBMKYyDAhqVhV2'
        access_secret='21vSkTDjV7HFxw6obmlRZ0xKO6muHRyJH7zerRHSN1No7'
        
    except KeyError:
         sys.stderr.write("TWITTER_* environment variables not set\n")
         sys.exit()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    return auth
    
def get_twitter_client():
    auth=get_twitter_auth()
    client=API(auth)
    return client

        