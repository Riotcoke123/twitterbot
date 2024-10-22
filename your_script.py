import tweepy
import time

# Your Twitter API credentials
API_KEY = ''
API_KEY_SECRET = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Max number of requests allowed per day
MAX_TWEETS_PER_DAY = 50

# Create the client object (v2)
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_KEY_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Track the number of tweets sent
tweet_count = 0
start_time = time.time()

# Function to reset the count after 24 hours
def reset_count():
    global tweet_count, start_time
    elapsed_time = time.time() - start_time
    if elapsed_time >= 24 * 60 * 60:  # 24 hours in seconds
        tweet_count = 0
        start_time = time.time()

# Function to tweet a status update, with rate limiting
def tweet(message):
    global tweet_count
    reset_count()
    if tweet_count < MAX_TWEETS_PER_DAY:
        try:
            client.create_tweet(text=message)  # This uses API v2
            tweet_count += 1
            print(f"Tweeted successfully! ({tweet_count}/{MAX_TWEETS_PER_DAY} tweets used)")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Tweet limit reached. Please wait until the 24-hour limit resets.")

# Example usage:
if __name__ == "__main__":
    # Tweet a message
    tweet("Hello, Twitter! This is a rate-limited bot speaking.")
