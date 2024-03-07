class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        row = len(matrix)
        col = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2
            r , c = mid // col, mid % col

            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


        


