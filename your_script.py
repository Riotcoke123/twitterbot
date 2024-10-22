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
            print(f"Tweeted successfully: \"{message}\" ({tweet_count}/{MAX_TWEETS_PER_DAY} tweets used)")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Tweet limit reached. Please wait until the 24-hour limit resets.")

# Function to get the current tweet count
def get_tweet_count():
    return tweet_count

# Function to read messages from a text file
def read_messages_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            messages = file.readlines()
            return [message.strip() for message in messages]  # Strip whitespace and newlines
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Example usage:
if __name__ == "__main__":
    # Specify the path to your text file
    file_path = 'tweets.txt'  # Change this to the path of your text file
    
    # Read messages from the file
    messages = read_messages_from_file(file_path)

    # Loop through each message and tweet it
    for message in messages:
        tweet(message)
        time.sleep(5)  # Optional: sleep for a few seconds between tweets

    # Get the current tweet count
    current_count = get_tweet_count()
    print(f"Total tweets sent in the current 24-hour period: {current_count}")

