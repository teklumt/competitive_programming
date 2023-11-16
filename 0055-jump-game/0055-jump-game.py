class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stack=['T']
        for i in range(len(nums)-2,-1,-1):
            if nums[i]==0:
                stack.append('F')
            elif nums[i]==1:
                if stack[-1]=='T':
                    stack.append('T')
                else:
                    stack.append('F')
            else:
                new=stack.copy()
                new.reverse()
                if 'T' in new[:nums[i]]:
                    stack.append('T')
                else:
                    stack.append('F')
        return True if stack[-1]=='T' else False
