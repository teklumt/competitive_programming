class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time=timeToLive
        self.store={}
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.store[tokenId] = currentTime + self.time        

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.store and self.store[tokenId] > currentTime:
            self.store[tokenId] = currentTime + self.time

    def countUnexpiredTokens(self, currentTime: int) -> int:
        curr=0
        for i in self.store:
            if self.store[i] > currentTime:
                curr+=1
        return curr
        
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)