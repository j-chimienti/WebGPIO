import tweepy
from lib.setup import settings

consumer_key = settings['Twitter']['consumer_key']
consumer_secret = settings['Twitter']['consumer_secret']
access_token = settings['Twitter']['access_token']
access_token_secret = settings['Twitter']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(auth)


def send(msg: str):
    return twitter_api.update(msg)


def sendWithMedia(media: str, msg: str):
    return twitter_api.update_with_media(media, msg)
