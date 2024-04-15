class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.num = nums
        self.k = k
        heapify(self.num)
        while len(self.num) > k:
            heappop(self.num)
          
    def add(self, val: int) -> int:
        if len(self.num) >= self.k:
            heappushpop(self.num, val)
        else:
            heappush(self.num, val)
        return self.num[0] 
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)