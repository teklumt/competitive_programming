class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack=[]
        right=-inf
        for x in nums[::-1]:
            if x<right:
                return True
            while stack and stack[-1]<x:
                right=stack.pop()
            stack.append(x)
        return False
