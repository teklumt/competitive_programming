class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        def func(i):
            if i >= len(nums):
                return 0
            if i not in dp:
                dp[i] = 1
                for j in  range(i + 1, len(nums)):
                    if nums[j] > nums[i]:
                        dp[i]  = max(dp[i], func(j) + 1)
                
            return dp[i]
        maxx = 0
        for i in range(len(nums)):
            maxx = max(maxx, func(i))
            
        return maxx