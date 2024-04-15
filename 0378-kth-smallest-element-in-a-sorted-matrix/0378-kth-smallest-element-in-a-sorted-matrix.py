class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num = []
        heapify(num)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if len(num) < k:
                    heappush(num, -matrix[i][j])
                else:
                    heappushpop(num, -matrix[i][j])
      
        return -num[0]