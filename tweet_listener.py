from tweepy.streaming import StreamListener
from time import sleep
from tweepy import OAuthHandler
from tweepy import Stream
import json

class TweetToFileListener(StreamListener):

    def set_output_file(self, file_name):
        # to clear the content of a file, just open and close it
        open(file_name, 'w').close()

        self.output_file = file_name

    def on_data(self, data):
        print(data)
        with open(self.output_file,'a') as tf:
            tf.write(data)
        return True

    def on_error(self, status):
        print(status)

def get_tweet_stream(output_file, twitter_credentials):
    access_token = twitter_credentials['access_token']
    access_token_secret = twitter_credentials['access_token_secret']
    consumer_key = twitter_credentials['consumer_key']
    consumer_secret = twitter_credentials['consumer_secret']

    l = TweetToFileListener()
    l.set_output_file(output_file)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    return stream

def listen_and_store_tweets(keywords, duration, output_file, twitter_credentials):

    stream = get_tweet_stream(output_file, twitter_credentials)

    stream.filter(track=keywords, is_async=True)
    sleep(duration)
    stream.disconnect()





if __name__ == '__main__':

    access_token = "1056802651440992257-ezrj9wJS8mAs37BfXXYxwPooYrpGrt"
    access_token_secret = "iZyyk4BRNiOjvqO2dGONJ8os7Vq63OK808xvIJaUYHtN7"
    consumer_key = "hdBSuF28Xyd1XfPkPq59fuHFn"
    consumer_secret = "sNElohsvd0nSwhCDN5htK2V8QivDsWR3p12iRovUumNnI0Vfz6"

    tweet_cred = {'access_token': access_token, 'access_token_secret': access_token_secret,
                  'consumer_key': consumer_key, 'consumer_secret': consumer_secret}

    listen_and_store_tweets(['python', 'c++', 'java', 'golang', 'php'], 300, "tweets.json", tweet_cred)
