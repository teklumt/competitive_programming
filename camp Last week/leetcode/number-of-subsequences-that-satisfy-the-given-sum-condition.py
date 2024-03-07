class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod =  10 ** 9 + 7
        res = 0

        nums.sort()
        
        for i in range(len(nums)):
            ter = target - nums[i]
            ind = (bisect_right(nums, ter) - 1) - i
            if ind >= 0:
                res += 2**(ind) % mod
        return res % mod

