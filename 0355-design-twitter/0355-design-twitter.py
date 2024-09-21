class Twitter:

    def __init__(self):
        self.Store = []  
        self.follows = defaultdict(set)  
    
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.Store.append([tweetId, userId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for tweetId, user in self.Store[::-1]:  
            if user == userId or user in self.follows[userId]: 
                res.append(tweetId)  
            if len(res) == 10:  
                break
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:  
            self.follows[followerId].remove(followeeId)


# Example usage:
# obj = Twitter()
# obj.postTweet(userId, tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId, followeeId)
# obj.unfollow(followerId, followeeId)
