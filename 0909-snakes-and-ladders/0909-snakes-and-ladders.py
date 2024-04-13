class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        newBoard = []

        
        for i in range(n):
            if i % 2 == 0:
                newBoard +=  board[n - 1 - i]
            else:
                newBoard += board[n - 1 - i][::-1]


        queue = deque([(1, 0)])
        seen = set()

        while queue:
            curr , level= queue.popleft()
            if curr == n * n:
                return level
           
            for j in range(curr + 1, min(curr + 6, n * n) + 1):
                if j not in seen:
                    seen.add(j)
                    if newBoard[j - 1] == -1:
                        queue.append((j, level + 1))

                    else:
                        queue.append((newBoard[j - 1] , level + 1))
             
        return -1
     