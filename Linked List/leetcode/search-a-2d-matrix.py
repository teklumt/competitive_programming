class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            num = bisect_left(i, target)
            if num < len(matrix[0]) and i[num] == target:
                return True
        return False