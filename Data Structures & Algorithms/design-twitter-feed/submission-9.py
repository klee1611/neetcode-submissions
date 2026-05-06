class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.follows[userId].add(userId)
        res = []
        tweets_heap = []
        for Id in self.follows[userId]:
            idx = len(self.tweets[Id])
            if idx == 0:
                continue
            idx -= 1
            time, t_id = self.tweets[Id][idx]
            heapq.heappush(tweets_heap, (-time, t_id, Id, idx))

        while len(res) < 10 and tweets_heap:
            time, t_id, Id, idx = heapq.heappop(tweets_heap)
            res.append(t_id)
            if idx == 0:
                continue
            idx -= 1
            time, t_id = self.tweets[Id][idx]
            heapq.heappush(tweets_heap, (-time, t_id, Id, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)