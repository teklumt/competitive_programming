class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(target):
            if target == 0:
                return  1
            
            
            if target not in memo:
                for j in nums:
                    if j <= target:
                        memo[target] += dp(target - j)
            return memo[target]

        return dp(target)
