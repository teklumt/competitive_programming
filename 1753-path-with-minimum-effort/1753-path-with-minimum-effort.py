class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0), (1, 0),(0, 1)]
        def isvalid(i , j):
                return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        def check(n, i , j, seen):
            if i == (len(heights) - 1) and j == (len(heights[0]) - 1):
                return True
            
            for r, c in directions:
                newR,  newC = i + r, j + c
                if isvalid(newR, newC) and ((newR, newC) not in seen) and (abs(heights[newR][newC] - heights[i][j]) <= n):
                    seen.add((newR,newC))
                    if check(n, newR, newC, seen):
                        return True
            return False
            

        left , right = 0 , 10 ** 6 
        res = inf
        while left <= right:
            mid = (left + right) // 2
            ch = check(mid, 0, 0, set([(0 , 0)]))
            if ch:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
            