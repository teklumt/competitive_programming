class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=[]
        check=[]
        final=[]
        for n in nums:
            if n in result:
                check.append(n)
            else:
                result.append(n)
        for b in result:
            if b in check:
                pass
            else:
                final.append(b)
        return final