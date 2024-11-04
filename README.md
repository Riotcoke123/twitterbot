<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
![X_logo](https://github.com/user-attachments/assets/26d061f4-daf3-40a7-b014-633cea139d06)

<img src="https://github.com/user-attachments/assets/26d061f4-daf3-40a7-b014-633cea139d06" alt="X logo" width="200" height="200" />

<h1>Twitter Bot</h1>
<p>
  This project is a simple Twitter bot using <a href="https://www.tweepy.org/">Tweepy</a>, a Python library for accessing the Twitter API.
  The bot can send tweets with a built-in rate limit of up to 50 tweets per 24 hours.
</p>

<h2>Features</h2>
<ul>
  <li>Posts tweets using Twitter API v2.</li>
  <li>Rate-limited to a maximum of 50 tweets per 24-hour period.</li>
  <li>Automatically resets the tweet count after 24 hours.</li>
  <li>Reads tweets from a specified text file, sending each line as a tweet.</li>
</ul>

<h2>New Features</h2>
<ul>
  <li>Ability to read multiple tweets from a text file.</li>
  <li>Each line in the text file is sent as a separate tweet.</li>
</ul>

<h2>Requirements</h2>
<p>To use this bot, you will need:</p>
<ul>
  <li>Python 3.7+ installed.</li>
  <li>Tweepy library (install it using <code>pip install tweepy</code>).</li>
  <li>Twitter API credentials:</li>
  <ul>
    <li>API Key</li>
    <li>API Key Secret</li>
    <li>Bearer Token</li>
    <li>Access Token</li>
    <li>Access Token Secret</li>
  </ul>
</ul>

<h2>Setup</h2>
<ol>
  <li>Clone the repository:</li>
  <pre><code>git clone https://github.com/Riotcoke123/twitterbot.git</code></pre>

  <li>Navigate to the project directory:</li>
  <pre><code>cd twitterbot</code></pre>

  <li>Install required dependencies:</li>
  <pre><code>pip install tweepy</code></pre>

  <li>Fill in your Twitter API credentials in the script:</li>
  <pre><code>API_KEY = 'your_api_key'
API_KEY_SECRET = 'your_api_key_secret'
BEARER_TOKEN = 'your_bearer_token'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'</code></pre>

  <li>Specify the path to your text file with tweets:</li>
  <pre><code>file_path = 'tweets.txt'</code></pre>

  <li>Run the bot:</li>
  <pre><code>python your_script.py</code></pre>
</ol>

<h2>Usage</h2>
<p>To send tweets from a file, ensure your <code>tweets.txt</code> file is formatted with one tweet per line:</p>
<pre><code>Hello, Twitter! This is my first tweet.
Today is a great day to code!
Check out my latest project.</code></pre>
<p>The bot will automatically read and tweet each line in the file.</p>

<h2>Configuration</h2>
<p>You can change the maximum number of tweets per 24-hour period by modifying the <code>MAX_TWEETS_PER_DAY</code> variable in the script:</p>
<pre><code># Max number of requests allowed per day
MAX_TWEETS_PER_DAY = 50</code></pre>

<h2>License</h2>
<p>This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the <a href="LICENSE">LICENSE</a> file for more details.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! Feel free to submit a pull request or open an issue for any bug reports or feature requests.</p>

<h2>Author</h2>
<p>Created by Riotcoke123. You can find more of my work on <a href="https://github.com/Riotcoke123">GitHub</a>.</p>

<h2>Links</h2>
<ul>
  <li><a href="https://github.com/Riotcoke123/twitterbot">GitHub Repository</a></li>
  <li><a href="https://developer.twitter.com/">Twitter Developer Portal</a></li>
</ul>

</body>
</html>

