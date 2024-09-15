class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1 , len(nums)):
                if abs(nums[i] - nums[j]) <= min((nums[i], nums[j])):
                    res = max(res, nums[i] ^ nums[j])
                else:
                    break
        return res