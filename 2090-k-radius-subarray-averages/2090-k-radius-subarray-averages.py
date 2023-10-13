class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k==0:
            return nums
        summ=0
        res=[]
        left=0
        if len(nums)<2*k+1:
            return [-1]*len(nums)
        res+=[-1]*k
        for i in range(2*k+1):
            summ+=nums[i]
        res.append(summ//(2*k+1))
        for i in range(2*k+1,len(nums)):
            summ-=nums[left]
            summ+=nums[i]
            res.append(summ//(2*k+1))
            left+=1
        res+=[-1]*k
        return res
