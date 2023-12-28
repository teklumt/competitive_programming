class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        hash=defaultdict(list)
        for i in range (len(mat)):
            for j in range(len(mat[0])):
                hash[i-j].append(mat[i][j])
        for i in hash:
            hash[i]=sorted(hash[i])
        for i in range (len(mat)):
            for j in range(len(mat[0])):
                hash[i-j].append(mat[i][j])
    
        k=0
        for i in range (len(mat)):
            for j in range(len(mat[0])):
                mat[i][j]=hash[i-j][k]
                del hash[i-j][0]
        return mat            
