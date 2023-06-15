class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        result=[]
        if n==1:
            return nums[0]
        red=[]
        for m in range(n):
            if nums[m] not in red:
                count=nums.count(nums[m])   
                result.append([count,nums[m]])
                red.append(nums[m])
        result.sort()
        return result[-1][1]
            