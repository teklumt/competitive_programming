class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        prifixSum=list(accumulate(nums,initial=0))
        for i in range(1,len(prifixSum)):
            if prifixSum[i-1]==prifixSum[-1]-prifixSum[i]:
                return i-1
        return -1
