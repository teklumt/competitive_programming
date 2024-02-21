class RecentCounter:

    def __init__(self):
        self.res=deque()
        

    def ping(self, t: int) -> int:
        while self.res and  self.res[0] < t-3000:
            self.res.popleft()
        self.res.append(t)
        return len(self.res)
            
               
  
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)