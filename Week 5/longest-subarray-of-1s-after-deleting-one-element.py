class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        currCount={1:0,0:0}
        res=0
        left=0
        bol=False
        for i in nums:
            if i==1:
                currCount[1]+=1
            else:
                bol=True
                while left<len(nums) and currCount[0]>0:
                    currCount[nums[left]]-=1
                    left+=1
                currCount[0]+=1
            res=max(res,currCount[1])
        return res if bol else res-1
