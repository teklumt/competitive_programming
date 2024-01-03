class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        presum=sum(skill)
        res=0
        skill.sort()
        n=presum//(len(skill)//2)
        i=0
        j=len(skill)-1
        while i<j:
            if skill[i]+skill[j]!=n:
                return -1
            res+=skill[i]*skill[j]
            i+=1
            j-=1
        return res