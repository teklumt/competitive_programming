class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        stack1=[]
        stack2={}
        res2=[]
        for i in matches:
            stack2[i[1]]=stack2.get(i[1],0)+1
        for i in matches:
            if i[0] not in stack2:
                stack1.append(i[0])
        for i in stack2:
            if stack2[i]==1:
                res2.append(i)
        if stack1:
            stack1=list(set(stack1))
            stack1.sort()
        if res2:
            res2=list(set(res2))
            res2.sort()
        return[stack1,res2]
