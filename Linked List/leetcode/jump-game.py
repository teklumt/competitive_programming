class Solution:
    def canJump(self, nums: List[int]) -> bool:

        count=0
        for i in range(len(nums)):
            count=max(count,nums[i])
            if count==0 and i<len(nums)-1:
                return False
            count-=1
        return True











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
                # new=stack.copy()
                # new.reverse()
                if 'T' in stack[::-1][:nums[i]]:
                    stack.append('T')
                else:
                    stack.append('F')
        return True if stack[-1]=='T' else False
