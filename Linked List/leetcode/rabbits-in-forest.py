class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter()
        answers.sort()
        res=0
        for i in answers:
            if count[i]==0:
                res+=i+1
                count[i]=i
            else:
                count[i]-=1
        return res
