class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        result = []
        for n in nums:
            if n > 0:
                break
            elif -1*n in nums:
                result.append(-1*n)
        if len(result) == 0:
            return -1
        else:
            return max(result)