class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        empty = []
        for i in range(len(board)):
            for j in  range(len(board[0])):
                if board[i][j] == 'O' and (i == len(board) - 1 or i == 0 or j == 0  or j == len(board[0]) - 1):
                    empty.append((i, j))
                    board[i][j] = 'T'

        FourDirection = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def isValid(row, col):
            return (  0 <= row < len(board)) and (0 <= col < len(board[0]))

   
        queue = deque([empty])

        seen = set()
        while queue:
            curr = queue.popleft()
            tar = []

            for row, col in curr:
                for r, c in FourDirection:
                    newR, newC = row + r, col + c
                    if isValid(newR, newC ) and (newR, newC) not in seen:
                        if board[newR][newC] == 'O':
                            board[newR][newC] = 'T'
                            tar.append((newR, newC))
                        seen.add((newR, newC))
            # print(tar)
            if tar:
                queue.append(tar)
        
        for i in range(len(board)):
            for j in  range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'




