class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num=sorted(nums)
        res=0
        for i in range(-2,-len(nums)-1,-2):
            res+=num[i]
        return res