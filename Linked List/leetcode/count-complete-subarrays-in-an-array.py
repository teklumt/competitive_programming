class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        cc=len(set(nums))
       
        
        left=0
        temp={}
        for i in range(len(nums)):
            temp[nums[i]]=temp.get(nums[i],0)+1
            while len(temp) == cc:
                temp[nums[left]]-=1
                if temp[nums[left]]==0:
                    del temp[nums[left]]
                left+=1
            count+=left
        return count
