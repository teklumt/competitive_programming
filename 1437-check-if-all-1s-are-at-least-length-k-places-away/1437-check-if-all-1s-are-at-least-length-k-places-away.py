class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        stack=[]
        win=[]
        for i in range(len(nums)):
            if nums[i]==1:
                if stack:
                    if i-stack[-1]-1<k:
                        return False
                stack.append(i)
        return True