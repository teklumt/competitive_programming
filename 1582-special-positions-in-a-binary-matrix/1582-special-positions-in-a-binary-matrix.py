class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count=0
        col = [[] for _ in range(len(mat[0]))]
        for i  in range(len(mat)):
            for j in range(len(mat[0])):
                col[j].append(mat[i][j])
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==1 and mat[i].count(1)==1 and col[j].count(1)==1:
                    count+=1
            
        return count
        