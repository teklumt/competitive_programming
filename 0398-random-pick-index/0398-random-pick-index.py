class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.store={}
        for i in range(len(self.nums)):
            self.store[self.nums[i]]=self.store.get(self.nums[i],[])+[i]


    def pick(self, target: int) -> int:
        return random.choice(self.store[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)