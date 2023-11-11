class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res=0
        win={}
        left=0
        summ=0
        for i in range(len(nums)):
            if len(win)<k:
                while nums[i] in win:
                    del win[nums[left]]
                    summ-=nums[left]
                    left+=1
                summ+=nums[i]
                win[nums[i]]=1
                if len(win)==k:
                    res=max(res,summ)

            else:
                del win[nums[left]]
                summ-=nums[left]
                left+=1
                while nums[i] in win:
                    del win[nums[left]]
                    summ-=nums[left]
                    left+=1
                summ+=nums[i]
                win[nums[i]]=1
                res=max(res,summ)
        return res