class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        n = len(nums)
        if summ % k != 0 or max(nums) > summ // k:
            return False
        target = summ // k
        dp = [-1 for i in range(2 ** n)]
        dp[0] = target
        for mask in range(1 , 2** n):
            for j in range(n):
                if mask & (1 << j):
                    val = dp[mask ^ (1 <<  j)] - nums[j]
                    if val > 0:
                        dp[mask] = val
                        break
                    elif val == 0:
                        dp[mask] = target
                        break
        return dp[-1] == target


        
        