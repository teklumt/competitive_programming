class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        res=[]
        for i in range(len(weights)-1):
            res.append(weights[i]+weights[i+1])
        res.sort()
        ans=0
        left=0
        right=len(res)-1
        while left<k-1:
            ans+=res[right]-res[left]
            # k-=1
            right-=1
            left+=1
        return ans
