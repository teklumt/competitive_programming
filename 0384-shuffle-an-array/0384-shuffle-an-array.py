class Solution:

    def __init__(self, nums: List[int]):
        self.normal=nums[:]
        self.shuff=nums
        

    def reset(self) -> List[int]:
        return self.normal
        

    def shuffle(self) -> List[int]:
        random.shuffle(self.shuff)
        return self.shuff
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()