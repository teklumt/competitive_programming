class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        minn = maxx = res = nums[0]

        for i in range(1 , len(nums)):
            if nums[i] < 0:
                minn , maxx = maxx, minn

            minn = min(nums[i], nums[i] * minn)
            maxx = max(nums[i], nums[i] * maxx)

            res = max(res, maxx)
        return res