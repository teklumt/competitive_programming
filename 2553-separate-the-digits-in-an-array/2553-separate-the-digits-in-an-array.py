class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        final=[]
        for i in nums:
            j=str(i)
            result+=list(j)
        for i in result:
            final.append(int(i))
        return final