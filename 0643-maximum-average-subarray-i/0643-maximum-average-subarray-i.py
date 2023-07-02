class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        ori = total
        i = 0
        j = k
        while j < len(nums):
            total -= nums[i]
            total += nums[j]
            if total > ori:
                ori = total
            i = i+1
            j = j+1
        return ori/k