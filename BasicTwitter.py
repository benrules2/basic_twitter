import tweepy
import time

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_key = 'access_key'
access_secret = 'access_secret'

def authorize_account(consumer_key = consumer_key, consumer_secret = consumer_secret,
                        access_key = access_key, access_secret = access_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        return tweepy.API(auth)

def read_messages(twitter_account, since = 1):
    mentions = tweepy.Cursor(twitter_account.mentions_timeline, since_id = str(since)).items()
    tweets = {"messages":[], "since_id":since}

    for tweet in mentions:
        tweets["messages"].append(tweet.text)
        if (tweet.id > tweets['since_id']):
            tweets['since_id'] = tweet.id

    return tweets

if __name__ == "__main__":

    twitter_account = authorize_account()
    since = 1
    
    while(True):  
        try:
            #read all mentions since we last checked
            tweets = read_messages(twitter_account, since)
            since = tweets['since_id']        

            #iterate through messages, updating status
            for message in tweets['messages']:
                twitter_account.update_status(message[::-1])

            #sleep 15 minutes and check again
            time.sleep(60 * 15)   
        except:
            pass 


    
    
        
