import requests
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def get_star_rating(sentiment_score):
    if sentiment_score >= 0.6:
        return 5
    elif sentiment_score >= 0.3:
        return 4
    elif sentiment_score >= 0.1:
        return 3
    elif sentiment_score >= -0.1:
        return 2
    else:
        return 1

url = import requests
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

def get_star_rating(sentiment_score):
    if sentiment_score >= 0.6:
        return 5
    elif sentiment_score >= 0.3:
        return 4
    elif sentiment_score >= 0.1:
        return 3
    elif sentiment_score >= -0.1:
        return 2
    else:
        return 1

url = "https://www.amazon.com/Tekken-3-Pc/dp/B00000K2X5"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text

    review_pattern = re.compile(r'\"reviewText\":\"(.*?)\"')
    reviews = re.findall(review_pattern, html_content)

    if reviews:
        for review in reviews:
            comment = re.sub(r'\\u[0-9A-Fa-f]{4}', '', review).strip()

            sentiment_scores = sid.polarity_scores(comment)
            sentiment_score = sentiment_scores['compound']

            rating = get_star_rating(sentiment_score)

            print(f"Comment: {comment}")
            print(f"Sentiment Score: {sentiment_score}")
            print(f"Star Rating: {rating}/5\n")
    else:
        print("No reviews found using the regex.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    html_content = response.text

    review_pattern = re.compile(r'\"reviewText\":\"(.*?)\"')
    reviews = re.findall(review_pattern, html_content)

    if reviews:
        for review in reviews:
            comment = re.sub(r'\\u[0-9A-Fa-f]{4}', '', review).strip()

            sentiment_scores = sid.polarity_scores(comment)
            sentiment_score = sentiment_scores['compound']

            rating = get_star_rating(sentiment_score)

            print(f"Comment: {comment}")
            print(f"Sentiment Score: {sentiment_score}")
            print(f"Star Rating: {rating}/5\n")
    else:
        print("No reviews found using the regex.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")