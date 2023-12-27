class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res=0
        maxx=0
        count=0

        for flip in flips:
            maxx=max(flip,maxx)
            count+=1
            if maxx==count:
                res+=1
        return res
