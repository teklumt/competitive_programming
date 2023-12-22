class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        bol=True
        col=[[] for c in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    col[j].append(board[i][j])
        for i in col:
            if len(set(i))!=len(i):
                return False
        
        for i in range(len(board)):
            num=set()
            for j in board[i]:
                if j!="." and j in num:
                    return False
                num.add(j)
        
        for i in range(0,9,+3):
            for j in range(0,9,+3):
                
                num=set()
                for k in range(i,i+3,1):
                    for m in range(j,j+3,1):
                        if board[k][m]!="." and board[k][m] in num:
                            return False
                        num.add(board[k][m])
        return True

        
