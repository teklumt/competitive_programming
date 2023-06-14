class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bol=False
        for m in matrix:
            if target in m:
                bol=True
        return bol