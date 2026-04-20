class Twitter:

    def __init__(self):
        # contains userID -> [time, tweetID]
        self.tweetMap = defaultdict(list)

        # contains userID -> [following IDs]
        self.followMap = defaultdict(set)

        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        # iterate thru list of followee
        for followeeId in self.followMap[userId]:

            # check if they have any tweets
            if followeeId in self.tweetMap:
                # get number of tweets by followee
                index = len(self.tweetMap[followeeId]) - 1

                # get time and tweet
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
