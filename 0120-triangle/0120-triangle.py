class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def IsBound(i, j):
            return 0 <= i < len(triangle) and 0 <= j < len(triangle[i])

        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):

                take = []
                if IsBound(i  - 1, j):take.append(triangle[i - 1][j])
                if IsBound(i  - 1, j - 1 ):take.append(triangle[i - 1][j - 1])
                triangle[i][j] += min(take) if take else 0
                # print(i, take, triangle)
        # print(triangle)
        return min(triangle[-1])



            