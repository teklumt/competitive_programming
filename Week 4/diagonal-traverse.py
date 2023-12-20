class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        res=[]
        hash=defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                hash[i+j].append(mat[i][j])
        
        for i in hash:
            if i%2==0:
                res+=reversed(hash[i])
            else:
                res+=hash[i]
            
        
        return res