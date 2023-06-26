class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=[]
        check=[]
        for n in nums:
            if n in result:
                check.append(n)
            else:
                result.append(n)
        for b in result:
            if b in check:
                pass
            else:
                return b