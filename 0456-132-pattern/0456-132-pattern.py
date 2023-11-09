class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        minn=-inf
        stack=[]
        for i in nums[::-1]:
            if i<minn:
                return True
            while stack and stack[-1]<i:
                minn=stack.pop()
            stack.append(i)
        return False