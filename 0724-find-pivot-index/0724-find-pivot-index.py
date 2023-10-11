class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        post=sum(nums)
        pre=0
        for i in range(len(nums)):
            if i==0:
                if post-nums[i]==0:
                    return i
            elif i==len(nums)-1:
                pre=sum(nums)-nums[i]
                if pre==0:
                    return i
            else:
                pre=pre+nums[i-1]
                if post-pre-nums[i]==pre:
                    return i
        return -1