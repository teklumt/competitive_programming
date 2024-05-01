class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        num = nums[0]
        for i in range(1, len(nums)):
            num ^= nums[i]    
        return bin(num ^ k).count('1')