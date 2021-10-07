import os
from collections import defaultdict


class Tweets:
    """
        get tweets database/relationships
    """
    def __init__(self, user_tweets=os.path.join(os.path.split(os.path.abspath(__file__))[0], "data", "tweet.txt")):
        self.user_tweets = user_tweets

    def tweet_data(self) -> dict:
        """read tweet.txt file and return data as object

        :return: object
        """
        _tweets = defaultdict(list)
        count = 0
        with open(self.user_tweets, encoding='utf-8', mode='r') as _data:
            rows = _data.readlines()
            for row in rows:
                user_tweet = row.strip().split(">")
                user, tweet = user_tweet[0].strip(), user_tweet[-1].strip()

                try:
                    if len(tweet) > 140:
                        raise Exception("Tweet characters more than 140")
                    else:
                        _tweets[user].append({count: tweet})
                        count += 1
                except ValueError as e:
                    _ = e

            return _tweets


if __name__ == "__main__":
    tweets = os.path.join('data', 'tweet.txt')
    Tweets().tweet_data()
