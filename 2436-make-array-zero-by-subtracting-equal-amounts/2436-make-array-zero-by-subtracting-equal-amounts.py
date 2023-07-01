class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        j=set(nums)
        new=[]
        for k in j:
            new.append(k)
        nums=new.copy()
        nums.sort()
        count=0
        for n in range(len(nums)):
            result=[]
            if nums[n]==0:
                pass
            else:
                for m in range(n,len(nums)):
                    t=nums[m]-nums[n]
                    result.append(t)
                count+=1
                if(len(set(result))==1):
                    break
        return count
