class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        store={0:1}
        summ=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                nums[i]=0
            else:
                nums[i]=1
        
        for i in nums:
            summ+=i
            count+=store.get(summ-k,0)
            store[summ]=store.get(summ,0)+1
        return count
