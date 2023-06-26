class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)
        bol=True
        for n in nums:
            if n!=m:
                if 2*n>m:
                    bol=False
        if bol:
            return nums.index(m)
        else:
            return -1