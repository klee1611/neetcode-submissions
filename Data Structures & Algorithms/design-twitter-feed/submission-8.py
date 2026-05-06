class Twitter:

    def __init__(self):
        self.follows = defaultdict(list)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.tweets[userId][:]
        for f in self.follows[userId]:
            tweets += self.tweets[f]
        tweets.sort(reverse = True)
        tweets = tweets[:10] if len(tweets) > 10 else tweets
        return [ tw for t, tw in tweets ]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId] or followeeId == followerId:
            return
        self.follows[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        for idx in range(len(self.follows[followerId])-1, -1, -1):
            Id = self.follows[followerId][idx]
            if Id == followeeId:
                self.follows[followerId].pop(idx)
                break