class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr=[[0]*n for _ in range(m)]
        

        for i in guards:
            arr[i[0]][i[1]]='G' 

        for i in walls:
            arr[i[0]][i[1]]='W'
        
        for i in range(m):
            j=0
            while j < n:
                if arr[i][j]=='G':
                    l=j-1
                    while arr[i][l]!='G'and arr[i][l]!='W' and l>-1:
                        arr[i][l]='H'
                        l-=1
                    l=j+1
                    while l<n and arr[i][l]!='W' and arr[i][l]!='G'  :
                        arr[i][l]='H'
                        l+=1
                    
                    
                    k=i+1
                    while k<m and arr[k][j]!='W' and arr[k][j]!='G':
                        arr[k][j]='H'
                        k+=1
                    k=i-1
                    while k>-1 and arr[k][j]!='W' and arr[k][j]!='G':
                        arr[k][j]='H'
                        k-=1
                
                    j=l if l>j else j+1

                else:
                    j+=1
        count=0
        for i in range(m):
            for j in range(n):
                if arr[i][j]==0:
                    count+=1
        return count

