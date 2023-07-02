class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        for m in nums:
            result.append(m*m)
        result.sort()
        return result