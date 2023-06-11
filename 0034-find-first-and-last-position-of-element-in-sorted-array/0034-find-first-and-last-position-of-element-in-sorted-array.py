class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        else:
            x1=0
            x2=0
            count=0
            for n in range(len(nums)):
                if nums[n]==target:
                    if count==0:
                        x1=n
                        x2=n
                        count+=1
                    else:
                        x2=n
            return [x1,x2]