class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        result=[]
        for n in nums:
            if n%2==0:
                pos.append(n)
            else:
                neg.append(n)
        result.append(pos[:]+neg[:])
        return result[0]
