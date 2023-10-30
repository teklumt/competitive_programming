class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # neet
        nums.sort()
        left,right=0,0
        total,res=0,0
        while right<len(nums):
            total+=nums[right]
            while nums[right]*(right-left+1)>total+k:
                total-=nums[left]
                left+=1
            res=max(right-left+1,res)
            right+=1
        return res
        