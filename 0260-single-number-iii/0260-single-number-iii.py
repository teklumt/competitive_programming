class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        totX = 0
        for i in nums:
            totX ^= i 
        totX &= -totX
        x, y  = 0, 0
        for i in nums:
            if i & totX:
                x ^= i
            else:
                y ^= i 

        return [x, y]
        