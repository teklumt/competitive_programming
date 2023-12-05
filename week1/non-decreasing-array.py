class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i+1]<nums[i]:
                temp=nums[:i]+nums[i+1:]
                if sorted(temp)==temp:
                    return True
                temp=nums[:i+1]+nums[i+2:]
                if sorted(temp)==temp:
                    return True
                return False
        return True