class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        if min(nums)>0:
            return 1
        if min(nums)==0:
            if nums[0]==0:
                return 1
            else:
                return 0
        if min(nums)<0:
            res=[0]
            for n in nums:
                res.append(res[-1]+n)
            return -1*(min(res))+1