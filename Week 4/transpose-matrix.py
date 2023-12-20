class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = [[] for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                col[j].append(matrix[i][j])
        return col