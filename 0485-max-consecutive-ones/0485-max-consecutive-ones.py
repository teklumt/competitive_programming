class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count={}
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                count[j]=count.get(j,0)+1
            else:
                j+=1
        return 0 if len(count)==0 else max(count.values())