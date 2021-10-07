import itertools
from .controller import (User, Tweets)


class ConsoleApp:
    def __init__(self, user_graph: dict, tweets_graph: dict):
        """

        :param user_graph: dictionary
        :param tweets_graph: dictionary
        """
        self.user_graph = user_graph
        self.tweets_graph = tweets_graph

        # flatten the user_graph/tree to a list of all chronological users in the database (user.txt)
        self.users = sorted(
            list(
                set(
                    itertools.chain(
                        *[list(set(follows + [user])) for user, follows in self.user_graph.items()]
                    )
                )
            )
        )

    def __repr__(self):
        return "user graph({})\ntweet graph({})".format(self.user_graph, self.tweets_graph)

    def console(self):
        """sort algorithm

        outputs tweets according to chronological order of user graph object
        """
        if self.users:
            for user in self.users:
                self.conversation_sort(user_graph=self.user_graph, tweets_graph=self.tweets_graph, search_name=user)
        else:
            raise Exception("File is empty")

    @staticmethod
    def conversation_sort(user_graph: dict, tweets_graph: dict, search_name: str):
        """

        :param user_graph: network representation of users relationship
        :param tweets_graph: network representation of users' tweets in order labeled by an index value
        :param search_name: search users iteratively/sequentially
        :return: None
        """

        def conversation(get_conversation_list: list) -> dict:
            # flatten conversation object
            obj = {}
            for conversation_line in get_conversation_list:
                obj.update(conversation_line)
            return obj

        def merge_conversation(search_name=search_name, tweets_graph=tweets_graph, user_graph=user_graph) -> dict:
            # merge user tweets and other users' tweets user is following
            conversation_between_users = {}
            try:
                user_tweets = conversation(get_conversation_list=tweets_graph[search_name])
            except KeyError as e:
                _ = e
            try:
                follows = sorted(user_graph[search_name])
            except KeyError as e:
                follows = []
                _ = e

            if follows:
                for followed in follows:
                    if followed in tweets_graph.keys():
                        followed_tweets = conversation(get_conversation_list=tweets_graph[followed])
                        conversation_between_users.update(followed_tweets)

            if user_tweets:
                conversation_between_users.update(user_tweets)

            return conversation_between_users

        print(search_name)
        conv = merge_conversation(search_name=search_name)

        # log tweet conversation
        try:
            for search_tweet_index in sorted(list(conv.keys())):
                for _user, _user_tweets in tweets_graph.items():
                    tmp = {}
                    [tmp.update(t) for t in _user_tweets]  # iterate through all tweets
                    if search_tweet_index in tmp.keys():
                        print("\t@{}: {}".format(_user, tmp[search_tweet_index]))
        except AttributeError as e:
            _ = e

        return None


if __name__ == "__main__":
    usr_graph = User().user_data()
    tweet_graph = Tweets().tweet_data()
    app = ConsoleApp(user_graph=usr_graph, tweets_graph=tweet_graph)
    app.console()
