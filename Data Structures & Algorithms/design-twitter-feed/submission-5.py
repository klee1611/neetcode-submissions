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
        self.follows[userId].add(userId)
        follows = list(self.follows[userId])

        t_index = [len(self.twits[f])-1 for f in follows]

        twits = []
        for i in range(len(t_index)):
            index = t_index[i]
            follow = follows[i]
            if index < 0:
                continue
            c, t = self.twits[follow][index]
            heapq.heappush(twits, (-c, t, index, follow))

        r = []
        while len(r) < 10 and twits:
            count, twit, index, follow = heapq.heappop(twits)
            r.append(twit)
            if index > 0:
                index -= 1
                c, t = self.twits[follow][index]
                heapq.heappush(twits, (-c, t, index, follow))
        return r

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)