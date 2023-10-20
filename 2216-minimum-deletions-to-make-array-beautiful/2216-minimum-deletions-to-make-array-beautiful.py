class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        stack=[]
        for i in nums:
            if stack and len(stack)%2!=0 and i==stack[-1]:
                continue
            else:
                stack.append(i)
        return len(nums)-len(stack) if len(stack)%2==0 else len(nums)-len(stack)+1