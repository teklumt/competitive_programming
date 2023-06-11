class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            x=nums.index(target)
            return x
        elif target<nums[0]:
            return 0
        else:
            n=1
            while True:
                if (target-n) in nums:
                    g=nums.index(target-n)
                    return g+1
                n=n+1
