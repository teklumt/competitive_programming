class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        res=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                res.append(i)
        if len(res)==0:
            if s==goal and len(set(s))<len(s):
                return True
            else:
                return False
        elif len(res)==2:
            if s[res[0]]==goal[res[1]] and s[res[1]]==goal[res[0]]:
                return True
            else:
                return False
        return False