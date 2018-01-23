import tweepy
import os
from time import sleep

# Get the authorization keys from the environment (like oxygen)
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# Get an API instance from Tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def tweet(message):
    try:
        print(message)
        api.update_status(message)
    except tweepy.TweepError as e:
        print(e.reason)
    else:
        # Try again in 2 hours
        sleep(1 * 3600)


def main():
    grimm_file = open('grimm_tweets.txt', 'r')
    grimm_lines = grimm_file.readlines()
    grimm_file.close()
    for line in grimm_lines:
        tweet(line.strip())
    print('The end!')
    tweet('The End!')


if __name__ == '__main__':
    main()
