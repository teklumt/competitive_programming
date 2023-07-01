class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        result=[]
        for n in nums:
            if n>0:
                pos.append(n)
            else:
                neg.append(n)
        for n in range(len(neg)) :
            result.append(pos[n])
            result.append(neg[n])
        return result