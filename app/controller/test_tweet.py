import os
import re
import unittest


class TestTweet(unittest.TestCase):
    tweet_file = os.path.join(os.path.split(os.path.abspath(__file__))[0], "data", "tweet.txt")

    def test_file_extension(self):
        self.assertEqual('tweet.txt', os.path.split(TestTweet.tweet_file)[-1])

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(TestTweet.tweet_file), f"{TestTweet.tweet_file} does not exists")

    def test_file_readable(self):
        self.assertTrue(os.access(TestTweet.tweet_file, os.R_OK), f"{TestTweet.tweet_file} is not readable")

    def test_file_size(self):
        self.assertNotEqual(0, os.stat(TestTweet.tweet_file).st_size, "File is empty")

    def test_delimiters_name_format(self):
        with open(TestTweet.tweet_file, 'r') as data_user_txt:
            rows = data_user_txt.readlines()
            for row in rows:
                self.assertIn(">", row, "Wrong delimiter found instead of >")
                get = row.split(">")
                name, tweet = get[0].strip(), get[-1].strip()
                self.assertTrue(bool(re.findall("^[A-Z]{1}", name)), "check name format {}".format(name))
                self.assertLessEqual(len(tweet.strip()), 140, f"{tweet} Tweet characters greater than 140.")


if __name__ == '__main__':
    unittest.main()
