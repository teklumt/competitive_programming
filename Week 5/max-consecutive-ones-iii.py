class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        myhash = {1: 0, 0: 0}
        left = 0
        count = 0
        for i in range(len(nums)):
            myhash[nums[i]] += 1
            while myhash[0] > k:
                myhash[nums[left]] -= 1
                left += 1
            
            count = max(count, myhash[0]+myhash[1])
        return count