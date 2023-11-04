class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res=0
        hash={}
        total=0
        left=0
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=i
                total+=nums[i]
            else:
                while nums[i] in hash:
                    del hash[nums[left]]
                    total-=nums[left]  
                    left+=1
                total+=nums[i]
                hash[nums[i]]=i
            res=max(res,total)
        return res