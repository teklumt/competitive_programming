class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(0, -1), (-1, 0), (1, 0),(0, 1)]
        def isvalid(i , j):
                return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        def check(n):
            seen = set([(0, 0)])
            stack = [(0, 0)]
            while stack:
                r , c = stack.pop()
                if r == (len(heights) - 1) and c == (len(heights[0]) - 1):
                    return True
                for dx, dy in directions:
                    newR, newC = r + dx, c + dy
                    if isvalid(newR, newC) and (newR, newC) not in seen and abs(heights[newR][newC] - heights[r][c]) <= n:
                        seen.add((newR, newC))
                        stack.append((newR, newC))
            return False 
            
            

        left , right = 0 , 10 ** 6 
        res = inf
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
            