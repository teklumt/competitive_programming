class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        count=0
        res=[[] for i in range(len(strs[0]))]
        for i in range(len(strs)):
            for j in range(len(strs[0])):
                res[j].append(strs[i][j])
                        
        for re in res:
            if re != sorted(re):
                count+=1
        return count