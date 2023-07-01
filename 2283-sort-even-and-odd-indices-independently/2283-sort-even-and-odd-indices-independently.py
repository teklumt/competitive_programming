class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        neg=[]
        pos=[]
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        h=0
        j=0
        neg.sort()
        neg.reverse()
        pos.sort()
        for i in range(len(nums)):
            if i%2==0:
                result.append(pos[h])
                h=h+1
            else:
                result.append(neg[j])
                j+=1
        return result