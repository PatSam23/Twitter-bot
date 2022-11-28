import tweepy
import time

auth = tweepy.OAuthHandler('XPqpKux56t5MzoTP0hEc4Bpw8', 'oJCpS41awsjMcFXuLcAihLClzzt2pjrbRVabTgSlXNC4Dyl8WY')
auth.set_access_token('1274354405337268224-o8Bwt9ylSzYoywcANJ3n6ujVsZbjRo',
                      'ZtPDMs0o25R59lALU4SSAnP9hT7o2UcmY58kbu1VebifN')

api = tweepy.API(auth)
user = api.me()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)
'''generous bot to follow back everyone'''


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next
    except tweepy.RateLimitError:
        time.sleep(1000)


search_str = 'elon'
numOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_str).items(numOfTweets):
    try:
        tweet.retweet()
        print("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
#
#
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     print(follower.name)    #this isn't giving me the expected output i am having an attribute error for 'name'
