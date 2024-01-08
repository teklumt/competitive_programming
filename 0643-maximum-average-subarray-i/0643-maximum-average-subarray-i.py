class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        res=total/k
        left=0
        for i in range(k,len(nums)):
            total-=nums[left] 
            total+=nums[i] 
            res=max(res,total/k)
            left+=1
        return res

