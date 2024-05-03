class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        totX = nums[0]
        for i in range(1, len(nums)):
            totX ^= nums[i]
        
        res = []
        maxx = (2**maximumBit)- 1
        for i in nums[::-1]:
            res.append(maxx ^ totX)
            totX ^= i
        return res