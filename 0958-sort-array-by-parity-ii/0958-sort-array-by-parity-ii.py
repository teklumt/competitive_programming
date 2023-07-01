class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        result=[]
        for n in nums:
            if n%2==0:
                pos.append(n)
            else:
                neg.append(n)
        h=0
        j=0
        for i in range(len(nums)):
            if i%2==0:
                result.append(pos[h])
                h=h+1
            else:
                result.append(neg[j])
                j+=1
        return result