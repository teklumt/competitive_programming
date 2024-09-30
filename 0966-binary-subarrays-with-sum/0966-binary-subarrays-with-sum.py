class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        presum = {0:1}
        count = 0
        summ = 0
      
        for i in nums:
            summ += i
            count += presum.get(summ - goal, 0)
            presum[summ ] = presum.get(summ, 0) + 1
        return count
