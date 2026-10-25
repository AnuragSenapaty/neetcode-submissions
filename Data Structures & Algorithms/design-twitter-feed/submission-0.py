from typing import List

class Twitter:

    def __init__(self):
        self.user_tweets = {}   # user_id -> list of indices into self.tweets
        self.user_follows = {}  # user_id -> set of followed user_ids
        self.tweets = []        # tweet ids, in posting order

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_tweets.setdefault(userId, []).append(len(self.tweets))
        self.tweets.append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # set of ids to read from: self + followees (avoids duplicates if self-follow)
        ids = {userId} | self.user_follows.get(userId, set())

        temp = []  # fresh list, so we never mutate stored data
        for uid in ids:
            temp.extend(self.user_tweets.get(uid, []))

        temp.sort(reverse=True)  # newest index first
        return [self.tweets[i] for i in temp[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_follows.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_follows.get(followerId, set()).discard(followeeId)