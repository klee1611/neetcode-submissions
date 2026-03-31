class Twitter:

    def __init__(self):
        self.twits = defaultdict(list)
        self.follows = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.twits[userId].append((self.count, tweetId))
        self.count += 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.follows[userId]

        twits = []
        for f in follows:
            twits += [(-c, t) for (c, t) in self.twits[f]]
        if userId not in follows:
            twits += [(-c, t) for (c, t) in self.twits[userId]]
        heapq.heapify(twits)

        r = []
        while len(r) < 10 and twits:
            r.append(heapq.heappop(twits)[1])
        return r

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)