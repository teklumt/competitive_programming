class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if i%2==0:
                res+=[nums[i+1]]*nums[i]
        return res